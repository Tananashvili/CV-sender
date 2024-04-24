import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


def send_email(to_email, subject):
    email_address = "saba.tananashvili@gmail.com"
    email_password = ""  #INPUT EMAIL PASSWORD
    from_email = email_address
    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = to_email
    msg["Subject"] = subject

    file_path = "CV.pdf"  # Replace with the path to your file
    attachment = open(file_path, "rb").read()
    attachment_part = MIMEApplication(attachment, Name=file_path)
    attachment_part["Content-Disposition"] = f"attachment; filename={file_path}"
    msg.attach(attachment_part)

    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()

    server.login(email_address, email_password)

    server.sendmail(from_email, to_email, msg.as_string())

    server.quit()
