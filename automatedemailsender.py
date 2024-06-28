import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass


source_email = 'sender_email@gmail.com'

def send_email(source_email, sender_password, destination_email, mail_subject, body_content):
    try:
        # Setup the MIME
        msg = MIMEMultipart()
        msg['From'] = source_email
        msg['To'] = destination_email
        msg['Subject'] = mail_subject
        
        # Attach the body with the msg instance
        msg.attach(MIMEText(body_content, 'plain'))
        
        # Create SMTP session for sending the mail
        email_server = smtplib.SMTP('smtp.gmail.com', 587)  # Using Gmail's SMTP server with TLS
        email_server.starttls()  # Enable STARTTLS encryption
        
        # Login with email and password
        email_server.login(source_email, sender_password)
        
        # Convert the multipart msg into a string
        text = msg.as_string()
        
        # Send the email
        email_server.sendmail(source_email, destination_email, text)
        email_server.quit()
        print(f'Email sent to {source_email}')
    
    except smtplib.SMTPAuthenticationError:
        print("Failed to send email: Authentication error. Please check your email and password or use an app-specific password.")
    except Exception as e:
        print(f"Failed to send email: {e}")

destination_email = 'receiver_mail@gmail.com'
mail_subject = input("Enter the email subject: ")
body_content = input("Enter the email body: ")

send_email(source_email, sender_password, destination_email, mail_subject, body_content)
