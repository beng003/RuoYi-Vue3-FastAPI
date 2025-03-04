from contextlib import asynccontextmanager
from fastapi import FastAPI
from config.env import AppConfig
from config.get_db import init_create_table
from config.get_redis import RedisUtil
from config.get_scheduler import SchedulerUtil
from exceptions.handle import handle_exception
from middlewares.handle import handle_middleware
from module_admin.controller.cache_controller import cacheController
from module_admin.controller.captcha_controller import captchaController
from module_admin.controller.common_controller import commonController
from module_admin.controller.config_controller import configController
from module_admin.controller.dept_controller import deptController
from module_admin.controller.dict_controller import dictController
from module_admin.controller.log_controller import logController
from module_admin.controller.login_controller import loginController
from module_admin.controller.job_controller import jobController
from module_admin.controller.menu_controller import menuController
from module_admin.controller.notice_controller import noticeController
from module_admin.controller.online_controller import onlineController
from module_admin.controller.post_controler import postController
from module_admin.controller.role_controller import roleController
from module_admin.controller.server_controller import serverController
from module_admin.controller.user_controller import userController
from module_generator.controller.gen_controller import genController
from sub_applications.handle import handle_sub_applications
from utils.common_util import worship
from utils.log_util import logger


# 生命周期事件
# note: contextlib生命周期管理（启动前准备 → 运行 → 关闭清理）
@asynccontextmanager
async def lifespan(app: FastAPI):
    # 启动阶段
    logger.info(f'{AppConfig.app_name}开始启动')
    worship()  # 打印启动艺术字
    await init_create_table()  # 初始化数据库表结构
    app.state.redis = await RedisUtil.create_redis_pool()  # 创建Redis连接池
    await RedisUtil.init_sys_dict(app.state.redis)  # 加载字典到Redis缓存
    await RedisUtil.init_sys_config(app.state.redis)  # 加载系统参数到Redis缓存
    await SchedulerUtil.init_system_scheduler()  # 启动定时任务
    logger.info(f'{AppConfig.app_name}启动成功')
    
    # 运行阶段
    yield  
    
    # 关闭阶段
    await RedisUtil.close_redis_pool(app)  # 关闭Redis连接池
    await SchedulerUtil.close_system_scheduler()  # 关闭定时任务

# FastAPI核心对象初始化
app = FastAPI(
    title=AppConfig.app_name,  # 从配置读取应用名称
    description=f'{AppConfig.app_name}接口文档',  # 自动生成API文档描述
    version=AppConfig.app_version,  # 从配置读取版本号
    lifespan=lifespan,  # 挂载生命周期处理器
)

# 挂载子应用
handle_sub_applications(app)
# 加载中间件处理方法
handle_middleware(app)
# 加载全局异常处理方法
handle_exception(app)


# 加载路由列表
controller_list = [
    {'router': loginController, 'tags': ['登录模块']},
    {'router': captchaController, 'tags': ['验证码模块']},
    {'router': userController, 'tags': ['系统管理-用户管理']},
    {'router': roleController, 'tags': ['系统管理-角色管理']},
    {'router': menuController, 'tags': ['系统管理-菜单管理']},
    {'router': deptController, 'tags': ['系统管理-部门管理']},
    {'router': postController, 'tags': ['系统管理-岗位管理']},
    {'router': dictController, 'tags': ['系统管理-字典管理']},
    {'router': configController, 'tags': ['系统管理-参数管理']},
    {'router': noticeController, 'tags': ['系统管理-通知公告管理']},
    {'router': logController, 'tags': ['系统管理-日志管理']},
    {'router': onlineController, 'tags': ['系统监控-在线用户']},
    {'router': jobController, 'tags': ['系统监控-定时任务']},
    {'router': serverController, 'tags': ['系统监控-菜单管理']},
    {'router': cacheController, 'tags': ['系统监控-缓存监控']},
    {'router': commonController, 'tags': ['通用模块']},
    {'router': genController, 'tags': ['代码生成']},
]

for controller in controller_list:
    app.include_router(router=controller.get('router'), tags=controller.get('tags'))
