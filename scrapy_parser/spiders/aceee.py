import scrapy

class AceeeSpider(scrapy.Spider):
    name = "aceee"
    
    start_urls = [
            'https://aceee.org/news-blog'
            ]

    def parse(self, response):
        for article in response.css('.news-content-box h2'):
            yield {
                'title': article.css('a::text').get(),
                'link': article.css('a::attr(href)').get()
            }

        next_page = response.css('li.next a::attr(href)').get()

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

#        page = response.url.split("/")[-1]
#        filename = 'aceee-%s.html' % page
#        with open(filename, 'wb') as f:
#            f.write(response.body)


# Заголовки
# response.css('.news-content-box h2 a::text').getall()
#'Local Governments Vote Resoundingly for Improved Efficiency in National Model Energy Code',
#'2019 and 2020: The Good, the Bad, and the Ugly',
#'Great Holiday News: Building Code to Make New Homes and Buildings More Energy Efficient  ',
#' Trump Administration Defies 2007 Law and Ties Americans to Energy-Wasting Bulbs ',
#'Can autonomous vehicles help cities address their climate goals? Only if they start planning now',
#'First-of-Its-Kind Report Reveals Dramatic Energy Efficiency Impacts, Warns of Stalled Progress in Face of Climate Challenge',
#'Tool allows communities to assess clean energy progress; Montgomery County calls it ‘innovative’',
#'New Year’s countdown: Our top 10 blog posts of 2019',
#'Twelve Strategies To Step Up Global Energy Efficiency',
#'Companies control majority of US energy use, but most lack efficiency goals',
#'Grid-interactive efficient buildings are the future, and utilities can help lead the way'

# Ссылки
# response.css('.news-content-box h2 a::attr(href)').getall()
#'/press/2020/01/local-governments-vote-resoundingly',
#'/blog/2020/01/2019-and-2020-good-bad-and-ugly',
#'/press/2019/12/great-holiday-news-building-code',
#'/press/2019/12/trump-administration-defies-2007-0',
#'/blog/2019/12/can-autonomous-vehicles-help-cities-0',
#'/press/2019/12/first-its-kind-report-reveals',
#'/blog/2019/12/tool-allows-communities-assess-clean',
#'/blog/2019/12/new-year-s-countdown-our-top-10-blog',
#'/press/2019/12/twelve-strategies-step-global-energy',
#'/blog/2019/11/companies-control-majority-us-energy',
#'/blog/2019/11/grid-interactive-efficient-buildings']

# Следующая страница
# response.css('li.next a::attr(href)').get()

