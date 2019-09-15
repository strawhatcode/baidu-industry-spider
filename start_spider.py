import csv
import time

from baidu_theme_spider.baiduSpider import BaiduSpider
from baidu_theme_spider.config import CONFIG

if __name__ == '__main__':
    begin_time = time.time()
    d = BaiduSpider(CONFIG['themeid'], CONFIG['startdate'], CONFIG['enddate'], CONFIG['dateinterval'])
    count = 0
    with open('baidu_lvyou2.csv', 'w', encoding='utf-8', newline='') as f:
        csv_f = csv.writer(f)
        csv_f.writerow(['name', 'value', 'date'])
        for datas in d.get_respones(CONFIG['pagesize']):
            for data in datas:
                if len(data) < 1:
                    continue
                count += 1
                csv_f.writerow(data)
                print('**************************【已解析[ {} ]条数据,当前数据为 {} 】**************************'
                      .format(count, data))
    print("**************************【所有数据解析完毕，总用时[ {} ]秒】**************************"
          .format(time.time() - begin_time))

