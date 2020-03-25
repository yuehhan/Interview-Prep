import requests
import smtplib
from linode_api4 import LinodeClient, Instance

EMAIL_USER = os.environ.get('EMAIL_USER')
EMAIL_PASS = os.environ.get('EMAIL_PASS')
LINODE_TOKEN = os.environ.get('LINODE_TOKEN')



def notify_user():
    with smtpli.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login()

        subject = 'The site is down!'
        body = 'Make sure the server restarted and it is back up'
        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(EMAIL_USER, EMAIL_USER, msg)

def reboot_server():
    client = LinodeClient(LINODE_TOKEN)
    my_server = client.load(Instance,#this should be a number from server)
    my_server.reboot()

try:
    r = requests.get('https://yuehh.com', timeout=5)

    if r.status_code != 200:
        notify_user()
        reboot_server()

except Exception as e:
    notify_user()
    reboot_server()

#check if response is a 200 response
#https://docs.python.org/3/library/smtplib.html
