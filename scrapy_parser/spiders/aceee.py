from datetime import datetime

import scrapy

class AceeeSpider(scrapy.Spider):
    name = "aceee"
    
    now = datetime.now()
    datestring = now.strftime("%Y-%m-%d")
    
    start_urls = [
            'https://aceee.org/news-blog'
            ]

    flag = False
    def parse(self, response):
        hrefs = response.css('.news-content-box h2 a::attr(href)').getall()
        if self.flag is False:
            self.flag = True
            for href in hrefs:
                yield response.follow(href, self.parse_article)
        else:
            for i in range(1, len(hrefs)):
                yield response.follow(hrefs[i], self.parse_article)
        
        next_page = response.css('li.next a::attr(href)').get()

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_article(self, response):
        text = (" ".join(response.xpath('//article/div/div/div/div//text()[not(ancestor::*[@class="form-submit"])]').extract())).replace("\xa0", "")
        yield {
            'title': response.xpath('//meta[@name="dcterms.title"]/@content').get(),
            'pubdate': response.xpath('//meta[@name="dcterms.date"]/@content').get(),
            'datestring': self.datestring,
            'categories': response.xpath('//div[@class="pane-content"]/ul[@class="views-summary"]/li/a/text()').extract(),
            'article_body': text,
            'tags': response.xpath('//div[@class="views-field views-field-term-node-tid"]/span[@class="field-content"]/i/a/text()').extract(),
            'external_links': response.xpath('//article/div/div/div/div//a/@href').extract()
        }
