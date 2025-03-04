from config.env import DataBaseConfig


class CommonConstant:
    """
    常用常量

    WWW: www主域
    HTTP: http请求
    HTTPS: https请求
    LOOKUP_RMI: RMI远程方法调用
    LOOKUP_LDAP: LDAP远程方法调用
    LOOKUP_LDAPS: LDAPS远程方法调用
    YES: 是否为系统默认（是）
    NO: 是否为系统默认（否）
    DEPT_NORMAL: 部门正常状态
    DEPT_DISABLE: 部门停用状态
    UNIQUE: 校验是否唯一的返回标识（是）
    NOT_UNIQUE: 校验是否唯一的返回标识（否）
    """

    WWW = 'www.'
    HTTP = 'http://'
    HTTPS = 'https://'
    LOOKUP_RMI = 'rmi:'
    LOOKUP_LDAP = 'ldap:'
    LOOKUP_LDAPS = 'ldaps:'
    YES = 'Y'
    NO = 'N'
    DEPT_NORMAL = '0'
    DEPT_DISABLE = '1'
    UNIQUE = True
    NOT_UNIQUE = False


class HttpStatusConstant:
    """
    返回状态码

    SUCCESS: 操作成功
    CREATED: 对象创建成功
    ACCEPTED: 请求已经被接受
    NO_CONTENT: 操作已经执行成功，但是没有返回数据
    MOVED_PERM: 资源已被移除
    SEE_OTHER: 重定向
    NOT_MODIFIED: 资源没有被修改
    BAD_REQUEST: 参数列表错误（缺少，格式不匹配）
    UNAUTHORIZED: 未授权
    FORBIDDEN: 访问受限，授权过期
    NOT_FOUND: 资源，服务未找到
    BAD_METHOD: 不允许的http方法
    CONFLICT: 资源冲突，或者资源被锁
    UNSUPPORTED_TYPE: 不支持的数据，媒体类型
    ERROR: 系统内部错误
    NOT_IMPLEMENTED: 接口未实现
    WARN: 系统警告消息
    """

    SUCCESS = 200
    CREATED = 201
    ACCEPTED = 202
    NO_CONTENT = 204
    MOVED_PERM = 301
    SEE_OTHER = 303
    NOT_MODIFIED = 304
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    BAD_METHOD = 405
    CONFLICT = 409
    UNSUPPORTED_TYPE = 415
    ERROR = 500
    NOT_IMPLEMENTED = 501
    WARN = 601


class JobConstant:
    """
    定时任务常量

    JOB_ERROR_LIST: 定时任务禁止调用模块及违规字符串列表
    JOB_WHITE_LIST: 定时任务允许调用模块列表
    """

    JOB_ERROR_LIST = [
        'app',
        'config',
        'exceptions',
        'import ',
        'middlewares',
        'module_admin',
        'open(',
        'os.',
        'server',
        'sub_applications',
        'subprocess.',
        'sys.',
        'utils',
        'while ',
        '__import__',
        '"',
        "'",
        ',',
        '?',
        ':',
        ';',
        '/',
        '|',
        '+',
        '-',
        '=',
        '~',
        '!',
        '#',
        '$',
        '%',
        '^',
        '&',
        '*',
        '<',
        '>',
        '(',
        ')',
        '[',
        ']',
        '{',
        '}',
        ' ',
    ]
    JOB_WHITE_LIST = ['module_task']


class MenuConstant:
    """
    菜单常量

    TYPE_DIR: 菜单类型（目录）
    TYPE_MENU: 菜单类型（菜单）
    TYPE_BUTTON: 菜单类型（按钮）
    YES_FRAME: 是否菜单外链（是）
    NO_FRAME: 是否菜单外链（否）
    LAYOUT: Layout组件标识
    PARENT_VIEW: ParentView组件标识
    INNER_LINK: InnerLink组件标识
    """

    TYPE_DIR = 'M'
    TYPE_MENU = 'C'
    TYPE_BUTTON = 'F'
    YES_FRAME = 0
    NO_FRAME = 1
    LAYOUT = 'Layout'
    PARENT_VIEW = 'ParentView'
    INNER_LINK = 'InnerLink'


