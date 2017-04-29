# -*- coding: utf-8 -*-
import smtplib
import sys

sys.path.append('..')
from config import MAIL_ACCOUNT, MAIL_PASSWORD

def compose_mail(address, link, keyword):
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(MAIL_ACCOUNT, MAIL_PASSWORD)

    msg = 'Subject: Nowa informacja na temat {key}\n' \
          'W poście {link} pojawiła się nowa informacja na temat {key}.'.format(key=keyword, link=link)

    smtpObj.sendmail(MAIL_ACCOUNT, address, msg)

    smtpObj.quit()
