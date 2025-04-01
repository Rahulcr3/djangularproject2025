from django.shortcuts import render,HttpResponse,redirect

from .models import User,Student,Teacher
# Create your views here.

def home(request):
    return render(request,"home.html")

def student_register(request):
    if request.method=="POST":
            FIRSTNAME=request.POST['FIRSTNAME']
            LASTNAME=request.POST['LASTNAME']
            EMAIL=request.POST['EMAIL']
            ADDRESS=request.POST['ADDRESS']
            PHONE_NUMBER=request.POST['PHONE_NUMBER']
            GUARDIAN=request. POST['GUARDIAN']
            USERNAME=request.POST['USERNAME']
            PASSWORD=request.POST['PASSWORD']
            new_user=User.objects.create_user(first_name=FIRSTNAME, last_name=LASTNAME, email=EMAIL, username=USERNAME,password=PASSWORD,usertype='student',is_active=False)
            new_user.save()
            x=Student.objects.create(student_id=new_user, guardian=GUARDIAN, address=ADDRESS, phone_number=PHONE_NUMBER)
            x.save()
            
            return HttpResponse("success")
    else:
        return render(request,'student_register.html')
    
from django.contrib.auth import authenticate,logout,login

def logins(request):
    if request.method=="POST":
        USERNAME=request.POST['USERNAME']
        PASSWORD=request.POST['PASSWORD']
        userpass=authenticate(request, username=USERNAME, password=PASSWORD)
        if userpass is not None and userpass.is_superuser==1:
            return redirect('adminhome')
        elif userpass is not None and userpass.is_staff==1:
            login(request, userpass)
            request.session['teacher_id']=userpass.id
            return redirect('teacherhome')
        elif userpass is not None and userpass.is_active==1:
            login(request, userpass)
            request.session['student_id']=userpass.id
            return redirect('studenthome')
        else:
            return HttpResponse("invalid login")
    else:
        return render(request,'logins.html')
    
def adminhome(request):
    return render(request,"adminhome.html")

def teacher_reg(request):
    if request.method=="POST":
            FIRSTNAME=request.POST['FIRSTNAME']
            LASTNAME=request.POST['LASTNAME']
            EMAIL=request.POST['EMAIL']
            ADDRESS=request.POST['ADDRESS']
            PHONE_NUMBER=request.POST['PHONE_NUMBER']
            USERNAME=request.POST['USERNAME']
            PASSWORD=request.POST['PASSWORD']
            SALARY=request.POST['SALARY']
            EXPERIENCE=request.POST['EXPERIENCE']
            new_user=User.objects.create_user(first_name=FIRSTNAME, last_name=LASTNAME, email=EMAIL, username=USERNAME,password=PASSWORD,usertype='teacher',is_staff=True)
            new_user.save()
            x=Teacher.objects.create(teacher_id=new_user,address=ADDRESS, phone_no=PHONE_NUMBER,salary=SALARY,experience=EXPERIENCE)
            x.save()
            return HttpResponse("success")
    else:
        return render(request,'teacher_reg.html')
    
def studentview(request):
        x=Student.objects.all()
        return render(request,"studentview.html",{"view":x})

def studentdelete(request,id):
    x=Student.objects.get(id=id)
    y=User.objects.get(id=x.student_id_id)
    x.delete()
    y.delete()
    return redirect("studentview") 

def studentapprove(request,id):
    x=Student.objects.get(student_id=id)
    user=x.student_id
    user.is_active=True
    user.save()
    return redirect("studentview")

def studenthome(request):
    return render(request,"studenthome.html")

def studentedit(request):
    x=request.session['student_id']
    y=Student.objects.get(student_id=x)
    return render(request,"studentedit.html",{"sedit":y})

def studentupdate(request,id):
    if request.method=='POST':
        fname=request.POST['FIRSTNAME']
        lname=request.POST['LASTNAME']
        newem=request.POST['EMAIL']
        newaddr=request.POST['ADDRESS']
        ph=request.POST['PHONE_NUMBER']
        g=request. POST['GUARDIAN']
        x=Student.objects.get(id=id)
        x.FIRSTNAME=fname
        x.LASTNAME=lname
        x.EMAIL=newem
        x.ADDRESS=newaddr
        x.PHONE_NUMBER=ph
        x.GUARDIAN=g
        x.save()
        y=User.objects.get(id=x.student_id_id)
        y.first_name=fname
        y.last_name=lname
        y.email=newem
        y.save()
        z=Student.objects.get(id=id)
        z.address=newaddr
        z.phone_number=ph
        z.guardian=g
        z.save()
        return redirect("studenthome")
    
    else:
        x=Student()
        return render(request,"studentedit.html",{"sedit":x})
    
def studentdata(request):
    x = request.session['student_id']
    y=Student.objects.get(student_id=x)
    return render(request,"studentdata.html",{"data":y})

def teacherview(request):
     x=Teacher.objects.all()
     return render(request,"teacherview.html",{"tview":x})

def teacherdelete(request,id):
        x=Teacher.objects.get(id=id)
        x.delete()
        return HttpResponse("deleted")

def teacherhome(request):
     return render(request,"teacherhome.html")

def teacheredit(request):
    x=request.session['teacher_id']
    y=Teacher.objects.get(teacher_id=x)
    return render(request,"teacheredit.html",{"tedit":y})  
     
def teacherupdate(request,id):
    if request.method=='POST':
        fn=request.POST['FIRSTNAME']
        ln=request.POST['LASTNAME']
        em=request.POST['EMAIL']
        addr=request.POST['ADDRESS']
        phn=request.POST['PHONE_NUMBER']
        sal=request.POST['SALARY']
        exp=request.POST['EXPERIENCE']
        t=Teacher.objects.get(id=id)
        t.FIRSTNAME=fn
        t.LASTNAME=ln
        t.EMAIL=em
        t.ADDRESS=addr
        t.PHONE_NUMBER=phn
        t.SALARY=sal
        t.EXPERIENCE=exp
        t.save()
        u=User.objects.get(id=t.teacher_id_id)
        u.first_name=fn
        u.last_name=ln
        u.email=em
        u.save()
        c=Teacher.objects.get(id=id)
        c.address=addr
        c.phone_no=phn
        c.salary=sal
        c.experience=exp
        c.save()
        return redirect("teacherhome")
    
    else:
        a=Teacher()
        return render(request,"teacheredit.html",{"tedit":a})


def logouts(request):
    if "student_id" in request.session:
        del request.session["student_id"]
    else:
        if "teacher_id" in request.session:
            del request.session['teacher_id']
    logout(request)
    return redirect("logins")

def index(request):
     return render(request,'index.html')

