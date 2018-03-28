#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/28 20:05
# @Author  : Dengsc
# @Site    : 
# @File    : utils.py
# @Software: PyCharm


import re
import pytz
import string
import random
import logging
from datetime import datetime, timedelta

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(filename)s[line:%(lineno)d]: %(message)s')
logger = logging.getLogger(__name__)


def utc_to_datetime(utc_time_str, utc_format='%Y-%m-%dT%H:%M:%S.%fZ', local_format='%Y-%m-%d %H:%M:%S'):
    """
    UTC时间转本地时间
    :param utc_time_str: UTC时间字符串
    :param utc_format: UTC时间格式
    :param local_format: 本地时间格式
    :return: str 本地时间
    """

    try:
        local_tz = pytz.timezone('Asia/Chongqing')
        utc_dt = datetime.datetime.strptime(utc_time_str, utc_format)
        local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
        return local_dt.strftime(local_format)
    except Exception as e:
        logger.error('[utc_to_datetime] %s --> %s' % (utc_time_str, str(e)))
        return None


def mem_unit(data_value):
    """
    存储数值可读转换
    :param data_value:数值 
    :return: 可读字符串
    """

    units = {'0': 'byte',
             '1': 'KB',
             '2': 'MB',
             '3': 'GB',
             '4': 'TB',
             '5': 'PB'
             }
    try:
        data = float(data_value)
        times = 0
        while abs(data) > 1024:
            data /= 1024
            times += 1
            ''' 达到最大计量单位'''
            if times == 5:
                break
        return '%.2f %s' % (data, units.get(str(times)))
    except Exception as e:
        logger.error('[calculate_unit] --> %s' % str(e))
        return data_value


def date_unit(data_value):
    """
    秒数数值可读转换
    :param data_value:数值 
    :return: 可读计量日期
    """

    units = {'0': u'秒',
             '1': u'分钟',
             '2': u'小时',
             '3': u'天'
             }
    try:
        data = float(data_value)
        times = 0
        while abs(data) > 60:
            data /= 60
            times += 1
            ''' 达到天计量单位'''
            if times == 2 and abs(data) > 24:
                data /= 24
                times += 1
                break
        return '%.2f %s' % (data, units.get(str(times)))
    except Exception as e:
        logger.error('[date_unit] --> %s' % str(e))
        return ''


def transform_size(size):
    """
    可读存储数值转换为byte
    :param size: <str> 1 K
    :return: <float> 1024.0
    """

    units = {
             'K': 1024.0,
             'M': 1024.0 * 1024,
             'G': 1024.0 * 1024 * 1024,
             'T': 1024.0 * 1024 * 1024 * 1024,
             'P': 1024.0 * 1024 * 1024 * 1024 * 1024,
             'default': 1.0
             }

    try:
        size = str(size).upper()
        _pat = r'([-]?[\d.]+)\s*([KMGTP]?)[B]?'
        result = re.compile(_pat).match(size).groups()
        num, unit = result if result else (size, 'default')
        return float(num) * units.get(unit if unit else 'default')
    except Exception as e:
        logger.error(u'[transform_size] --> %s' % str(e))
        return size


def calc_date(date_id, offset):
    """
    取日期偏移
    :param date_id: YYYYMMDD
    :param offset: int
    :return: YYYYMMDD
    """

    try:
        fmt = '%Y%m%d'
        str_date = datetime.strptime(date_id, fmt)
        off_date = str_date + timedelta(days=offset)
        return off_date.strftime(fmt)
    except Exception as e:
        logger.error('[get_last_date] --> errmsg:%s' % str(e))
        return None


def is_date(date_id, fmt):
    """
    判断输入字符串能否格式化为日期
    :param date_id: str yyyymmdd
    :param fmt: str %Y%m%d
    :return: bool True/False
    """
    try:
        datetime.strptime(date_id, fmt)
        return True
    except Exception as e:
        logger.error('date format error [%s] --> [%s] ,errmsg: %s' % (date_id, fmt, str(e)))
        return False


def timestamp_to_datetime(timestamp, fmt='%Y-%m-%d %H:%M:%S', convert_to_local=True):
    """
    UNIX时间戳转datetime
    :param timestamp: int, log, float
    :param fmt: %Y%m%d
    :param convert_to_local: True/False
    :return: str
    """
    try:
        dt = datetime.utcfromtimestamp(int(timestamp))
        if convert_to_local:
            dt = dt + timedelta(hours=8)
        return dt.strftime(fmt)
    except Exception as e:
        logger.error('timestamp_to_datetime error [%s] --> [%s] , errmsg: %s' % (timestamp, fmt, str(e)))
        return None


def threshold_value_style(value):
    """
    设置阈值
    :param value: 值
    :return: str
    """
    value = int(value)
    if value < 50:
        return 'success'
    elif value < 80:
        return 'warning'
    else:
        return 'danger'


def password_create(length=8):
    """
    随机密码生成
    :return: str
    """
    all_choice = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for i in range(length):
        password += random.choice(all_choice)
    return password
