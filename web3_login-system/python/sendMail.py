import smtplib
import random


def mail(addr, Num):
    print("sendMail.py :" + addr)
    from_addr = 'wei4gaming@gmail.com'
    to_addr_list = [addr]
    
    # print("驗證碼 :{} ".format(Num))

    msg = "Subject:Verification code" +'\n'+ str(Num)
    mySMTP = smtplib.SMTP('smtp.gmail.com', 587)
    mySMTP.ehlo()
    mySMTP.starttls()
    mySMTP.login(from_addr, 'vphuiqxwvuxsruuy')
    status = mySMTP.sendmail(from_addr, to_addr_list, msg)

    if status == {}:
        print("mail.py :" + "發送郵件成功")
    mySMTP.quit()
    #weihe7813@gmail.com