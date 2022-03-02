#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time : 2021/8/26 9:45
# @Author : gongyq
# @File : extentions.py

import os
import yaml
from os.path import dirname, abspath, join, splitext
from flask import current_app
from public.validate import Validate


current_path = dirname(abspath(__file__))

yml_json = {}

try:
    yml_path = join(current_path, "validations")
    for file in os.listdir(yml_path):
        if splitext(file)[-1] != '.yml':
            continue
        with open(join(yml_path, file), "rb") as f:
            yml_json.update(yaml.safe_load(f.read()))
except yaml.YAMLError as e:
    current_app.logger.info(e)


v = Validate(yml_json)
validate = v.validation