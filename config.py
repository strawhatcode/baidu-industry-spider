# user-agent，每次都随机选择一个ua作为请求头来发送请求
USERAGENT = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36',
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
]

CONFIG = {
    # 行业id
    'themeid': 12,
    # 开始时间
    'startdate': '20191213',
    # 终止时间
    'enddate': '20191231',
    # 按几天为一个时间范围
    'dateinterval': 1,
    # 每页显示多少条数据
    'pagesize': 30,
    # 最终数据保存为csv的路径
    'save_csv_path': 'baidu_phone2.csv'
}