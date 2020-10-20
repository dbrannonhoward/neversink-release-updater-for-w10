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
        self.filename_containing_unparsed_release_strings = \
            self.scrape_release_strings_to_disk_and_return_filename()
        self.local_version = self.get_local_version()
        self.remote_version = self.get_remote_version()

    @staticmethod
    def get_local_version():
        return 'todo'

    @staticmethod
    def get_remote_version():
        return 'todo'

    @staticmethod
    def json_to_dict(json_string) -> list:
        json_as_list_of_dict = json.loads(json_string)
        return json_as_list_of_dict

    def open_file_contents(self, filename) -> list:
        with open(filename, 'r') as f:
            file_contents_as_dict = self.json_to_dict(f.read())
            return file_contents_as_dict

    # TODO(dbrannonhoward@gmail) main debug entry
    def parse_and_return_all_version_numbers(self, file_containing_dict=dict()) -> list:
        releases_list_as_list_of_strings = list()
        opened_file_contents = self.open_file_contents(file_containing_dict)
        for release in opened_file_contents:
            releases_list_as_list_of_strings.append(self.regex_filter_version(release))
        return releases_list_as_list_of_strings

    @staticmethod
    def regex_filter_version(release_dict=dict) -> str:
        version_filter = re.compile(REGEX_VERSION_PATTERN)
        for key in release_dict.keys():
            version_string = version_filter.findall(str(release_dict[key]))[0]
        if version_string:
            return version_string
        return 'Not found'

    @staticmethod
    def scrape_release_strings_to_disk_and_return_filename() -> str:
        tr = TwistedReactor(spider_definition=NeverSinkSpider)
        filename_containing_releases_dict = tr.crawl()
        return filename_containing_releases_dict

    def main(self):
        version_list = self.parse_and_return_all_version_numbers(
            self.filename_containing_unparsed_release_strings)
        print(version_list)


if __name__ == '__main__':
    ns = NeverSinkUpdater()
    ns.main()
