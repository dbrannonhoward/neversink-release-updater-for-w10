
def main():
    # initialization
    paths_managed = get_path_list()
    # get neversink details
    neversink_local_contents = get_neversink_directory_contents()
    neversink_local_version = get_neversink_version(neversink_local_contents)
    # check neversink github version
    neversink_github_url = get_neversink_url()
    neversink_html_contents = get_site_html(neversink_github_url)
    neversink_remote_version = get_neversink_release_info(neversink_html_contents)
    # compare current release to local version
    # TODO what data to compare?
    neversink_download = get_neversink_release()
    move_neversink_download()
    extract_neversink_download()


def get_neversink_directory_contents():
    return 'pass'


def get_neversink_version(folder_contents):
    neversink_zip_files = filter_zip_files(folder_contents)
    move_old_neversink_zip_files_to_trash(neversink_zip_files)
    neversink_zip_version = extract_version_from_filename(neversink_zip_files)


def get_path_list():
    return 'pass'


if __name__ == '__main__':
    main()
