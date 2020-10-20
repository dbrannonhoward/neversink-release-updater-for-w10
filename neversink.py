import json
import re

from CONSTANTS import NEVERSINK_GITHUB_URL
from CONSTANTS import NEVERSINK_LOCAL_PATH
from CONSTANTS import REGEX_VERSION_PATTERN
from neversink_spider_definition import NeverSinkSpider
from neversink_spider_definition import TwistedReactor


class NeverSinkUpdater:

    def __init__(self):
        self.local_folder_location = NEVERSINK_LOCAL_PATH
        self.remote_web_location = NEVERSINK_GITHUB_URL
        self.local_version = self.get_local_version()
        self.remote_version = self.get_remote_version()

    @staticmethod
    def get_local_version():
        return 'todo'

    @staticmethod
    def get_remote_version():
        return 'todo'

    @staticmethod
    def json_to_dict(json_string):
        return json.loads(json_string)

    def open_file_contents(self, filename):
        with open(filename, 'r') as f:
            return self.json_to_dict(f.read())

    def parse_and_return_all_version_numbers(self, file_containing_dict=dict()):
        releases_list = list()
        for release in self.open_file_contents(file_containing_dict):
            releases_list.append(self.regex_filter_version(release))
        return releases_list

    @staticmethod
    def regex_filter_version(release_dict=dict):
        version_filter = re.compile(REGEX_VERSION_PATTERN)
        for key in release_dict.keys():
            test = version_filter.findall(str(release_dict[key]))[0]
        return test

    @staticmethod
    def scrape_release_strings_to_disk():
        tr = TwistedReactor(spider_definition=NeverSinkSpider)
        filename_containing_releases_dict = tr.crawl()
        return filename_containing_releases_dict

    def main(self):
        filename = self.scrape_release_strings_to_disk()
        version_list = self.parse_and_return_all_version_numbers(filename)
        print(version_list)


if __name__ == '__main__':
    ns = NeverSinkUpdater()
    ns.main()
