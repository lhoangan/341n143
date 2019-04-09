import smtplib
import base64
import sys
import os

from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


def byemail(subject, body, image=None, text=None):

    user = 'lhoangan.exp@gmail.com'
    recipient = 'lhoangan@gmail.com'
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    #SUBJECT = subject
    #TEXT = body

    # Prepare actual message
    #message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    #""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = user
    msg['To'] = recipient
    msg.attach(MIMEText(body, 'plain'))


    if image is not None:
        img_data = open(image, 'rb').read()
        msg.attach(MIMEImage(img_data, name=os.path.basename(image)))
    if text is not None:
        attachment = MIMEText(open(text).read())
        attachment.add_header('Content-Disposition', 'attachment',
            filename=os.path.splitext(os.path.basename(image))[0]+'.txt')
        msg.attach(attachment)

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, d('s)d(g*eg&hg^j%sf$hg#j@ge!f', 'tIvHXJxgnJ9f'))
        server.sendmail(FROM, TO, msg.as_string())
        server.close()
        print 'Email sent'
    except:
        print "Failed to send email"

def d(key, string):
    decoded_chars = []
    string = base64.urlsafe_b64decode(string)
    for i in xrange(len(string)):
        key_c = key[i % len(key)]
        encoded_c = chr(abs(ord(string[i]) - ord(key_c) % 256))
        decoded_chars.append(encoded_c)
    decoded_string = "".join(decoded_chars)
    return decoded_string

if __name__=="__main__":
    if len(sys.argv) == 1:
        byemail("Running done", "Done")
    elif len(sys.argv) == 3:
        byemail(str(sys.argv[1]), str(sys.argv[2]))
    elif len(sys.argv) == 5 or len(sys.argv) == 7:
        img = None
        text = None
        data_type = sys.argv[3]
        if data_type.upper() == '--IMAGE':
            img = sys.argv[4]
        if data_type.upper() == '--TEXT':
            text = sys.argv[4]
        if len(sys.argv) == 7:
            data_type = sys.argv[5]
            if data_type.upper() == '--IMAGE':
                img = sys.argv[6]
            if data_type.upper() == '--TEXT':
                text = sys.argv[6]

        byemail(str(sys.argv[1]), str(sys.argv[2]), image=img, text=text)
