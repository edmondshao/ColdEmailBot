# Import smtplib for the actual sending function
import smtplib

# For guessing MIME type
import mimetypes

# Import the email modules we'll need
import email
import email.mime.application

smtp_server = 'smtp.gmail.com'
port = 587
set_server = "gmail"


emailWork =['es4418@nyu.edu',
'es4418@stern.nyu.edu',
'edmondshao7@gmail.com']
'''
emailWork = ['cope.ono@quovo.com',
'nicole.kozlowska@quovo.com',
'annie.buckel@quovo.com',
'oleh.dubno@quovo.com',
'justing.kern@quovo.com',
'yelena.reznikova@quovo.com',
'jake.barszcz@quovo.com',
'evan.dean@quovo.com',
'andera.c@quovo.com',
'kenny.ho@quovo.com',
'zhongkun.jin@quovo.com',
'john.whitfield@quovo.com',
'greg.thompson@quovo.com',
'andrew.king@quovo.com',
'zach.verkamp@quovo.com',
'hunter.betz@quovo.com',
'lauren.crossett@quovo.com',
'norman.shipman@quovo.com',
'lowell.putnam@quovo.com',
'lucas.guild@quovo.com',
'jake.davis@quovo.com',
'david.gowrie@quovo.com',
'len.karpf@quovo.com',
'robert.klotz@iextrading.com',
'james.cape@iextrading.com',
'eric.quinlan@iextrading.com',
'roamon.gonalez@iextrading.com',
'Lan.chou@iextrading.com',
'greg.zaharadis@iextrading.com',
'taylor.hakes@iextrading.com',
'larry.yu@iextrading.com',
'bryan.grohman@iextrading.com']
'''

for e in emailWork:
    print 'the email',e
    # Create a text/plain message
    msg = email.mime.Multipart.MIMEMultipart()
    msg['Subject'] = 'Ascend NYU: Invitation to Video Game Networking Event [10/20]'
    msg['From'] = 'edmondshao7@gmail.com'
    msg['To'] = e

    # The main body is just another attachment
    body = email.mime.Text.MIMEText("""Hi,

I hope this email finds you well. My name is Edmond and I am a e-board member of Ascend NYU. We are a student chapter of a national professional development organization, with over 60,000 members, focused on empowering leaders across many diverse industries. We are particularly interested in your experiences in the financial technology industry.  On Saturday, October 20th, from 1:30 pm to 3:30 pm, we will be hosting an informal networking event, Video Games with Fintech Professionals at the NYU LaGuardia Co-op in Manhattan. We would like to invite you to join us! Represent your firm, relax, and engage with a group of students passionate about fintech.

This session is intended to foster an intimate and relaxed environment where our students can have fun while connecting with you, the professionals, and ask any questions they may have regarding professional work-life, recruiting, and the industry at large.

Join us to unwind with a night full of food and fun! Get to know our dynamic student community and connect with other financial professionals from industry-leading firms. Refreshments will be provided.

Please let me know if you can make it! I have attached a one-pager with event details to this email for your reference. If you have any other questions, do not hesitate to text me at (847)420-8568 or es4418@stern.nyu.edu.

Have a wonderful day and I look forward to being in touch soon!

Best,
Edmond
""")
    msg.attach(body)

    # PDF attachment
    filename='OnePager.pdf'
    fp=open(filename,'rb')
    att = email.mime.application.MIMEApplication(fp.read(),_subtype="pdf")
    fp.close()
    att.add_header('Content-Disposition','attachment',filename=filename)
    msg.attach(att)

    # send via Gmail server
    # NOTE: my ISP, Centurylink, seems to be automatically rewriting
    # port 25 packets to be port 587 and it is trashing port 587 packets.
    # So, I use the default port 25, but I authenticate.
    s = smtplib.SMTP(smtp_server,port)
    s.ehlo()
    s.starttls()
    s.login('edmondshao7@gmail.com','ke4se6@bg')
    s.sendmail('edmondshao7@gmail.com',[e], msg.as_string())
    s.quit()
    print 'Done'
