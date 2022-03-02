#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time : 2021/8/25 17:00
# @Author : gongyq
# @File : exts.py

from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import create_engine
# from local_config import SQLALCHEMY_BINDS

db = SQLAlchemy()


def getLatestRecord(record):
    """
    获取最新添加的记录
    :return:
    """
    db.session.add(record)
    db.session.commit()
    # print(record.id)
    # queryList = db.session.execute("SELECT LAST_INSERT_ID();").fetchall()
    # latestRecord = model.query.filter_by(id=queryList[0][0]).first()
    return record