import os
import sys
import time
from loguru import logger as _logger
from typing import Dict
from middlewares.trace_middleware import TraceCtx

class LoggerInitializer:
    def __init__(self):
        self.log_path = os.path.join(os.getcwd(), 'logs')
        self.__ensure_log_directory_exists()
        self.log_path_error = os.path.join(self.log_path, f'{time.strftime("%Y-%m-%d")}_error.log')

    def __ensure_log_directory_exists(self):
        """
        确保日志目录存在，如果不存在则创建
        """
        if not os.path.exists(self.log_path):
            os.mkdir(self.log_path)

    @staticmethod
    def __filter(log: Dict):
        """
        自定义日志过滤器，添加trace_id
        """
        log['trace_id'] = TraceCtx.get_id()
        return log

    def init_log(self):
        """
        初始化日志配置
        """
        # note: loguru日志初始化配置
        # 自定义日志格式
        # 日志格式分解说明：
        format_str = (
            '<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | '  # 精确到毫秒的时间戳
            '<cyan>{trace_id}</cyan> | '                        # 请求追踪ID（来自中间件）
            '<level>{level: <8}</level> | '                     # 对齐的日志级别标签
            '<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - '  # 代码位置
            '<level>{message}</level>'                          # 日志内容
        )
        _logger.remove()
        
        # 移除后重新添加sys.stderr, 目的: 控制台输出与文件日志内容和结构一致
        # 参数详解：
        # 1. sys.stderr -> 将日志输出到控制台（与print默认的stdout分离，避免日志与程序输出混杂）
        # 2. filter     -> 通过__filter方法注入trace_id（来自中间件的请求追踪ID）
        # 3. format_str -> 彩色日志格式：时间 | trace_id | 日志级别 | 代码位置 | 消息
        # 4. enqueue    -> 解决多线程日志乱序问题（生产环境必须开启）
        _logger.add(sys.stderr, filter=self.__filter, format=format_str, enqueue=True)
        _logger.add(
            self.log_path_error,
            filter=self.__filter,
            format=format_str,
            rotation='50MB',  # 日志文件达到50MB自动分割
            encoding='utf-8',  # 确保中文日志正常存储
            enqueue=True,  # 线程安全写入
            compression='zip',   # 自动压缩历史日志
        )

        return _logger


# 初始化日志处理器
log_initializer = LoggerInitializer()
logger = log_initializer.init_log()
