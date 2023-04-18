import smtplib


def send_email_of_site(from_email, to_email, messeg, password, smtp_host):
    smtpObj = smtplib.SMTP(smtp_host)
    smtpObj.starttls()
    smtpObj.login(from_email, password)
    smtpObj.sendmail(from_email, to_email, messeg)
    smtpObj.quit()
