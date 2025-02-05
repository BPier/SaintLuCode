import time, os, subprocess
import logging


logging.basicConfig(filename='//server1/ServerData/_SaintLuCode/test/ip.log' ,level=logging.DEBUG,format='%(asctime)s - %(message)s')


for x in range(0,30):
    PublicIP = subprocess.check_output('curl ifconfig.me')
    logging.info(f"IPAddress: {str(PublicIP)}")
    pingTailscale = subprocess.check_output('ping 100.118.160.47.')
    logging.info(f"Tailscale Ping: {pingTailscale}")
    public ping
    time.sleep(1)
    x+=1