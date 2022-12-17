import time
import smtplib

def mail_sending(recipient, password):
    smtpobj = smtplib.SMTP_SSL('smtp.mail.ru', 465)
    # smtpobj.starttls()


    msg = f'''some test {password}'''


    
    smtpobj.login(sender, senders_pass)

    smtpobj.sendmail(sender, recipient, str(msg))

    smtpobj.quit()