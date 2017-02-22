import os

path = os.path.abspath(os.path.dirname(__file__))
print("Current directory : " + path)


def delete_pycache_dirs(current_path):
    """
    Delete __pycache__ directories.
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

        if item == '__pycache__':
            print('DELETE!!')
            os.rmdir(path_name)
        else:
            print('No pycache')
            delete_pycache_dirs(path_name)

delete_pycache_dirs(path)
