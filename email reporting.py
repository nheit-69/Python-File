import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

def send_email():
    # Email account credentials
    from_email = "prem.ne8work767@gmail.com"
    password = "bayb xial vfbx tgfc"
    to_email = "minz.9prem.78@fmail.com"

    # Create message container
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = f"hello dear this our report  - {datetime.datetime.now().strftime('%Y-%m-%d')}"

    # Email body
    body = '''It was in 2014 that he last did a cartwheel on a cricket ground, and who is to say that
     had he been 100 per cent, the Chennai crowd could have very well been blessed with another one from
      the Pathaan of Bollywood.'''

    # Attach the body to the email
    msg.attach(MIMEText(body, 'plain'))

    # Set up the server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)

    # Send the email
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)

    # Quit the server
    server.quit()

if __name__ == "__main__":
    send_email()
