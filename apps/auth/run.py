#!/usr/bin/env python
# -*- encoding: utf-8 -*-python No module named 'pwd'
# @Time : 2021/8/25 17:30
# @Author : gongyq
# @File : run.py
from apps.auth.setting import config

if config.SERVER_ENV != 'develop':
    from gevent import monkey

    monkey.patch_all()
else:
    pass

from app import create_app as raw_app
from apps.auth.views.auth import authBP


def register_blueprints(app):
    app.register_blueprint(authBP, url_prefix="/v1/auth/")


def create_app():
    app = raw_app(config)
    register_blueprints(app)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(port=config.PORT)
