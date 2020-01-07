import scrapy

class AceeeSpider(scrapy.Spider):
    name = "aceee"
    
#    start_urls = [
#            'https://aceee.org/news-blog'
#            ]

    start_urls = [
        'https://aceee.org/blog/2020/01/2019-and-2020-good-bad-and-ugly'
    ]

#    def parse(self, response):
#        for article in response.css('.news-content-box h2'):
#            yield {
#                'title': article.css('a::text').get(),
#                'link': article.css('a::attr(href)').get()
#            }
#
#        next_page = response.css('li.next a::attr(href)').get()

#        if next_page is not None:
#            yield response.follow(next_page, callback=self.parse)

    def parse(self, response):
        text = " ".join(response.xpath('//article/div/div/div/div//text()').extract())
        yield {
            'title': response.xpath('//meta[@name="dcterms.title"]/@content').get(),
            'pubdate': response.xpath('//meta[@name="dcterms.date"]/@content').get(),
            'datestring': '2020-01-08',
            'categories': response.xpath('//div[@class="pane-content"]/ul[@class="views-summary"]/li/a/text()').extract(),
            'article_body': text,
            'tags': response.xpath('//div[@class="views-field views-field-term-node-tid"]/span[@class="field-content"]/i/a/text()').extract(),
            'external_links': response.xpath('//article/div/div/div/div//a/@href').extract()
        }

# заголовок: response.xpath("//meta[@name='dcterms.title']/@content").get()

# ссылка: response.xpath("//link[@rel='shortlink']/@href").get()

# дата публикации: response.xpath("//meta[@name='dcterms.date']/@content").get()

# категории: response.xpath('//div[@class="pane-content"]/ul[@class="views-summary"]/li/a/text()').extract()

# текст статьи: response.xpath('//article/div/div/div/div//text()').extract()
#   concat из массива в строку

# теги: response.xpath('//div[@class="views-field views-field-term-node-tid"]/span[@class="field-content"]/i/a/text()').extract()

# ссылки: response.xpath('//article/div/div/div/div//a/@href').extract()

# ------------------------------------------------------------------------------

# Заголовки
# response.css('.news-content-box h2 a::text').getall()

# Ссылки
# response.css('.news-content-box h2 a::attr(href)').getall()

# Следующая страница
# response.css('li.next a::attr(href)').get()

