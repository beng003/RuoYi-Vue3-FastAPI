from enum import Enum


class BusinessType(Enum):
    """
    业务操作类型

    OTHER: 其它
    INSERT: 新增
    UPDATE: 修改
    DELETE: 删除
    GRANT: 授权
    EXPORT: 导出
    IMPORT: 导入
    FORCE: 强退
    GENCODE: 生成代码
    CLEAN: 清空数据
    """

    OTHER = 0
    INSERT = 1
    UPDATE = 2
    DELETE = 3
    GRANT = 4
    EXPORT = 5
    IMPORT = 6
    FORCE = 7
    GENCODE = 8
    CLEAN = 9


class RedisInitKeyConfig(Enum):
    """
    系统内置Redis键名
    """

    @property
    def key(self):
        return self.value.get('key')

    @property
    def remark(self):
        return self.value.get('remark')

    ACCESS_TOKEN = {'key': 'access_token', 'remark': '登录令牌信息'}
    SYS_DICT = {'key': 'sys_dict', 'remark': '数据字典'}
    SYS_CONFIG = {'key': 'sys_config', 'remark': '配置信息'}
    CAPTCHA_CODES = {'key': 'captcha_codes', 'remark': '图片验证码'}
    ACCOUNT_LOCK = {'key': 'account_lock', 'remark': '用户锁定'}
    PASSWORD_ERROR_COUNT = {'key': 'password_error_count', 'remark': '密码错误次数'}
    SMS_CODE = {'key': 'sms_code', 'remark': '短信验证码'}


# # note: Enum中的枚举成员是单例对象
# # 1. Enum访问单个枚举成员
# access_token_key = RedisInitKeyConfig.ACCESS_TOKEN.key  # 'access_token'
# access_token_remark = RedisInitKeyConfig.ACCESS_TOKEN.remark  # '登录令牌信息'
# print(f"Redis键名: {access_token_key}, 用途: {access_token_remark}")

# # 2. 使用枚举设置/获取 Redis 数据
# r.set(RedisInitKeyConfig.PASSWORD_ERROR_COUNT.key, 3)
# error_count = r.get(RedisInitKeyConfig.PASSWORD_ERROR_COUNT.key)
# # 结合业务逻辑
# if int(error_count) > 5:
#     r.set(RedisInitKeyConfig.ACCOUNT_LOCK.key, 'locked')