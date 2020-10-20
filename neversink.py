from CONSTANTS import NEVERSINK_GITHUB_URL
from CONSTANTS import NEVERSINK_LOCAL_PATH
from neversink_spider_definition import NeverSinkSpider
from neversink_spider_definition import TwistedReactor


class NeverSink:

    def __init__(self):
        self.local_folder_location = NEVERSINK_LOCAL_PATH
        self.remote_web_location = NEVERSINK_GITHUB_URL
        self.local_version = self.get_local_version()
        self.remote_version = self.get_remote_version()

    def get_local_version(self):
        return 'todo'

    def get_remote_version(self):
        return 'todo'

    def parse_remote_version_file(self, dict_to_parse=dict()):
        print(dict_to_parse)
        return 'todo'

    def scrape_release_strings_to_disk(self):
        tr = TwistedReactor(spider_definition=NeverSinkSpider)
        filename_containing_releases_dict = tr.crawl()
        return filename_containing_releases_dict

    def main(self):
        filename = self.scrape_release_strings_to_disk()
        version = self.parse_remote_version_file(filename)


if __name__ == '__main__':
    ns = NeverSink()
    ns.main()
