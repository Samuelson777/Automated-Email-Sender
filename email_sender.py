import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = "your_email@example.com"  # Replace with your email
sender_password = "your_password"          # Replace with your email password
recipient_email = "recipient@example.com"  # Replace with recipient's email
subject = "Automated Email"
body = "This is an automated email sent from a Python script."

# Create the email
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

# Send the email
try:
    with smtplib.SMTP('smtp.gmail.com', 587) as server:  # For Gmail
        server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
        server.login(sender_email, sender_password)
        server.send_message(msg)
        print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")