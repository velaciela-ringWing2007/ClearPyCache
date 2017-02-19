import os

path = os.path.abspath(os.path.dirname(__file__))
print("Current directory : " + path)


def delete_pychache_dirs(current_path):
    """
    Delete __pychache__ directories.
    :param current_path:
    :return:
    """

    files = os.listdir(current_path)
    for item in files:
        path_name = current_path + '/' + item
        print('path:' + path_name, end=' => ')

        # Go to next when if file is no directory
        if os.path.isdir(path_name) == False:
            print('No directory')
            continue

        if item == '__pychache__':
            print('DELETE!!')
            os.rmdir(path_name)
        else:
            print('No pychache')
            delete_pychache_dirs(path_name)

delete_pychache_dirs(path)