import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = '<your email address>'
email['to'] = '<to email address>'
email['subject'] = '<subject>'
email['message'] = '<message>'

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('<your email address>', '<your password>')
  smtp.send_message(email)
  print('all good boss!')
