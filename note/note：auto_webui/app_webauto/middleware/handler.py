#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽
import os

from common import yaml_handler, excel_handler, logging_handler, requests_handler
from config import config


class Handler:
    conf = config

    # YAML 数据
    yaml = yaml_handler.read_yaml(os.path.join(config.CONFIG_PATH, "config.yml"))

    # excel 数据
    __excel_path = conf.DATA_PATH
    __excel_file = yaml["excel"]["file"]
    excel = excel_handler.ExcelHandler(os.path.join(__excel_path, __excel_file))

    # logger
    __logger_config = yaml["logger"]
    logger = logging_handler.get_logger(
        name=__logger_config["name"],
        file=os.path.join(config.LOG_PATH, __logger_config["file"]),
        logger_level=__logger_config["logger_level"],
        stream_level=__logger_config["stream_level"],
        file_level=__logger_config["file_level"]
    )



if __name__ == '__main__':
    pass