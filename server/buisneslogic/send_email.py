import time
import smtplib

def mail_sending(recipient, password):
    smtpobj = smtplib.SMTP_SSL('smtp.mail.ru', 465)
    # smtpobj.starttls()


    msg = f'''some test {password}'''

    sender = 'alexander.kizimenko@mail.ru'
    senders_pass = 'hBT7zrGwTi4pFdz8cARH'
    
    smtpobj.login(sender, senders_pass)

    smtpobj.sendmail(sender, recipient, str(msg))

    smtpobj.quit()