# Call the function send_email(to, subject, body) using keyword arguments in any order. 
def send_email(to, subject, body):
    print(f"Sending email to: {to}")
    print(f"Subject: {subject}")
    print(f"Body: {body}")
send_email(to= 'nikhil', subject= 'for testing', body= 'this is a text email')