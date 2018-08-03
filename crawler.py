# -*- coding: utf-8 -*-

import time
import requests
import re
import os
import sys

def animation():

	x = 0

	while(x <= 1):

	    print("\n[*] Starting the web crawler... |")
	    time.sleep(0.1)
	    os.system('clear')
	    print("\n[ ] STarting the web crawler... /")
	    time.sleep(0.1)
	    os.system('clear')
	    print("\n[*] StArting the web crawler... -")
	    time.sleep(0.1)
	    os.system('clear')
	    print("\n[ ] StaRting the web crawler... |")
	    time.sleep(0.1)
	    os.system('clear')
	    print("\n[*] StarTing the web crawler... \\")
	    time.sleep(0.1)
	    os.system('clear')
	    print("\n[ ] StartIng the web crawler... |")
	    time.sleep(0.1)
	    os.system('clear')
	    print("\n[*] StartiNg The web crawler... /")
	    time.sleep(0.1)
	    os.system('clear')
	    print("\n[ ] Starting tHe web crawler... -")
	    time.sleep(0.1)
	    os.system('clear')
	    print("\n[*] Starting thE web crawler... |")
	    time.sleep(0.1)
	    os.system('clear')
	    print("\n[ ] Starting the Web crawler... \\")
	    time.sleep(0.1)
	    os.system('clear')
	    print("\n[*] Starting the wEb crawler... |")
	    time.sleep(0.1)
	    os.system('clear')
	    print("\n[ ] Starting the weB crawler... /")
	    time.sleep(0.1)
	    os.system('clear')
	    print("\n[*] Starting the web Crawler... -")
	    time.sleep(0.1)
	    os.system('clear')
	    print("\n[ ] Starting the web cRawler... |")
	    time.sleep(0.1)
	    os.system('clear')	
	    print("\n[*] Starting the web crAwler... \\")
	    time.sleep(0.1)
	    os.system('clear')
	    print("\n[ ] Starting the web craWler... |")
	    time.sleep(0.1)
	    os.system('clear')
	    print("\n[*] Starting the web crawLer... /")
	    time.sleep(0.1)
	    os.system('clear')
	    print("\n[ ] Starting the web crawlEr... -")
	    time.sleep(0.1)
	    os.system('clear')
	    print("\n[*] Starting the web crawleR... |")
	    time.sleep(0.1)
	    os.system('clear')
	    print("\n[ ] starting the web crawler... |")
	    time.sleep(0.1)
	    os.system('clear')
	    print("\n[*] starting the web crawler... \\")
	    time.sleep(0.1)
	    os.system('clear')
	    x = x + 1

def banner():
		print("""             ,----------------,              ,---------,""")
		print("""         ,-----------------------,          ,"        ,"|""")
		print("""       ,"                      ,"|        ,"        ,"  |""")
		print("""     +-----------------------+  |      ,"        ,"    |""")
		print("""     |  .-----------------.  |  |     +---------+      |""")
		print("""     |  |                 |  |  |     | -==----'|      |""")
		print("""     |  |  Web Crawler    |  |  |     |         |      |""")
		print("""     |  |  Created by:    |  |  |/----|`---=    |      |""")
		print("""     |  |                 |  |  |   ,/|==== ooo |      ;""")
		print("""     |  |  kr1pt0nG1rl    |  |  |  // |(((( [33]|    ,'""")
		print("""     |  `-----------------'  |," .;'| |((((     |  ,'""")
		print("""     +-----------------------+  ;;  | |         |,"+""")
		print("""        /_)______________(_/  //'   | +---------+""")
		print("""   ___________________________/___  `,""")
		print("""  /  oooooooooooooooo  .o.  oooo /,   \,"+"-----------""")
		print(""" / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,""")
		print("""/_==__==========__==_ooo__ooo=_/'   /___________,""")
		print("""`-----------------------------'""")

def animation2():

	x = 0

	while(x <= 1):

	    print("\n[*] Searching... |")
	    time.sleep(0.6)
	    os.system('clear')
	    print("\n[ ] Searching... /")
	    time.sleep(0.6)
	    os.system('clear')
	    print("\n[*] Searching... -")
	    time.sleep(0.6)
	    os.system('clear')
	    print("\n[ ] Searching... |")
	    time.sleep(0.6)
	    os.system('clear')
	    print("\n[*] Searching... \\")
	    time.sleep(0.6)
	    os.system('clear')
	    break

def capture_links(site):
	
	web_crawl = []
	web_crawl.append(site)

	header = {'user-agent': 'Mozila/5.0 (Windows NT 10.0; Win64; x64)' 'AppleWebKit/537.36 (KHTML,like Gecko)''Chrome/51.0.2704.103 Safari/537.36'}

	while True:
		url = web_crawl[0]

		req = requests.get(url, headers=header, timeout=5)
		
		html = req.text
		links = re.findall(r'<a href="?\'?(https?:\/\/[^"\'>]*)' ,html)
	          
		for link in links:
			if link not in web_crawl:
				web_crawl.append(link)
				print 'crawling:' ,link


		break
	req.close()
	print ('\nDone!!!\n')

	total = len(web_crawl)
	print "TOTAL OF LINKS: " + str(total)

def capture_emails(site):
	web_crawl = []
	web_crawl.append(site)

	header = {'user-agent': 'Mozila/11.0 (Windows NT 10.0; Win64; x64)' 'AppleWebKit/537.36 (KHTML,like Gecko)''Chrome/52.0.2704.103 Safari/537.36'}

	while True:
		url = site

		req = requests.get(url, headers=header, timeout=5)
		
		html = req.text
		emails = re.findall(r'(\w+@+\w+.+\w)' ,html)
		for email in emails:
			if email not in web_crawl:
				email = email.replace("</p><br><br","")

				web_crawl.append(email)
				print 'email:' ,email

		break
	req.close()
	print ('\nDone!!!')

	total = len(web_crawl)
	total = total - 1
	print "\nTOTAL OF E-MAILS: " + str(total)


banner()
print('\nkisses to Anh4x0r ٩(^ᴗ^)۶')
time.sleep(2.5)

animation()
try:

	site = sys.argv[1]
except:
	site = raw_input("Enter the URL to search: ")
try:
	option = sys.argv[2]
except:
	print("\nSelect your option...  ")
	time.sleep(1.5)
	print("#########################")
	print("[1] Print only links") 
	print("[2] Print only emails")
	print("[3] Print all")
	print("#########################")

	option = raw_input("\nType your option: ") 
	

animation2()


	
if option == '1':
	capture_links(site)
elif option == '2':
	capture_emails(site)
elif option == '3':
	print("\n\nExtrating the links:\n")
	capture_links(site)
	print("\n\nExtrating the E-mails: \n")
	capture_emails(site)
else:
	print("INVALID OPTION, TRY AGAIN")
