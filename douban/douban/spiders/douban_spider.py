import scrapy
from douban.items import DoubanItem

class DoubanSpiderSpider(scrapy.Spider):
    # 爬虫名
    name = 'douban_spider'
    # 允许的域名
    allowed_domains = ['movie.douban.com']
    # 入口URL,扔到调度器里面去
    start_urls = ['https://movie.douban.com/top250']
    # 默认解析方法
    def parse(self, response):
        # print(response.text)
        # 循环电影的条目
        movie_list = response.xpath("//div[@class='article']/ol[@class='grid_view']/li")
        print(movie_list)
        for i_item in movie_list:
            # item文件导进来
            douban_item = DoubanItem()
            # 写详细的xpath，进行数据解析
            douban_item['serial_number'] = i_item.xpath(".//div[@class='item']//em/text()").extract_first()
            douban_item['movie_name'] = i_item.xpath(".//div[@class='item']//div[@class='hd']/a/span[1]/text()").extract_first()
            # 数据处理（多行）
            content = i_item.xpath(".//div[@class='item']//div[@class='bd']/p[1]/text()").extract()
            for i_content in content:
                content_s = "".join(i_content.split())
                douban_item['introduce'] = content_s
            # print(douban_item['introduce'])
            douban_item['star'] = i_item.xpath(".//span[@class='rating_num']/text()").extract_first()
            douban_item['evaluate'] = i_item.xpath(".//div[@class='star']/span[4]/text()").extract_first()
            douban_item['describe'] = i_item.xpath(".//span[@class='inq']/text()").extract_first()
            # 将数据yield到pipelines里面（然后进行数据清洗，存储等）
            yield douban_item
        # 解析下一页规则，取后页的xpath
        next_link = response.xpath("//span[@class='next']/link/@href").extract()
        if next_link:
            next_link = next_link[0]
            yield scrapy.Request("https://movie.douban.com/top250" + next_link, callback=self.parse)

