#!/usr/bin/python

import datetime
import logging
import urllib
import httplib
import smtplib
  
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def sendmail(textstring, headerstring):
    fromaddr = "dash@yourdomain.com"
    toaddr = "your@email.domain"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    df = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    msg['Subject'] = headerstring + " - " + df
    
    body = textstring
    msg.attach(MIMEText(body, 'plain'))
    
    server = smtplib.SMTP('smtp.yourdomain.com', 587)
    server.starttls()
    server.login(fromaddr, "your-password")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

def button_pressed_dash_oral():
    print "hello Bravo"
    sendmail("Bravo activated", "Dash Bravo")
    #urlopen("http://homematic/config/xmlapi/runprogram.cgi?program_id=bravo").read()

def button_pressed_dash_nivea():
    print "hello Mike"
    sendmail("Mike activated", "Dash Mike")
    #urlopen("http://homematic/config/xmlapi/runprogram.cgi?program_id=mike").read()

def button_pressed_dash_nerf():
    print "hello November"
    sendmail("Nerf activated", "Dash November")
    #urlopen("http://homematic/config/xmlapi/runprogram.cgi?program_id=november").read()    
 
def udp_filter(pkt):
    options = pkt[DHCP].options
    for option in options:
        if isinstance(option, tuple):
            if 'requested_addr' in option:
                mac_to_action[pkt.src]()
                break

# Add MAC address in lowercase!
mac_to_action = {'ac:63:be:90:79:45' : button_pressed_dash_oral, '11:11:11:11:11:11' : button_pressed_dash_nivea, '11:11:11:11:11:11' : button_pressed_dash_nerf} 

mac_id_list = list(mac_to_action.keys())
sniff(prn=udp_filter, store=0, filter="udp", lfilter=lambda d: d.src in mac_id_list)
  
if __name__ == "__main__":
 main()
