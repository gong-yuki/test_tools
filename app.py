#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time : 2021/8/25 16:57
# @Author : gongyq
# @File : app.py
from flask import Flask, jsonify
from exts import db
# from flask_wtf import CSRFProtect
from tlogger import logger_create
# from flask_cors import CORS
from public.decorators import t_middleware

try:
    from local_config import SERVER_ENV
except ImportError:
    SERVER_ENV = 'product'


class CreateApp(Flask):

    # def make_response(self, rv):
    #     if isinstance(rv, dict):
    #         rv = jsonify(format_response(rv))
    #     # # url关于最后面 / 的308重定向
    #     # elif getattr(rv, 'code') == 308:
    #     #     new_rv = rv
    #     # else:
    #     #     raise DataTypeErrorException
    #     return super().make_response(rv)

    def run(self, host='0.0.0.0', port=5000, debug=True, workers=None, load_dotenv=True, server_env=None, **options):
        if server_env == 'develop' or SERVER_ENV == 'develop':
            super().run(host='0.0.0.0', port=port, debug=debug)
        else:
            import multiprocessing
            from gunicorn.app.base import BaseApplication

            class Application(BaseApplication):

                def __init__(self, app, local_options=None):
                    self.options = local_options or {}
                    self.application = app
                    super(Application, self).__init__()

                def load_config(self):
                    config = dict([(key, value) for key, value in self.options.items()
                                   if key in self.cfg.settings and value is not None])
                    for key, value in config.items():
                        self.cfg.set(key.lower(), value)

                def load(self):
                    return self.application

                def init(self, parser, opts, args):
                    super(Application, self).init(parser, opts, args)

            # 设置gunicorn的配置，bind监听请求，与指定socket进行板顶
            # workers工作进程的数量，依靠操作系统来提供负载均衡，推进的worker数量是(2*$num_cores)+1
            # worker_class工作进程类型，包括sync（默认）,eventlet,gevent,tornado,gthread,gaiohttp
            current_options = {
                'bind': f'{host}:{port}',
                'workers': workers or (multiprocessing.cpu_count() * 2) + 1,
                'worker_class': 'gevent',
                'timeout': '1800',
            }

            Application(self, current_options).run()


def register_logger(app, config):
    logger_create(config.SERVICE_NAME, app)


def create_app(config):
    print(SERVER_ENV)
    app = CreateApp(config.SERVICE_NAME)
    app.config.from_object(config)
    t_middleware(app)
    db.init_app(app)
    # CORS(app, supports_credentials=True)  # 设置参数
    # CORS(app, ={r"/*": {"origins": "*"}}, send_wildcard=True)  # 设置参数
    # CAS(app)
    # CSRFProtect(app)
    register_logger(app, config)
    return app

