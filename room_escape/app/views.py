from django.shortcuts import render, redirect
from app.models import student
from app.form import PostForm
from app import mailServer


# Create your views here.
def all_Info(request):
    students = student.objects.all().order_by('id')
    return render(request, 'all_info.html', locals())


def index(request):
    if request.method == "POST":
        if 'button' in request.POST:
            number = request.POST['cNumber']
            try:
                buff = student.objects.get(cNumber=number) 
                # buff.cStatus = "尚未進場" 
                # buff.save()
                return redirect('index')
            except:
                message = "查無此資料!"

        elif 'status_btn' in request.POST:
            status = request.POST.get('status')
            buff = student.objects.get(cNumber=status)

            if buff.cStatus == "尚未進場":
                buff.cStatus = "已進場"
                buff.save()
            elif buff.cStatus == "已進場":
                
                sendMethod = 'after'
                Mail = [buff.cMail]
                mailServer.Server(Mail, sendMethod)

                buff.cStatus = "已離場"
                buff.save()

    return render(request, "index.html", locals())


def new_data(request):
    
    if request.method == "POST":
        postform = PostForm(request.POST)
        if postform.is_valid():
            list_display = ('id', 'cNumber', 'cName', 'cMajor', 'cGrade', 'ctime', 'cMail', 'cStatus')
            cNumber = postform.cleaned_data['cNumber']
            cName = postform.cleaned_data['cName']
            cMajor = postform.cleaned_data['cMajor']
            cGrade = postform.cleaned_data['cGrade']
            ctime = postform.cleaned_data['ctime']
            cMail = postform.cleaned_data['cMail']
            cStatus = postform.cleaned_data['cStatus']
            print(cNumber,cName,cMajor,cGrade,ctime,cMail,cStatus)
            
            if student.objects.filter(cNumber = cNumber):
    
                message = '資料已存在...'
            else:
                unit = student.objects.create(cNumber=cNumber, cName=cName, cMajor=cMajor, cGrade=cGrade, ctime=ctime, cMail=cMail, cStatus=cStatus)
                unit.save()
                message = '以儲存...'
                postform = PostForm()
                # return redirect('all_Info')
    else:
        postform = PostForm()
        message = '姓名、學號、電話必須輸入'
    return render(request, "new.html", locals())


dataMail = []
def getMail(request):
    if request.method == "POST":
        sendMethod = 'before'
        mailServer.Server(dataMail, sendMethod)
        total =len(dataMail)
        endSend = '傳送完畢'
        # data = mailServer.Server()
    else:
        dataMail.clear()
        all_info = student.objects.all()
        for i in range(len(all_info)):
            allMail = all_info[i].cMail
            dataMail.append(allMail)
        print(dataMail)

    return render(request, 'mail.html', locals())


