import scrapy

from CONSTANTS import NEVERSINK_GITHUB_URL

# from a virtual environment, run as : python -m cmd
# where cmd = scrapy runspider this_module_name.py -o filename.jl
# this module contains spider definition, results written to filename.jl


class NeverSinkSpider(scrapy.Spider):
    name = 'releases'
    # the crawler engine makes requests to these urls
    # this generates a response to be parsed
    start_urls = [
        NEVERSINK_GITHUB_URL,
    ]

    # parse is the default callback method of the crawler
    def parse(self, response):
        for release in response.css('div.release-header'):
            yield {
                'release': release.css('a::text').get(default='not found'),
            }

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
