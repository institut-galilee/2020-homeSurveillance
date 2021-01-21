# source https://github.com/e-tinkers

import RPi.GPIO as GPIO
import os
from time import sleep
from http.server import BaseHTTPRequestHandler, HTTPServer

host_name = "192.168.36.143"  # Change this to your Raspberry Pi IP address
host_port = 7000



class MyServer(BaseHTTPRequestHandler):
    """ A special implementation of BaseHTTPRequestHander for reading data from
        and control GPIO of a Raspberry Pi
    """

    def do_HEAD(self):
        """ do_HEAD() can be tested use curl command
            'curl -I http://server-ip-address:port'
        """
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def _redirect(self, path):
        self.send_response(303)
        self.send_header('Content-type', 'text/html')
        self.send_header('Location', path)
        self.end_headers()

    def do_GET(self):
        """ do_GET() can be tested using curl command
            'curl http://server-ip-address:port'
        """
        html = """
           <html>
           <body style="width:960px; margin: 20px auto;">
           <h1>Turn On/Off your alarm</h1>
           <form action="/" method="POST">
               Turn LED :
               <input style="color:red" type="submit" name="submit" value="On">
               <input style="color:blue"type="submit" name="submit" value="Off">
           </form>
           </body>
           </html>
        """
        temp = os.popen("/opt/vc/bin/vcgencmd measure_temp").read()
        self.do_HEAD()
        self.wfile.write(html.format(temp[5:]).encode("utf-8"))

    def do_POST(self):
        """ do_POST() can be tested using curl command
            'curl -d "submit=On" http://server-ip-address:port'
        """
        content_length = int(self.headers['Content-Length'])  # Get the size of data
        post_data = self.rfile.read(content_length).decode("utf-8")  # Get the data
        post_data = post_data.split("=")[1]  # Only keep the value

        # GPIO setup
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(18, GPIO.OUT)

        # Trigger the alarm 
        if post_data == "On":
            os.system("python3 buzzer.py")
        
        #KIll the process 'buzzer.py'
        else:
            for line in os.popen("ps ax | grep buzzer | grep -v grep"):  
                fields = line.split() 
                
                # extracting Process ID from the output 
                pid = fields[0]  
                
                # terminating process  
                os.kill(int(pid), signal.SIGKILL)  
        print("LED is {}".format(post_data))
        self._redirect('/')  # Redirect back to the root url


if __name__ == "__main__":
    http_server = HTTPServer((host_name, host_port), MyServer)
    print("Server Starts - %s:%s" % (host_name, host_port))

    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        http_server.server_close()