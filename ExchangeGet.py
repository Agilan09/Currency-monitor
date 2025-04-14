import requests
import smtplib
from email.mime.text import MIMEText
import time

THRESHOLD = 4.90
EMAIL_SENDER = "agirajah14@gmail.com"
EMAIL_PASSWORD = "bras klzj tfyg ozpt"
EMAIL_RECIPIENT = "agirajah14@gmail.com"

def get_exchange_rate():
    try:
        response = requests.get("https://api.frankfurter.app/latest?from=EUR&to=MYR")
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        data = response.json()
        return data["rates"]["MYR"]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching exchange rate: {e}")
        return None
    
def send_email(rate):
    msg = MIMEText(f"EUR/MYR exchange rate is {rate}, which is above the threshold of {THRESHOLD}.")
    msg["Subject"] = "EUR/MYR Exchange Rate Alert"
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECIPIENT

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")
  
  
start_time = None  
    
while True:
    rate = get_exchange_rate()
    print(rate)
    
    
    """  if rate > 4.9:
        if start_time is None:
            start_time = time.time()
        elif time.time() - start_time >= 10:
            print("Value remained")
            break
    else:
        start_time = None """
        
    if rate is not None and rate >= THRESHOLD:
     print(rate)
     send_email(rate)  
    time.sleep(3600)
     
