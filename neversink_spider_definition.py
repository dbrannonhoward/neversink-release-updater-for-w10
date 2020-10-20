import datetime
import os
import scrapy
from scrapy.crawler import CrawlerProcess

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


class TwistedReactor:

    def __init__(self, spider_definition=NeverSinkSpider):
        self.output_file = "releases.json"
        self.delete_existing_output_file()
        self.spider_definition = spider_definition
        self.process = CrawlerProcess(settings={
            "FEEDS": {
                self.output_file: {
                    "format": "json"},
            },
        })

    def crawl(self):
        self.process.crawl(self.spider_definition)
        self.process.start()  # the script will block here til crawling is finished
        return self.output_file

    def delete_existing_output_file(self):
        if os.path.exists(self.output_file):
            os.remove(self.output_file)


if __name__ == '__main__':
    tr = TwistedReactor(spider_definition=NeverSinkSpider)
    tr.crawl()
