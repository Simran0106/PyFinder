#!/usr/bin/python3



print("context-type: text/html")
print()
import os
import cgi
form=cgi.FieldStorage
a=int(getvalue.form("x"))


    
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
