'''
Application 3 - Website Blocker

Blocks access to websites listed in website_list by adding them to /etc/hosts file
Access only blocked during specified "working hours" (10 am - 6 pm)

Possible future work: accept user input to add/remove websites from blocked list, 
					  and/or change timeframe of working hours
'''
import time
from datetime import datetime as dt

hosts_path = "/etc/hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "www.youtube.com", "www.amazon.ca"]

while True:
	if dt(dt.now().year, dt.now().month, dt.now().day, 10) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 18):
		print("Working hours...")
		with open(hosts_path, 'r+') as file:
			content = file.read()
			for website in website_list:
				if website not in content:
					file.write(redirect + " " + website + "\n")
	else:
		print("Fun hours...")
		with open(hosts_path, 'r+') as file:
			content = file.readlines()
			file.seek(0)
			for line in content:
				if not any(website in line for website in website_list):
					file.write(line)
			file.truncate()
					
	time.sleep(5)