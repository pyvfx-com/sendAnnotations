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
            # Create a 'screenshot' folder in the current working directory
            folder = os.path.expanduser("~/.cache/screenshot/")
        else:
            # Create a 'screenshot' folder in the current working directory
            folder = os.path.expanduser("~/.cache/screenshot/")

        try:
            os.mkdir(folder)
        except FileExistsError:
            pass
        return folder


if __name__ == "__main__":
    screenshot_creator = ScreenshotFolderCreator()
    screenshot_folder = screenshot_creator.create_screenshot_folder()
    print("Screenshot folder path:", screenshot_folder)