class GenConstant:
    """
    代码生成器核心配置常量
    
    主要包含四大类配置：
    
    1. 模板配置 - 定义代码生成器支持的模板类型
       TPL_CRUD: 基础CRUD模板（单表操作）
       TPL_TREE: 树形结构模板（包含父子关系）
       TPL_SUB:  主子表模板（一对多关系）
    
    2. 数据库适配 - 根据 DataBaseConfig.db_type 动态适配不同数据库类型
       COLUMNTYPE_STR:    字符串类型字段集合（适配 PostgreSQL/MySQL 等）
       COLUMNTYPE_TEXT:   大文本类型字段集合
       COLUMNTYPE_TIME:   时间类型字段集合（包含带时区类型）
       COLUMNTYPE_GEOMETRY: 空间数据类型集合（点线面等几何图形）
       COLUMNTYPE_NUMBER: 数字类型字段集合（整型/浮点型等）
    
    3. 字段控制 - 定义代码生成时需要特殊处理的字段
       COLUMNNAME_NOT_EDIT:  禁止在前端编辑的字段（如ID/创建时间等）
       COLUMNNAME_NOT_LIST:  不在列表页显示的字段
       COLUMNNAME_NOT_QUERY: 不参与查询的字段
       BASE_ENTITY: 基础实体类包含字段（createBy/createTime等）
       TREE_ENTITY: 树形实体类特殊字段（parentId/children等）
    
    4. 类型映射系统 - 数据库类型到编程语言的类型转换
       DB_TO_SQLALCHEMY_TYPE_MAPPING: 数据库类型 → SQLAlchemy 类型映射
       DB_TO_PYTHON_TYPE_MAPPING:     数据库类型 → Python 原生类型映射
    
    5. 前端组件配置 - 定义生成的表单控件类型
       HTML_INPUT:      文本框
       HTML_DATETIME:   日期时间选择器
       HTML_IMAGE_UPLOAD: 图片上传组件
       ...其他控件类型...
    """

    # 模板类型标识（值对应模板目录名称）
    TPL_CRUD = 'crud'  # 基础增删改查模板
    TPL_TREE = 'tree'  # 树形结构模板 
    TPL_SUB = 'sub'    # 主子表模板

    # 树形结构字段配置（用于树表模板）
    TREE_CODE = 'treeCode'         # 树节点编码字段名
    TREE_PARENT_CODE = 'treeParentCode'  # 树父节点编码字段名
    TREE_NAME = 'treeName'         # 树显示名称字段名

    # 动态数据库类型配置（根据 db_type 切换类型集合）
    COLUMNTYPE_STR = (
        ['character varying', 'varchar', 'character', 'char']  # PostgreSQL字符串类型
        if DataBaseConfig.db_type == 'postgresql'
        else ['char', 'varchar', 'nvarchar', 'varchar2']      # 其他数据库字符串类型
    )
    COLUMNTYPE_TEXT = (
        ['text', 'citext'] if DataBaseConfig.db_type == 'postgresql' else ['tinytext', 'text', 'mediumtext', 'longtext']
    )
    COLUMNTYPE_TIME = (
        [
            'date',
            'time',
            'time with time zone',
            'time without time zone',
            'timestamp',
            'timestamp with time zone',
            'timestamp without time zone',
            'interval',
        ]
        if DataBaseConfig.db_type == 'postgresql'
        else ['datetime', 'time', 'date', 'timestamp']
    )
    COLUMNTYPE_GEOMETRY = (
        ['point', 'line', 'lseg', 'box', 'path', 'polygon', 'circle']
        if DataBaseConfig.db_type == 'postgresql'
        else [
            'geometry',
            'point',
            'linestring',
            'polygon',
            'multipoint',
            'multilinestring',
            'multipolygon',
            'geometrycollection',
        ]
    )
    COLUMNTYPE_NUMBER = [
        'tinyint',
        'smallint',
        'mediumint',
        'int',
        'number',
        'integer',
        'bit',
        'bigint',
        'float',
        'double',
        'decimal',
    ]
    COLUMNNAME_NOT_EDIT = ['id', 'create_by', 'create_time', 'del_flag']
    COLUMNNAME_NOT_LIST = ['id', 'create_by', 'create_time', 'del_flag', 'update_by', 'update_time']
    COLUMNNAME_NOT_QUERY = ['id', 'create_by', 'create_time', 'del_flag', 'update_by', 'update_time', 'remark']
    BASE_ENTITY = ['createBy', 'createTime', 'updateBy', 'updateTime', 'remark']
    TREE_ENTITY = ['parentName', 'parentId', 'orderNum', 'ancestors', 'children']
    HTML_INPUT = 'input'
    HTML_TEXTAREA = 'textarea'
    HTML_SELECT = 'select'
    HTML_RADIO = 'radio'
    HTML_CHECKBOX = 'checkbox'
    HTML_DATETIME = 'datetime'
    HTML_IMAGE_UPLOAD = 'imageUpload'
    HTML_FILE_UPLOAD = 'fileUpload'
    HTML_EDITOR = 'editor'
    TYPE_DECIMAL = 'Decimal'
    TYPE_DATE = ['date', 'time', 'datetime']
    QUERY_LIKE = 'LIKE'
    QUERY_EQ = 'EQ'
    REQUIRE = '1'
    DB_TO_SQLALCHEMY_TYPE_MAPPING = (
        {
            'boolean': 'Boolean',
            'smallint': 'SmallInteger',
            'integer': 'Integer',
            'bigint': 'BigInteger',
            'real': 'Float',
            'double precision': 'Float',
            'numeric': 'Numeric',
            'character varying': 'String',
            'character': 'String',
            'text': 'Text',
            'bytea': 'LargeBinary',
            'date': 'Date',
            'time': 'Time',
            'time with time zone': 'Time',
            'time without time zone': 'Time',
            'timestamp': 'DateTime',
            'timestamp with time zone': 'DateTime',
            'timestamp without time zone': 'DateTime',
            'interval': 'Interval',
            'json': 'JSON',
            'jsonb': 'JSONB',
            'uuid': 'Uuid',
            'inet': 'INET',
            'cidr': 'CIDR',
            'macaddr': 'MACADDR',
            'point': 'Geometry',
            'line': 'Geometry',
            'lseg': 'Geometry',
            'box': 'Geometry',
            'path': 'Geometry',
            'polygon': 'Geometry',
            'circle': 'Geometry',
            'bit': 'Bit',
            'bit varying': 'Bit',
            'tsvector': 'TSVECTOR',
            'tsquery': 'TSQUERY',
            'xml': 'String',
            'array': 'ARRAY',
            'composite': 'JSON',
            'enum': 'Enum',
            'range': 'Range',
            'money': 'Numeric',
            'pg_lsn': 'BigInteger',
            'txid_snapshot': 'String',
            'oid': 'BigInteger',
            'regproc': 'String',
            'regclass': 'String',
            'regtype': 'String',
            'regrole': 'String',
            'regnamespace': 'String',
            'int2vector': 'ARRAY',
            'oidvector': 'ARRAY',
            'pg_node_tree': 'Text',
        }
        if DataBaseConfig.db_type == 'postgresql'
        else {
            # 数值类型
            'TINYINT': 'SmallInteger',
            'SMALLINT': 'SmallInteger',
            'MEDIUMINT': 'Integer',
            'INT': 'Integer',
            'INTEGER': 'Integer',
            'BIGINT': 'BigInteger',
            'FLOAT': 'Float',
            'DOUBLE': 'Float',
            'DECIMAL': 'DECIMAL',
            'BIT': 'Integer',
            # 日期和时间类型
            'DATE': 'Date',
            'TIME': 'Time',
            'DATETIME': 'DateTime',
            'TIMESTAMP': 'TIMESTAMP',
            'YEAR': 'Integer',
            # 字符串类型
            'CHAR': 'CHAR',
            'VARCHAR': 'String',
            'TINYTEXT': 'Text',
            'TEXT': 'Text',
            'MEDIUMTEXT': 'Text',
            'LONGTEXT': 'Text',
            'BINARY': 'BINARY',
            'VARBINARY': 'VARBINARY',
            'TINYBLOB': 'LargeBinary',
            'BLOB': 'LargeBinary',
            'MEDIUMBLOB': 'LargeBinary',
            'LONGBLOB': 'LargeBinary',
            # 枚举和集合类型
            'ENUM': 'Enum',
            'SET': 'String',
            # JSON 类型
            'JSON': 'JSON',
            # 空间数据类型（需要扩展支持，如 GeoAlchemy2）
            'GEOMETRY': 'Geometry',  # 需要安装 geoalchemy2
            'POINT': 'Geometry',
            'LINESTRING': 'Geometry',
            'POLYGON': 'Geometry',
            'MULTIPOINT': 'Geometry',
            'MULTILINESTRING': 'Geometry',
            'MULTIPOLYGON': 'Geometry',
            'GEOMETRYCOLLECTION': 'Geometry',
        }
    )
    DB_TO_PYTHON_TYPE_MAPPING = (
        {
            'boolean': 'bool',
            'smallint': 'int',
            'integer': 'int',
            'bigint': 'int',
            'real': 'float',
            'double precision': 'float',
            'numeric': 'Decimal',
            'character varying': 'str',
            'character': 'str',
            'text': 'str',
            'bytea': 'bytes',
            'date': 'date',
            'time': 'time',
            'time with time zone': 'time',
            'time without time zone': 'time',
            'timestamp': 'datetime',
            'timestamp with time zone': 'datetime',
            'timestamp without time zone': 'datetime',
            'interval': 'timedelta',
            'json': 'dict',
            'jsonb': 'dict',
            'uuid': 'str',
            'inet': 'str',
            'cidr': 'str',
            'macaddr': 'str',
            'point': 'list',
            'line': 'list',
            'lseg': 'list',
            'box': 'list',
            'path': 'list',
            'polygon': 'list',
            'circle': 'list',
            'bit': 'int',
            'bit varying': 'int',
            'tsvector': 'str',
            'tsquery': 'str',
            'xml': 'str',
            'array': 'list',
            'composite': 'dict',
            'enum': 'str',
            'range': 'list',
            'money': 'Decimal',
            'pg_lsn': 'int',
            'txid_snapshot': 'str',
            'oid': 'int',
            'regproc': 'str',
            'regclass': 'str',
            'regtype': 'str',
            'regrole': 'str',
            'regnamespace': 'str',
            'int2vector': 'list',
            'oidvector': 'list',
            'pg_node_tree': 'str',
        }
        if DataBaseConfig.db_type == 'postgresql'
        else {
            # 数值类型
            'TINYINT': 'int',
            'SMALLINT': 'int',
            'MEDIUMINT': 'int',
            'INT': 'int',
            'INTEGER': 'int',
            'BIGINT': 'int',
            'FLOAT': 'float',
            'DOUBLE': 'float',
            'DECIMAL': 'Decimal',
            'BIT': 'int',
            # 日期和时间类型
            'DATE': 'date',
            'TIME': 'time',
            'DATETIME': 'datetime',
            'TIMESTAMP': 'datetime',
            'YEAR': 'int',
            # 字符串类型
            'CHAR': 'str',
            'VARCHAR': 'str',
            'TINYTEXT': 'str',
            'TEXT': 'str',
            'MEDIUMTEXT': 'str',
            'LONGTEXT': 'str',
            'BINARY': 'bytes',
            'VARBINARY': 'bytes',
            'TINYBLOB': 'bytes',
            'BLOB': 'bytes',
            'MEDIUMBLOB': 'bytes',
            'LONGBLOB': 'bytes',
            # 枚举和集合类型
            'ENUM': 'str',
            'SET': 'str',
            # JSON 类型
            'JSON': 'dict',
            # 空间数据类型（通常需要特殊处理）
            'GEOMETRY': 'bytes',
            'POINT': 'bytes',
            'LINESTRING': 'bytes',
            'POLYGON': 'bytes',
            'MULTIPOINT': 'bytes',
            'MULTILINESTRING': 'bytes',
            'MULTIPOLYGON': 'bytes',
            'GEOMETRYCOLLECTION': 'bytes',
        }
    )
