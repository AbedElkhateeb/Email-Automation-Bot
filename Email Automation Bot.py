import smtplib
import time

sender = "your_email@gmail.com"
password = "your_app_password"

emails = ["test1@gmail.com", "test2@gmail.com"]

message = "Subject: Automation Bot\n\nHello! This is an automated message."

for email in emails:
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, email, message)
        server.quit()

        print("Sent to:", email)
        time.sleep(2)

    except Exception as e:
        print("Error:", e)