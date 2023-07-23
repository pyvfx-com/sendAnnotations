import os
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage


def sendEmail(Annotation: str, Sender: str, Receiver: str):
    receiver = Receiver
    sender = Sender
    subject = f"[GPL] Annotation from {sender}"
    # subject = f"[{os.getenv('PL_SHOW').upper()}] Annotation from {sender}"
    body = "This is a test message with an image attachment."
    # read image file
    image_path = Annotation
    if not os.path.exists(image_path):
        print(f"Error: image file '{image_path}' not found.")
        return
    with open(image_path, 'rb') as f:
        img_data = f.read()
    image = MIMEImage(img_data)

    # create message
    msgRoot = MIMEMultipart()
    msgRoot['From'] = sender
    msgRoot['To'] = receiver
    msgRoot['Subject'] = subject
    msgRoot['Body'] = body
    msgRoot.attach(image)

    # Gmail SMTP server settings
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Login credentials (replace with your email and password/App Password)
    username = "htmldigger@gmail.com"
    password = "your app password"

    smtp = smtplib.SMTP(smtp_server, smtp_port)
    smtp.starttls()
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msgRoot.as_string())
    smtp.quit()
    time.sleep(2)
    print("\033[1;96m\n"
          "Annotation sent over the email successfully to : "
          "\033[00m\033[36m\033[3;5m(%s )\n\033[00m" % receiver)


if __name__ == '__main__':
    sendEmail(Annotation=img, Sender=send, Receiver=rec)
