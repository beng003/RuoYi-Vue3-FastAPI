# -*- coding: utf-8 -*-
"""
@author: peng
@file: ctx.py
@time: 2025/1/17  16:57
"""

# note: 上下文变量 (contextvars) 是Python 3.7+的特性，用于解决：
# 1. 异步编程中线程局部变量(thread-local)失效的问题
# 2. 在协程链路中保持请求级别的状态
# 3. 每个请求拥有独立的变量副本，互不干扰

import contextvars
from uuid import uuid4

# note: contextvars.ContextVar创建名为'request-id'的上下文变量
# 作用：在异步请求链路中保持唯一追踪ID
# # 特殊全局变量
# # 声明一次的全局变量
# # 协程/线程变量
# # 通过像全局变量一样声明一次提供统一的、协程/线程独立的变量代码结构
CTX_REQUEST_ID: contextvars.ContextVar[str] = contextvars.ContextVar('request-id', default='')


class TraceCtx:
    @staticmethod
    def set_id():
        _id = uuid4().hex
        CTX_REQUEST_ID.set(_id)
        return _id

    @staticmethod
    def get_id():
        return CTX_REQUEST_ID.get()
