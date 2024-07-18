import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from socket import gaierror

def send_email():
    sender_email = "ak9072918@gmail.com"
    receiver_email = "akashkumaraaa12@gmail.com"
    password = "apza zocl ptxz qfqs"
    subject = "Reminder: Drink Water!"
    body = "Pani pee le bhai, creatine le raha hai tu"
    
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    
    message.attach(MIMEText(body, 'plain'))
    
    try:
        # Create SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        # Login to SMTP server
        s.login(sender_email, password)
        
        # Send email
        s.sendmail(sender_email, receiver_email, message.as_string())
        
        print("Email sent successfully!")
    except (gaierror, ConnectionRefusedError):
        print("Failed to connect to the SMTP server. Check your network connection and try again.")
    except smtplib.SMTPAuthenticationError:
        print("SMTP authentication error. Check your username and password.")
    except smtplib.SMTPException as e:
        print(f"SMTP error occurred: {e}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
    finally:
        # Terminate SMTP session
        if 's' in locals():
            s.quit()

# Call the function to send the email
send_email()
