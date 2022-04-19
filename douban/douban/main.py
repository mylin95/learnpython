from scrapy import cmdline

# 数据抓取
# cmdline.execute('scrapy crawl douban_spider'.split())

# 数据抓取，并输出到 test.json 文件（unicode编码格式存储）
# cmdline.execute('scrapy crawl douban_spider -o test.json'.split())

# 数据抓取，并输出到 test.csv 文件（需要转文件编码为：UTF-BOM）
cmdline.execute('scrapy crawl douban_spider -o test.csv'.split())