from distutils.log import error
import smtplib
from email.mime.text import MIMEText


#------!!!! https://myaccount.google.com/ !!!!-----安全性修改#
def Server(addr, sendMethod):
    #發送所有email
    print('總人數:'+ str(len(addr)))
    
    for i in range(len(addr)):
        print("---------" + str(i+1) + "----------")     
        print("mailServer.py :" + addr[i]) 
        from_addr = 'wei4gaming@gmail.com' #發送帳號
        pwd = "vphuiqxwvuxsruuy" #發送帳號的密碼
        to_addr_list = addr[i] #設定收件人 [account1, account2,.....]

        msgInfoBefore = '密室逃脫：屍身'+ '\n' + '⚠️活動注意事項⚠️' + '\n' + '1、請全程配戴口罩' + '\n' + '2、請出示健康聲明憑證' + '\n' + '3、請由I棟電梯方向進場（關卡方向：I307➡️I308➡️I309' + '\n' + '4、進場後請勿觸碰非關卡道具佈景及工作人員' + '\n' + '5、逃脫過程請勿破壞關卡道具'  + '\n' + '6、不可攜帶通訊工具（ex:手機、耳機）進場' + '\n' + '7、場內禁止飲食' + '\n' + '8、不可向未進行遊戲之參加人員洩露遊戲內容及關卡' + '\n' + '9、全程禁止錄影、錄音' + '\n' + '10、禁止攜帶危險物品（ex:美工刀、剪刀、打火機)' + '\n' + '11、請穿著方便活動的衣物及鞋子（包鞋）'+ '\n' +''+ '\n' +'⭐️請提前10分鐘報到⭐️'+ '\n' +'以上煩請詳閱、配合敬祝闖關順利'+ '\n' +'資工X保健X健管'
        msgInfoAfter = '密室逃脫：屍身'+ '\n'+ '感謝您參與這次活動' + '\n' + '謝謝您對我們系會的支持' + '\n' + '您珍貴的回饋是我們進步的來源' + '\n' + ''

        # 判斷要寄哪類別訊息
        if sendMethod == 'before' :
            msgInfo = msgInfoBefore
        elif sendMethod == 'after':
            msgInfo = msgInfoAfter
        else:
            msgInfo = "unknow"

               
        msg = MIMEText(msgInfo, 'plain', 'utf-8')
        msg['Subject'] = '資工、保健、健管 系學會'
        msg['From'] = '密室逃脫-屍身'
        msg['To'] = addr[i] # 寄送信箱
        msg['Cc'] = addr[i] # for 迴圈學生email

        # print(type(msg))

        #-------------以下誤改-----------#
        try:
            mySMTP = smtplib.SMTP('smtp.gmail.com', 587)
            mySMTP.ehlo()
            mySMTP.starttls()
            mySMTP.login(from_addr, pwd)
            status = mySMTP.sendmail(from_addr, to_addr_list, msg.as_string())
            print("mail.py :" + "發送郵件成功")
            mySMTP.quit() #結束連線
            
        except smtplib.SMTPException:
            print(error)
            print("發送郵件失敗")
