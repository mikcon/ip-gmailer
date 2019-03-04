# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 07:58:36 2019

@author: Michael Conway
"""

from email.mime.text import MIMEText
from urllib.request import urlopen
import json
import smtplib 
import config 

gmailUser = config.SETTINGS_CONFIG['gmailUser']
gmailPass = config.SETTINGS_CONFIG['gmailPass']
url = 'https://api.myip.com'
smtpServer = 'smtp.gmail.com'

def sendMail(body):
    msg = MIMEText(body)
    msg['From'] = config.SETTINGS_CONFIG['gmailUser']
    msg['To'] = config.SETTINGS_CONFIG['emailTo']   
    
    try:
        s = smtplib.SMTP_SSL(smtpServer)
        s.ehlo()
        s.login(gmailUser,gmailPass)
        s.send_message(msg)
        s.quit()
    except smtplib.SMTPResponseException as e:
        error_code = e.smtp_code
        error_message = e.smtp_error
        print(error_code + ':' + error_message)
        
        
jsonData = (urlopen(url)).read()

jsonParsed = json.loads(jsonData)

body = jsonParsed["ip"]

sendMail(body)