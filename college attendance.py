'''
import csv          #csv is to extract data from excel sheet        (note that excel sheet is saved in form of .csv format) csv file stores values separated by commas
import smtplib      #smtplib is library to send the email

fh=open("testhack.csv",newline="")

reader=csv.reader(fh)

header=next(reader) # header contains the top line of the excel file i.e the line which contains RollNo,Name,Mly,Cum Email

data=[row for row in reader]    # data is the list of all the information in excel file

rolla=[]    #for 60-75 defaulters
mthlya=[]
namea=[]
cuma=[]
emaila=[]
rollb=[]    #for 50-60 defaulters
nameb=[]
mthlyb=[]
cumb=[]
emailb=[]
rollc=[]    #for <50 defaulters
namec=[]
mthlyc=[]
cumc=[]
emailc=[]

for row in data:    #to put students in different categories
    if(row[2]!="" and int(row[2])>=60 and int(row[2])<75):
        rolla.append(row[0])
        namea.append(row[1])
        mthlya.append(row[2])
        cuma.append(row[3])
        emaila.append(row[4])
    elif(row[2]!="" and int(row[2])>=50 and int(row[2])<60):
        rollb.append(row[0])
        nameb.append(row[1])
        mthlyb.append(row[2])
        cumb.append(row[3])
        emailb.append(row[4])
    elif(row[2]!="" and int(row[2])<50):
        rollc.append(row[0])
        namec.append(row[1])
        mthlyc.append(row[2])
        cumc.append(row[3])
        emailc.append(row[4])
        
print("Roll.No\t\tName\t\tMonthly Attn\t\tCumulative Attn\t\tEmail id\n")

print("\n\nCategory 1\n\n") #category 1 is from 60-75

for i in range(0,len(rolla)):
    print(rolla[i],"\t\t",namea[i],"\t\t",mthlya[i],"\t\t",cuma[i],"\t\t",emaila[i])
print("************************************************************")


print("\n\nCategory 2\n\n") #category 2 is from 50-60


for i in range(0,len(rollb)):
    print(rollb[i],"\t",nameb[i],"\t",mthlyb[i],"\t",cumb[i],"\t",emailb[i])
print("************************************************************")


print("\n\nCategory 3\n\n") #category 3 is <50


for i in range(0,len(rollc)):
    print(rollc[i],"\t",namec[i],"\t",mthlyc[i],"\t",cumc[i],"\t",emailc[i])
print("************************************************************")


def send_email(user, pwd, recipient, subject, body,cnt):    #function to send the mail.
    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body
    try:
        # Prepare actual message
        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (FROM, TO, SUBJECT, TEXT)
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print ('successfully sent the mail')
    except:
        if(cnt<=3):
            cnt+=1
            send_email(user,pwd,recipient,subject,body,cnt)
        else:
            print ("failed to send mail to "+message)

semail=""  #Put your email id here   senders email should be in gmail
spwd="" #Put your password here

sub="Attendance defaulter"  #subject of the email


cnt=1   #counter to try sending email 3 times in case sending email fails

for i in range(0,len(rolla)):
    recp=emaila[i]
    message="This is to inform you that "+namea[i]+" has come defaulter for this month in Category 1.\nAttendance for this month is "+mthlya[i]+"\nCumulative attendance till this month is "+cuma[i]+"."
    send_email(semail,spwd,recp,sub,message,cnt)

for i in range(0,len(rollb)):
    recp=emailb[i]
    message="This is to inform you that "+nameb[i]+" has come defaulter for this month in Category 2.\nAttendance for this month is "+mthlyb[i]+"\nCumulative attendance till this month is "+cumb[i]+"."
    send_email(semail,spwd,recp,sub,message,cnt)

for i in range(0,len(rollc)):
    recp=emailc[i]
    message="This is to inform you that "+namec[i]+" has come defaulter for this month in Category 3.\nAttendance for this month is "+mthlyc[i]+"\nCumulative attendance till this month is "+cumc[i]+"."
    send_email(semail,spwd,recp,sub,message,cnt)















'''











import csv          #csv is to extract data from excel sheet        (note that excel sheet is saved in form of .csv format) csv file stores values separated by commas
import smtplib      #smtplib is library to send the email

