import os
import pywhatkit

print("Welcome to Python Laucher")

print("Enter 1 to launch Web Browser")
print("Enter 2 to launch Text Editor")
print("Enter 3 to launch Media Player")
print("Enter 4 to send a new message")
print("Enter 5 to join a web meeting")
print("Enter 0 to exit")
i=0
while i<=2:
	a=int(input("Enter Your Choice: "))
	if a==1:
		os.system("chrome")
		print("Web Browser had Started")	
	elif a==2:
		os.system("notepad")
		print("Web Browser had Started")	
	elif a==3:
		os.system("wmplayer")
		print("Web Browser had Started")
	elif a==4:
		q= input("Enter number with country code:")
		p=input("Enter message:")
		m=int(input("Enter hours:"))
		n=int(input("Enter min:"))
		pywhatkit.sendwhatmsg(q,p,m,n)
		print("Message sent\t"+p)
	elif a==5:
		os.system("chrome https://zoom.us/join")
		print("You meeting is launched ")
	elif a==0:
		exit()
	else:
		print("inavlid choice")