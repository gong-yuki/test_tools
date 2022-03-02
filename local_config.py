#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time : 2021/8/25 17:18
# @Author : gongyq
# @File : local_config.py

# 服务 ： dev 开发环境
SERVER_ENV = 'develop'

# 开启调试
DEBUG = True

# 数据库连接地址
DB_USERNAME = 'root'
DB_PASSWORD = '123456'
DB_HOST = '127.0.0.1'
DB_PORT = '3306'
DB_NAME = 'test_tools_dev'

DB_URI = 'mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8' % (DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)

SQLALCHEMY_DATABASE_URI = DB_URI
# 配置 sql 修改进行不追踪
SQLALCHEMY_TRACK_MODIFICATIONS = True

# 启用任务调度
SCHEDULER_API_ENABLED = True

# Response 的 message 和 code 的配置
MSG_MAP = {
    0: 'ok',

    101: 'can not find object',
    102: 'save object error',
    103: '标题或名称重复',
    104: 'can not create object',
    105: 'remove failed',
    106: 'operate failed',
    108: 'permission denied',
    109: 'project permission denied',
    110: '无此操作权限，请联系管理员',

    201: 'field required',
    202: 'field length error',

    301: 'password wrong',
    303: 'username or password wrong',

    401: 'not login!',
    403: 'not allowed!',
    404: 'not found!',
    410: 'auth expired!',
    411: 'auth error!',
    413: 'username is not exist or password error!',
    414: 'invalid data!',
    415: 'open file failed!'
}

# 测试用例文档表头
CASE_FILE_HEADER = ["流程案例编号", "流程案例名称", "测试要点", "总前置条件", "测试步骤", "系统", "角色", "前置条件", "步骤描述", "预期结果", "实际结果", "案例执行结果",
                    "测试人", "测试日期", "测试截图"]

# 冒烟测试清单表头
SMOKE_TEST_HEADER = ["产品", "模块", "验证点", "操作", "预期结果", "执行人", "执行结果"]
