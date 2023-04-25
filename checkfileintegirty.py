import hashlib
import smtplib
from email.message import EmailMessage



print("This is a simple python tool check the integrity of your file")
print("Please enter the path of the file ypu want to be checked in format (/etc/host/hostname)")
filePath = input("Enter file path (): ")
usrEmail = input("Enter your email: ")
usrPasswd = input("Enter your email password: ")
print("Make sure that two factor authentication is enabled")

def getHash(filePath):
    md5 =hashlib.md5()
    with open(filePath,'rb') as file:     #open file in binary read mode
        hash = file.read()

        md5.update(hash)

        return md5.hexdigest()

def sendEmail():
    message = EmailMessage()
    message.set_content(" ")
    message['subject'] = "IMPORTANT FILE DATA TAMPER DETECTED PLEASE CHECK"
    message['from'] = usrEmail
    message['to'] = usrEmail
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(usrEmail, usrPasswd)
    server.send_message(message)
    server.quit()

baseline = getHash(filePath)
print("[+] Just calculated your baseline")
print("[+] Checking")

#comparing the file has with the basline hash

while True:
    check = getHash(filePath)
    if check != baseline:
        print("[+] FILE TAMPER DETECTED !!!")
        baseline = check



