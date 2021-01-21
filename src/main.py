import RPi.GPIO as GPIO
from time import sleep
import os 
from multiprocessing import Process
import smtplib
import imghdr
from email.message import EmailMessage

#lunch the buzzer script
def alarm():
    os.system("python3 buzzer.py")

# lunch the stream script 
def stream():
    os.system("python3 stream.py")



# Email settings 
sender = os.environ.get('EMAIL_USER')
password = os.environ.get('EMAIL_PASS')
message="SECURITY ALERT !! "

content="""\
<h2> Click <a style="color:blue" href="http://192.168.36.143:8000"> HERE</a>
to see the live stream 
<br>
<h2>Click <a style="color:blue" href="http://192.168.36.143:7000> HERE</a>
to turn ON/OFF your alarm </h2>

"""


msg=EmailMessage()
msg["Subject"]=message
msg["From"]=sender
msg["To"]=sender
msg.set_content(message)
msg.set_alternative(content,subtype="html")

images=["image1.jpg" , "image2.jpg"]
p1=Process(target=alarm)
p2=Process(target=stream)



GPIO.setmode(GPIO.BCM)
TRIG = 23 
ECHO = 24
WAIT_TIME=5

# whether an object is detected 
found=False

#whether the person has been identified 
#This variable simulate the finger print authentication 
access=False

print ("Distance Measurement In Progress")

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
try:
    while True:
        # if the person doesn't identify him self after 'WAIT_TIME' second we trigger the alarm and lunch the live stream 
        if(found and not access ):
        p1.start()
        p2.start()

        GPIO.output(TRIG, False)
        print ("Waiting For Sensor To Settle")
        time.sleep(2)

        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO)==0:
          pulse_start = time.time()

        while GPIO.input(ECHO)==1:
          pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150
        distance = round(distance, 2)

        # if a person is to close we wait for 'WAIT_TIME' seconds until he identify him self and we send an email containing a picture of the captured object and a link to the live stream 
        if(distance <= 10):
            found=True

            # add files to attachement 
            for file_name in files:
                with open(file_name ,"rb") as f: 
                    file_data=f.read()
                    file_type=imghdr.what(f.name)
                    file_name=f.name
                msg.add_attachment(file_data,maintype="image",subtype=file_type,filename=file_name)
            
            # send the email 
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login(sender,password)
                print("loged...")
                smtp.send_message(msg)
                print("sent")
            
            sleep(WAIT_TIME)

        print (f"Distance: {distance} cm\n")

except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    gpio.cleanup()