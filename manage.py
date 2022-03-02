#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time : 2021/8/25 17:40
# @Author : gongyq
# @File : manage.py
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from apps.testcase.run import create_app
from exts import db
from apps.testcase.models.casefile import CaseFile
from apps.testcase.models.casetemplate import CaseTemplate
from apps.testcase.models.casedetail import CaseDetail


app = create_app()

manager = Manager(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()