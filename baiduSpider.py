
import json
import time
import datetime
import requests
import random
from .config import USERAGENT


class BaiduSpider:

    def __init__(self, themeid, startdate, enddate, dateinterval):
        self.themeid = themeid
        self.startdate = startdate
        self.enddate = enddate
        self.dateinterval = dateinterval

    """请求头，随机useragent"""
    def headers(self):
        useragent = random.choice(USERAGENT)
        header = {
            'user-agent': useragent
        }
        return header

    """
        发送请求的方法
    """
    def get_respones(self, pagesize):
        url = 'http://insight.baidu.com/base/search/rank/listByArea'
        params = {
            'pageSize': pagesize,
            'source': 0,
            'dimensionid': self.themeid,
            'rateType': 100,
            'area': 0,
            'filterNodes': ''

        }
        datetype = self.date_split(self.startdate, self.enddate, self.dateinterval)
        count = 0
        for i in datetype:
            count += 1
            params['dateType'] = i
            sleep_time = random.random() + 0.5
            time.sleep(sleep_time)
            res = requests.get(url=url, params=params, headers=self.headers())
            print("------------------------【已发送[ {} ]个请求】------------------------".format(count))
            yield self.parse_data(res.text)

    """
        解析请求返回来的数据
    """
    def parse_data(self, res_data):
        data_list = []
        datas = json.loads(res_data)
        data = datas['data']['results']
        if len(data['current']) < 1:
            return data_list
        else:
            date = data['currDate'].split('~')[0]
            for d in data['current']:
                temp_list = [d['item'], d['value'], date]
                data_list.append(temp_list)
        return data_list

    """
        对起始日期和终止日期根据范围进行分隔
    """
    def date_split(self, startdate, enddate, dateinterval):
        startdate = datetime.datetime.strptime(startdate, '%Y%m%d')
        enddate = datetime.datetime.strptime(enddate, '%Y%m%d')
        enddate = enddate + datetime.timedelta(days=1)
        total_days = (enddate - startdate).days + 1
        if total_days % dateinterval == 0:
            loop_count = total_days // dateinterval
        else:
            loop_count = total_days // dateinterval + 1
        date_list = []
        start = startdate
        for i in range(0, loop_count):
            if i == loop_count - 1:
                end = start + datetime.timedelta(days=total_days % dateinterval - 1)
            else:
                end = start + datetime.timedelta(days=dateinterval - 1)

            date_list.append(self.filter_date(start, end))

            start = end + datetime.timedelta(days=1)
        return date_list

    """把每一段日期改成字符串参数"""
    def filter_date(self, startdate, enddate):
        str_start = ''
        str_end = ''
        for d1 in str(startdate)[0:10].split('-'):
            str_start += d1
        for d2 in str(enddate)[0:10].split('-'):
            str_end += d2
        return str_start + '~' + str_end
