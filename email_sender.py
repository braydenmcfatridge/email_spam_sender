import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Brayden'
email['to'] = 'braydenmcfatridge@yahoo.com'
email['subject'] = 'YOU WIN A MILLION DOLLARS!'

email.set_content(html.substitute({'name': 'Darwin'}), 'html')

with smtplib.SMTP(host='smtp@gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('pythonbrayden@gmail.com', 'Pythoniscool6')
    smtp.send_message(email)
    print('howdy')