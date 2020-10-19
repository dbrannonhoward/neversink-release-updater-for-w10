import scrapy


from CONSTANTS import NEVERSINK_GITHUB_URL
from CONSTANTS import NEVERSINK_LOCAL_PATH


class NeverSink:

    def __init__(self):
        self.local_folder_location = NEVERSINK_LOCAL_PATH
        self.remote_web_location = NEVERSINK_GITHUB_URL
        self.scraper_module = 'neversink_spider_definition.py'
        self.scraper_spider_args = '-o'
        self.output_file = 'releases.jl'
        self.local_version = self.get_local_version()
        self.remote_version = self.get_remote_version()
        self.load_runtime_module()

    def get_local_version(self):
        return 'pass'

    def get_remote_version(self):
        self.scrape_remote_version_to_disk()
        return self.parse_remote_version_file()

    def parse_remote_version_file(self):
        return 'pass'

    def scrape_remote_version_to_disk(self):


    def main(self):
        self.scrape_remote_version_to_disk()


if __name__ == '__main__':
    ns = NeverSink()
    ns.main()
