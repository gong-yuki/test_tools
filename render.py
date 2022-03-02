#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time : 2021/8/25 17:10
# @Author : gongyq
# @File : render.py

import json
from flask import make_response, jsonify, send_from_directory
from local_config import MSG_MAP


def format_response(res):
    res_keys = res.keys()
    if 'code' not in res_keys:
        res['code'] = 0
    if 'message' not in res_keys:
        res['message'] = MSG_MAP.get(res['code'], '')
    if 'data' not in res_keys:
        res['data'] = []
    return res


def _render(resp):
    response = make_response(jsonify(resp))
    response.status = str(resp["code"])
    # response.headers["Access-Control-Allow-Origin"] = "*"
    return response

def file_render(filepath, filename):
    response = make_response(send_from_directory(filepath, filename, as_attachment=True))
    response.headers["Content-Disposition"] = "attachment; filename={}".format(filename.encode().decode('latin-1'))
    return response


def json_render(response):
    if 'code' not in response.keys():
        response['code'] = 0
    if 'message' not in response.keys():
        response['message'] = MSG_MAP.get(response['code'], '')
    return _render(response)


def json_list_render(code, data, limit, offset, message=None):
    if message is None:
        message = MSG_MAP.get(code)
    resp = dict(
        code=code, limit=limit, offset=offset, message=message, data=data)
    return _render(resp)


def json_list_render2(code, data, page_size, page_index, total, message=None):
    if message is None:
        message = MSG_MAP.get(code)
    resp = dict(
        code=code, pageSize=page_size, currentPage=page_index, total=total, message=message, list=data)
    return _render(resp)


def json_detail_render(code, data=None, message=None, total=None):
    if data is None:
        data = []
    if message is None:
        message = MSG_MAP.get(code)
    resp = dict(code=code, message=message, data=data)
    if total:
        resp['total'] = total
    return _render(resp)


def json_token_render(code, token, message=None):
    if message is None:
        message = MSG_MAP.get(code)
    resp = dict(code=code, token=token, message=message)
    return _render(resp)


def json_detail_render_sse(code, data=None, message=None):
    if data is None:
        data = []
    if message is None:
        message = MSG_MAP.get(code)
    resp = dict(code=code, message=message, data=data)
    return json.dumps(resp)


def row2list(rows):
    data = []
    for row in rows:
        if hasattr(row, '_asdict'):
            rv = row._asdict()
        else:
            rv = row.__dict__
        for k, v in rv.items():
            if not isinstance(v, str):
                rv.pop(k)
                break
        data.append(rv)
    return data