import time
start = time.time()

fh=open("testhack.csv",newline="")

reader=csv.reader(fh)

header=next(reader) # header contains the top line of the excel file i.e the line which contains RollNo,Name,Mly,Cum Email

data=[row for row in reader]    # data is the list of all the information in excel file

rolla=[]    #for 60-75 defaulters
mthlya=[]
namea=[]
cuma=[]
emaila=[]
rollb=[]    #for 50-60 defaulters
nameb=[]
mthlyb=[]
cumb=[]
emailb=[]
rollc=[]    #for <50 defaulters
namec=[]
mthlyc=[]
cumc=[]
emailc=[]

for row in data:    #to put students in different categories
    if(row[2]!="" and int(row[2])>=60 and int(row[2])<75):
        rolla.append(row[0])
        namea.append(row[1])
        mthlya.append(row[2])
        cuma.append(row[3])
        emaila.append(row[4])
    elif(row[2]!="" and int(row[2])>=50 and int(row[2])<60):
        rollb.append(row[0])
        nameb.append(row[1])
        mthlyb.append(row[2])
        cumb.append(row[3])
        emailb.append(row[4])
    elif(row[2]!="" and int(row[2])<50):
        rollc.append(row[0])
        namec.append(row[1])
        mthlyc.append(row[2])
        cumc.append(row[3])
        emailc.append(row[4])
        
print("Roll.No\t\tName\t\tMonthly Attn\t\tCumulative Attn\t\tEmail id\n")

print("\n\nCategory 1\n\n") #category 1 is from 60-75

for i in range(0,len(rolla)):
    print(rolla[i],"\t\t",namea[i],"\t\t",mthlya[i],"\t\t",cuma[i],"\t\t",emaila[i])
print("************************************************************")


print("\n\nCategory 2\n\n") #category 2 is from 50-60


for i in range(0,len(rollb)):
    print(rollb[i],"\t",nameb[i],"\t",mthlyb[i],"\t",cumb[i],"\t",emailb[i])
print("************************************************************")


print("\n\nCategory 3\n\n") #category 3 is <50


for i in range(0,len(rollc)):
    print(rollc[i],"\t",namec[i],"\t",mthlyc[i],"\t",cumc[i],"\t",emailc[i])
print("************************************************************")


def send_email(user, pwd, recipient, subject, body,cnt):    #function to send the mail.
    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body
    try:
        # Prepare actual message
        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (FROM, TO, SUBJECT, TEXT)
        server.sendmail(FROM, TO, message)
        print ('successfully sent the mail')
    except:
        if(cnt<=3):
            cnt+=1
            send_email(user,pwd,recipient,subject,body,cnt)
        else:
            print ("failed to send mail to "+message)

semail=""  #Put your email id here   senders email should be in gmail
spwd="" #Put your password here

sub="Attendance defaulter"  #subject of the email


cnt=1   #counter to try sending email 3 times in case sending email fails


server = smtplib.SMTP("smtp.gmail.com", 587)    #server opens once
server.ehlo()
server.starttls()
server.login(semail, spwd)
  
for i in range(0,len(rolla)):
    recp=emaila[i]
    message="This is to inform you that "+namea[i]+" has come defaulter for this month in Category 1.\nAttendance for this month is "+mthlya[i]+"\nCumulative attendance till this month is "+cuma[i]+"."
    send_email(semail,spwd,recp,sub,message,cnt)

for i in range(0,len(rollb)):
    recp=emailb[i]
    message="This is to inform you that "+nameb[i]+" has come defaulter for this month in Category 2.\nAttendance for this month is "+mthlyb[i]+"\nCumulative attendance till this month is "+cumb[i]+"."
    send_email(semail,spwd,recp,sub,message,cnt)

for i in range(0,len(rollc)):
    recp=emailc[i]
    message="This is to inform you that "+namec[i]+" has come defaulter for this month in Category 3.\nAttendance for this month is "+mthlyc[i]+"\nCumulative attendance till this month is "+cumc[i]+"."
    send_email(semail,spwd,recp,sub,message,cnt)

server.close() #server closes once

print('It took', time.time()-start, 'seconds.')




