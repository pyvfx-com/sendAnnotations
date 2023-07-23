import os


def grab_screenshot():
    dir_path = os.path.expanduser("~/.cache/screenshot/")
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    else:
        pass
    os.system("gnome-screenshot -a -b --file={}/{}.jpg".format(dir_path, "annotation"))
    # os.system("screencapture -s {}/{}.jpg".format(dir_path, "annotation"))
    s_path = "{}{}.jpg".format(dir_path, "annotation")
    return s_path


if __name__ == '__main__':
    grab_screenshot()
