yieldimport qrcode
from datetime import datetime
import pywhatkit as kit
import os
import time

# Student info
student_name = "Bharani"
now = datetime.now()
date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")

# QR Data
qr_data = f"Name: {student_name}\nDate & Time: {date_time_str}"

# Generate QR
qr = qrcode.make(qr_data)
file_path = "student_qr.png"
qr.save(file_path)

print("QR code saved!")

# WhatsApp number (include country code, e.g., +91 for India)
phone_number = "+919344243297"  # replace with actual phone number

# Wait 20 seconds and send the image via WhatsApp Web
print("Opening WhatsApp Web...")
kit.sendwhats_image(phone_number, file_path, f"Attendance QR for {student_name}", 20)
print("Image scheduled to send. Make sure WhatsApp Web is open.")

