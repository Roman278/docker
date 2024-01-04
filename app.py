import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, message, to_email):
    # Set your email credentials
    sender_email = 'your_email@gmail.com'
    sender_password = 'your_email_password'

    # Create the email message
    email_message = MIMEMultipart()
    email_message['From'] = sender_email
    email_message['To'] = to_email
    email_message['Subject'] = subject

    # Attach the message to the email body
    email_message.attach(MIMEText(message, 'plain'))

    # Establish a connection to the SMTP server (in this case, Gmail's SMTP server)
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        # Start TLS for security
        server.starttls()

        # Login to your Gmail account
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, to_email, email_message.as_string())

    print("Email sent successfully!")

# Example usage
subject = "Notification: Your Task is Complete"
message = "Dear user, your task has been completed successfully."
to_email = "recipient@example.com"

send_email(subject, message, to_email)
