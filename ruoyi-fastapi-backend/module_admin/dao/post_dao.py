from sqlalchemy import delete, func, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from module_admin.entity.do.post_do import SysPost
from module_admin.entity.do.user_do import SysUserPost
from module_admin.entity.vo.post_vo import PostModel, PostPageQueryModel
from utils.page_util import PageUtil


class PostDao:
    """
    岗位管理模块数据库操作层
    """

    @classmethod
    async def get_post_by_id(cls, db: AsyncSession, post_id: int):
        """
        根据岗位id获取在用岗位详细信息

        :param db: orm对象
        :param post_id: 岗位id
        :return: 在用岗位信息对象
        """
        post_info = (
            (await db.execute(select(SysPost).where(SysPost.post_id == post_id, SysPost.status == '0')))
            .scalars()
            .first()
        )

        return post_info

    @classmethod
    async def get_post_detail_by_id(cls, db: AsyncSession, post_id: int):
        """
        根据岗位id获取岗位详细信息

        :param db: orm对象
        :param post_id: 岗位id
        :return: 岗位信息对象
        """
        post_info = (await db.execute(select(SysPost).where(SysPost.post_id == post_id))).scalars().first()

        return post_info

    @classmethod
    async def get_post_detail_by_info(cls, db: AsyncSession, post: PostModel):
        """
        根据岗位参数获取岗位信息

        :param db: orm对象
        :param post: 岗位参数对象
        :return: 岗位信息对象
        """
        post_info = (
            (
                await db.execute(
                    select(SysPost).where(
                        SysPost.post_name == post.post_name if post.post_name else True,
                        SysPost.post_code == post.post_code if post.post_code else True,
                        SysPost.post_sort == post.post_sort if post.post_sort else True,
                    )
                )
            )
            .scalars()
            .first()
        )

        return post_info

    @classmethod
    async def get_post_list(cls, db: AsyncSession, query_object: PostPageQueryModel, is_page: bool = False):
        """
        根据查询参数获取岗位列表信息（支持分页）
        
        :param db: 异步数据库会话
        :param query_object: 包含分页参数和过滤条件的查询对象
        :param is_page: 是否启用分页（True返回分页结果，False返回全部数据）
        :return: 岗位列表（分页或完整列表）
        """
        
        # note: SQL构建基础查询语句
        query = (
            select(SysPost)  # 选择岗位表所有字段
            .where(  # 动态过滤条件
                # question: 为什么使用模糊匹配而不是精确匹配？
                # answer: 模糊匹配可以提高查询效率，精确匹配可能会导致查询结果不精确
                # 岗位编码模糊查询（如果query_object有post_code参数）
                SysPost.post_code.like(f'%{query_object.post_code}%') if query_object.post_code else True,
                # 岗位名称模糊查询（如果query_object有post_name参数）
                SysPost.post_name.like(f'%{query_object.post_name}%') if query_object.post_name else True,
                # 状态精确匹配（如果query_object有status参数）
                SysPost.status == query_object.status if query_object.status else True,
            )
            .order_by(SysPost.post_sort)  # 按排序字段升序排列
            .distinct()  # 去重查询结果
        )
        
        # 执行分页/全量查询
        post_list = await PageUtil.paginate(
            db,                # 数据库会话
            query,             # 构建好的查询语句
            query_object.page_num,    # 当前页码
            query_object.page_size,   # 每页条数
            is_page            # 是否分页标志
        )
        
        return post_list

    @classmethod
    async def add_post_dao(cls, db: AsyncSession, post: PostModel):
        """
        新增岗位数据库操作

        :param db: orm对象
        :param post: 岗位对象
        :return:
        """
        db_post = SysPost(**post.model_dump())
        db.add(db_post)
        await db.flush()

        return db_post

    @classmethod
    async def edit_post_dao(cls, db: AsyncSession, post: dict):
        """
        编辑岗位数据库操作

        :param db: orm对象
        :param post: 需要更新的岗位字典
        :return:
        """
        await db.execute(update(SysPost), [post])

    @classmethod
    async def delete_post_dao(cls, db: AsyncSession, post: PostModel):
        """
        删除岗位数据库操作

        :param db: orm对象
        :param post: 岗位对象
        :return:
        """
        await db.execute(delete(SysPost).where(SysPost.post_id.in_([post.post_id])))

    @classmethod
    async def count_user_post_dao(cls, db: AsyncSession, post_id: int):
        """
        根据岗位id查询岗位关联的用户数量

        :param db: orm对象
        :param post_id: 岗位id
        :return: 岗位关联的用户数量
        """
        user_post_count = (
            await db.execute(select(func.count('*')).select_from(SysUserPost).where(SysUserPost.post_id == post_id))
        ).scalar()

        return user_post_count
