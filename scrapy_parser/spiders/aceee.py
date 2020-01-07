from datetime import datetime
import csv

import scrapy

class AceeeSpider(scrapy.Spider):
    name = "aceee"
    
    now = datetime.now()
    datestring = now.strftime("%Y-%m-%d")
    
    start_urls = [
            'https://aceee.org/news-blog'
            ]

    with open('%s.csv'%name, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['title', 'pubdate', 'datestring', 'categories', 'article_body', 'tags', 'external_links'])
            
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
        data = {
            'title': response.xpath('//meta[@name="dcterms.title"]/@content').get(),
            'pubdate': (response.xpath('//meta[@name="dcterms.date"]/@content').get()).split('T', 1)[0],
            'datestring': self.datestring,
            'categories': "",
            'article_body': (" ".join(response.xpath('//article[@class="node node-job clearfix"]/div/div/div/div//text()[not(ancestor::*[@class="form-submit"])]').extract())).replace("\xa0", ""),
            'tags': ", ".join(response.xpath('//div[@class="views-field views-field-term-node-tid"]/span[@class="field-content"]/i/a/text()').extract()),
            'external_links': ", ".join(response.xpath('//article[@class="node node-job clearfix"]/div/div/div/div//a/@href').extract())
        }
        with open('%s.csv'%self.name, 'a', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow([data['title'], data['pubdate'], data['datestring'], data['categories'], data['article_body'], data['tags'], data['external_links']])

