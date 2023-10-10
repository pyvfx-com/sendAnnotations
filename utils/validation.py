import platform
import os


class ScreenshotFolderCreator:
    def __init__(self):
        pass

    @staticmethod
    def get_os_name():
        system = platform.system()
        if system == "Windows":
            return "Windows"
        elif system == "Darwin":
            return "macOS"
        elif system == "Linux":
            return "Linux"
        else:
            return "Unknown"

    @staticmethod
    def create_screenshot_folder():
        os_name = ScreenshotFolderCreator.get_os_name()

        if os_name == "Windows":
            screenshot_folder = os.path.expanduser("~/.cache/screenshot/")
        else:
            screenshot_folder = os.path.expanduser("~/.cache/screenshot/")

        try:
            os.mkdir(screenshot_folder)
        except FileExistsError as fe:
            print(fe)

        return screenshot_folder


if __name__ == "__main__":
    screenshot_creator = ScreenshotFolderCreator()
    screenshot_folder = screenshot_creator.create_screenshot_folder()
    print("Screenshot folder path:", screenshot_folder)
