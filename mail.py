# -*- coding: utf-8 -*-
import datetime
import smtplib
from email.header import Header
from email.mime.text import MIMEText

import yaml


class Email(object):
    def __init__(self, config):
        self.config = config
        self.localtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def send(self, subject, text):
        text += self.localtime
        msg = MIMEText(text, 'plain', 'utf-8')
        msg['Subject'] = Header(subject, 'utf-8')
        msg['from'] = self.config["email"]["from_addr"]
        msg['to'] = ', '.join(self.config["email"]["to_addr"])

        server = smtplib.SMTP(self.config["email"]["server"], self.config["email"]["port"])
        server.set_debuglevel(1)
        server.login(self.config["email"]["from_addr"], self.config["email"]["password"])
        server.sendmail(self.config["email"]["from_addr"], self.config["email"]["to_addr"], msg.as_string())
        server.quit()


if __name__ == "__main__":
    f = open("./config/config.yaml")
    config = yaml.safe_load(f)
    f.close()
    email = Email(config)
    email.send("this is test email")
