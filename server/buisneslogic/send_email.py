import smtplib

from server.settings import ALLOWED_HOSTS

def mail_sending(recipient, password):
    smtpobj = smtplib.SMTP_SSL("smtp.mail.ru", 465)
    # smtpobj.starttls()


    msg = f'''
    Hello!
    it is ur account on {ALLOWED_HOSTS[-1]} 
    LOGIN: {recipient}
    PASSWORD: {password}
    Go {ALLOWED_HOSTS[-1]}, click login
    '''

    
    smtpobj.login(sender, senders_pass)

    smtpobj.sendmail(sender, recipient, str(msg))

    smtpobj.quit()