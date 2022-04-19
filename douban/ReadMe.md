# 数据抓取
python 数据抓取 豆瓣电影 top250 页面的数据

## 数据抓取：
- 原生：urllib requests
- scrapy

## Scrapy抓取4步走：
1. 新建项目
2. 明确目标
3. 制作爬虫
4. 存储内容

## python 依赖安装包下载地址：https://pypi.org/
```shell script
pip install scrapy
scrapy startproject douban
scrapy genspider douban_spider movie.douban.com
yum -y install sqlite3
#运行
scrapy crawl douban_spider
scrapy crawl douban_spider -o test.json
scrapy crawl douban_spider -o test.csv
```
目标网站：https://movie.douban.com/top250
