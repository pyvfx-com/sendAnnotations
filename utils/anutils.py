import os
import re
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


class mumbaiComp:
    """this is module for only Mumbai comp team, to add extra 2d VFX pipeline
        @example :
            mumbaiComp(
            username=os.getlogin(),
            nukepath=os.path.expanduser("~/.nuke/")
            )
        what will happen ?
            * if your username and .nuke username is match it will ask for grab screenshot.
            * screenshot will save inside your ~/.cache/screenshot/
    """

    def __init__(self, username: str, nukepath: str) -> None:
        self.username = username
        self.nukepath = nukepath
        self.validation_user_nuke()
        self.adding_pluginPath()
        if self.validation_user_nuke():
            self.grab_screenshot()
        else:
            pass

    def validation_user_nuke(self):
        x_user = self.username
        x_nkpath = self.nukepath
        nuke = "/home/{}/.nuke".format(x_user)
        if nuke == x_nkpath:
            return True
        else:
            return False

    def adding_pluginPath(self):
        inpath = "{}/init.py".format(self.nukepath)
        if self.validation_user_nuke():
            for _, _, files in os.walk(self.nukepath, topdown=True):
                for file in files:
                    if file == "init.py":
                        with open(inpath, 'r') as f:
                            file_contents = f.read()
                            if "nuke.pluginAddPath('/home/rion/tools/nuke')" not in file_contents:
                                with open(inpath, 'a') as f:
                                    f.write("nuke.pluginAddPath('/home/rion/tools/nuke')\n")
                    else:
                        pass
        else:
            print("Volla you are not identical.\nPlease ask %s to run this same script." % (
                self.uservalidate()))

    @staticmethod
    def uservalidate():
        # data = fDirectoryData()
        # usrs = data.getAllUsers()
        # for usr in usrs:
        #     if usr.getUsername() == self.nukepath.split("/")[-2]:
        return "Htmldigger"

    @staticmethod
    def grab_screenshot():
        string = (str(datetime.datetime.now()))
        regex_pattern = r"[^a-zA-Z0-9\s]+"
        clean_string = re.sub(regex_pattern, "", string).replace(" ", "_tmp_")
        dir_path = os.path.expanduser("~/.cache/screenshot/")
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        else:
            pass
        os.system("gnome-screenshot -a -b --file={}/{}.jpg".format(dir_path, clean_string))
        xpath = "%s/%s" % (dir_path, clean_string)
        return xpath

    @staticmethod
    def email_send():

        img = '/home/rion/.cache/screenshot/20230325_tmp_220133654661.jpg'
        rec = "ripanbiswas007@gmail.com"

        def sendEmail(annotation: str, receiver: str):
            receiver = receiver  # "anupam.biswas@framestore.com"
            sender = "anupam.biswas@framestore.com"
            subject = "Test Message"
            body = "This is a test message with an image attachment."

            # read image file
            image_path = annotation
            if not os.path.exists(image_path):
                print(f"Error: image file '{image_path}' not found.")
                return
            with open(image_path, 'rb') as f:
                img_data = f.read()
            image = MIMEImage(img_data, name=os.path.basename(image_path))

            # create message
            msgRoot = MIMEMultipart()
            msgRoot['From'] = receiver
            msgRoot['To'] = receiver
            msgRoot['Subject'] = subject
            msgRoot.attach(MIMEText(body))
            msgRoot.attach(image)

            smtp = smtplib.SMTP()
            smtp.connect('localhost')
            smtp.sendmail(sender, receiver, msgRoot.as_string())
            smtp.quit()
            print("Email sent successfully.")

    @staticmethod
    def file_delete(files: str):
        """Deletes files from a directory that were created more than one day ago.

        Args:
            files (str): The path to the directory containing the files.

        Returns:
            None.

        Raises:
            OSError: If the directory specified by `files` does not exist or is inaccessible.
        """
        dir_path = files
        now = datetime.datetime.now()
        threshold_time = now - datetime.timedelta(days=1)

        # Iterate over all the files in the directory
        for filename in os.listdir(dir_path):
            file_path = os.path.join(dir_path, filename)
            creation_time = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
            if creation_time < threshold_time:
                # Delete the file
                os.remove(file_path)


if __name__ == '__main__':
    mumbaiComp(username=os.getlogin(), nukepath="/home/rion/.nuke")
