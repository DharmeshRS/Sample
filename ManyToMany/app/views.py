from django.shortcuts import render,redirect
from app.models import SubjectModel,StudentModel
from django.contrib import messages
# Create your views here.
def homepage(request):
    return render(request,"homepage.html")


def addsub(request):
    return render(request,"addsub.html")


def savesub(request):
    cid=request.POST["cid"]
    subject=request.POST["subject"]
    SubjectModel(classid=cid,subject=subject).save()
    messages.success(request,"Subject is Saved")
    return redirect('addsub')


def displaysub(request):
    return render(request,"displaysub.html",{"data":SubjectModel.objects.all()})


def addstudent(request):
    return render(request,"addstudent.html",{"data":SubjectModel.objects.all()})

def savestudent(request):
    sid=request.POST["sid"]
    sname=request.POST["sname"]
    contact=request.POST["contact"]
    subject=request.POST.getlist("subject")
    st=StudentModel(studentid=sid,name=sname,contact=contact)
    st.save()
    st.subject.set(subject)

    return redirect('addstudent')


def displaystudent(request):
    return render(request,"displaystudeny.html",{"data":StudentModel.objects.all()})


def deletestudent(request):
    stno=request.GET.get("stno")
    StudentModel.objects.filter(studentid=stno).delete()
    messages.success(request,"Data Is Deleted")
    return render(request,"displaystudeny.html",{"data":StudentModel.objects.all()})


def deletesub(request):
    subjno = request.GET.get("subj")
    SubjectModel.objects.filter(classid=subjno).delete()
    messages.success(request, "Data Is Deleted")
    return render(request, "displaysub.html", {"data": SubjectModel.objects.all()})


def updatesubject(request):
    id=request.GET.get("id")
    print(id)
    qs=SubjectModel.objects.get(classid=id)
    print(qs)
    return render(request,"update.html",{"data":qs})


def updatesave(request):
    cid = request.POST["cid"]
    subject = request.POST["subject"]
    SubjectModel(classid=cid, subject=subject).save()
    messages.success(request, "Subject is Saved")
    return redirect('displaysub')