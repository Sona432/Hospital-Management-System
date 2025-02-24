from django.shortcuts import render,HttpResponse,redirect
from app1.models import tbl_login,tbl_account,tbl_department,tbl_doctor,tbl_patient,tbl_opdays,tbl_appointment
from app1.models import tbl_diagnosis,tbl_medicine,tbl_labtest
from django.core.files.storage import FileSystemStorage
import datetime
from django.core.mail import send_mail
def index(request):
    return render(request,"index.html")
def lab(request):
    return render(request,"lab_home.html")    
def add_account(request):
    return render(request,"add_account.html")    
def login(request):
    return render(request,"login.html")   
def login1(request):
    if request.method=='POST':
        data=tbl_login.objects.all()
        Username=request.POST.get('username')
        Password=request.POST.get('password')
        flag=0
        for da in data:
            if Username==da.username and Password==da.password:
                type=da.category
                flag=1
                request.session['uid']=Username
                if type=="admin":
                    return redirect('/admins')
                elif type=="doctor":
                    return redirect('/doctor')
                elif type=="patient":
                    return redirect('/patient')
                elif type=="lab":
                    return redirect('/lab')
                   
               
                else:
                    return HttpResponse("Invalid acct type")
        if flag==0:
            return HttpResponse("User doesn't exist")  
def admins(request):
    return render(request,"admin_home.html")    
def doctor(request):
    return render(request,"doctor_home.html")    
def patient(request):
    return render(request,"patient_home.html")     
def add_department(request):
    return render(request,"add_department.html")   
def add_account1(request):
    if request.method == 'POST':
        data =tbl_account()
        data.account_id="na"
        data.name=request.POST.get('name')
        data.role=request.POST.get('role')
        data.phone=request.POST.get('phone')
        data.email=request.POST.get('email')
        data.status="active"
        data.save()


        data.account_id = "ACCOUNT_00" + str(data.id)
        data.save()
        if data.role=="lab":

            data1=tbl_login()
            data1.username="ACCOUNT_00" + str(data.id)
            data1.password=request.POST.get('phone')
            data1.category="lab"
            send_mail('login','username'+data1.username+'password'+data1.password,'from@example.co',[data.email,])


            data1.save()
        return render(request,"add_account.html")
def add_department1(request):
    if request.method == 'POST':
        data =tbl_department()
        data.department_id="na"
        data.name=request.POST.get('name')
        data.status="active"
        data.save()


        data.department_id = "DEPARTMENT_00" + str(data.id)
        data.save()
        return render(request,"add_department.html")    

def remove_account(request):
    items = tbl_account.objects.all()
    return render(request,"remove_account.html",{'items':items }) 
def remove_department(request):
    items = tbl_department.objects.all()
    return render(request,"remove_department.html",{'items':items })     
def remove_account1(request,id):
    items = tbl_account.objects.get(id=id)
    items.delete()
    return redirect('/remove_account')
def remove_department1(request,id):
    items = tbl_department.objects.get(id=id)
    items.delete()
    return redirect('/remove_department')     
def add_doctor(request):
    items = tbl_account.objects.filter(role="doctor").filter(status="active")
    return render(request,"add_doctor.html",{'items':items }) 
def add_doctor1(request,id):
    items = tbl_account.objects.get(id=id)
    data=tbl_department.objects.all()
    return render(request,"add_doctor1.html",{'items':items,'data':data})           
def add_doctor2(request):
    if request.method == 'POST':
        data =tbl_doctor()
        data.doctot_id="na"
        data.account_id=request.POST.get('account_id')
        data.department_id=request.POST.get('department_id')
        data.name=request.POST.get('name')
        data.qualification=request.POST.get('qualification')
        data.gender=request.POST.get('gender')
        data.remark=request.POST.get('remark')
        data.email=request.POST.get('email')
        data3=tbl_account.objects.get(account_id=request.POST.get('account_id'))
        data.phone=data3.phone
        data.email=data3.email
        data.status="ok"
        data.save()
        data.doctor_id = "DOCTOR_00" + str(data.id)
        data.save()
        data1=tbl_login()
        data1.username="DOCTOR_00" + str(data.id)
        data1.password=data3.phone
        data1.category="doctor"
        data1.save()
        data3.status="ok"
        data3.save()
        send_mail('login','username'+data.doctor_id+'password'+data3.phone,'from@example.co',[data.email,])


        return redirect('/add_doctor')    
def update_doctor(request):
    items = tbl_doctor.objects.filter(status="ok")
    return render(request,"update_doctor.html",{'items':items })    
def update_doctor1(request,id):
    items = tbl_doctor.objects.get(id=id)
    return render(request,"update_doctor1.html",{'items':items })          
def update_doctor2(request,id):
    items = tbl_doctor.objects.get(id=id)
    items.qualification=request.POST.get('qualification')
    items.remark=request.POST.get('remark')
    items.save()
    return redirect('/update_doctor')    
def add_patient(request):
    return render(request,"add_patient.html")    
def add_patient1(request):
    if request.method == 'POST':
        data =tbl_patient()
        data.patient_id="na"
        data.name=request.POST.get('name')
        data.age=request.POST.get('age')
        data.gender=request.POST.get('gender')
        data.address=request.POST.get('address')
        data.phone=request.POST.get('phone')
        data.status="ok"
        data.save()
        data.patient_id = "PATIENT_00" + str(data.id)
        data.save()
        data1=tbl_login()
        data1.username="PATIENT_00" + str(data.id)
        data1.password=request.POST.get('phone')
        data1.category="patient"
        data1.save()
        send_mail('login','username'+data.patient_id+'password'+data.phone,'from@example.co',[data.email,])
        return render(request,'add_patient.html')   
def update_patient(request):
    items = tbl_patient.objects.filter(status="ok")
    return render(request,"update_patient.html",{'items':items })    
def update_patient1(request,id):
    items = tbl_patient.objects.get(id=id)
    return render(request,"update_patient1.html",{'items':items })          
def update_patient2(request,id):
    items = tbl_patient.objects.get(id=id)
    items.address=request.POST.get('address')
    items.phone=request.POST.get('phone')
    items.save()
    return redirect('/update_patient')      
def edit_profile(request):
    uid=request.session['uid']
    items = tbl_patient.objects.get(patient_id=uid)
    return render(request,"edit_profile.html",{'items':items })   
def edit_profile1(request,id):
    items = tbl_patient.objects.get(id=id)
    items.name=request.POST.get('name')
    items.age=request.POST.get('age')
    items.gender=request.POST.get('gender')
    items.address=request.POST.get('address')
    items.phone=request.POST.get('phone')
    items.save()
    return redirect('/edit_profile')    
def opdays(request):
    items = tbl_doctor.objects.all()
    return render(request,"opdays.html",{'items':items })        
def opdays1(request,id):
    items = tbl_doctor.objects.get(id=id)
    return render(request,"opdays1.html",{'items':items })  
def opdays2(request,id):
    if request.method == 'POST':
        data =tbl_opdays()
        data.op_id="na"
        data.doctor_id=request.POST.get('doctor_id')
        data.doctor_name=request.POST.get('name')
        data.department_id=request.POST.get('department_id')
        data.opday=request.POST.get('opday')
        data.total_tokens=request.POST.get('total_tokens')
        data.booked_tokens=0
        data.ts1=0
        data.ts2=0
        data.ts3=0

        data.save()


        data.op_id = "OP_00" + str(data.id)
        data.save()
        return redirect('/opdays')
def search_doctor(request):
    items = tbl_doctor.objects.all()
    return render(request,"search_doctor.html",{'items':items })      
def search_doctor1(request,id):
    items = tbl_opdays.objects.filter(doctor_id=id)
    return render(request,"search_doctor1.html",{'items':items })   
def search_doctor2(request,id):
        data1=tbl_opdays.objects.get(op_id=id)
        now = datetime.datetime.now()
        s=now.strftime("%A")
        if s==data1.opday:

            t1=datetime.datetime.now().strftime('%H:%M:%S')
            t2="15.00.00"
            if t1>t2:
                return render(request,"status2.html")
            else:    
            
                if data1.booked_tokens<data1.total_tokens:

                    data2=tbl_patient.objects.get(patient_id=request.session['uid'])
                    data =tbl_appointment()
                    data.appointment_id="na"
                    data.op_id=id
                    data.doctor_id=data1.doctor_id
                    data8=tbl_doctor.objects.get(doctor_id=data1.doctor_id)
                    data.patient_id=data2.patient_id
                    data.name=data2.name
                    data.date=datetime.datetime.now().strftime ("%Y-%m-%d")
                    data.time= datetime.datetime.now().strftime('%H:%M:%S')
                    data.status="pending"
                    data.save()
                    data.appointment_id = "APPOINTMENT_00" + str(data.id)
                    data.save()
                    send_mail('login','appointment'+data.appointment_id,'from@example.co',[data8.email,])

                    b=data1.booked_tokens
                    b=int(b+1)
                    data1.booked_tokens=b
                    data1.save()
                    if data1.booked_tokens<=10:
                        c=data1.ts1
                        c=int(c+1)
                        data1.ts1=c
                        data1.save()
                        a="time slot is 2 to 3"
                        data.slot=a
                        data.save()
                    if data1.booked_tokens<=20 and data1.booked_tokens>10:
                        c=data1.ts2
                        c=int(c+1)
                        data1.ts2=c
                        data1.save()
                        a="time slot is 3 to 4"
                        data.slot=a
                        data.save()
                    if data1.booked_tokens<=30 and data1.booked_tokens>20:
                        c=data1.ts3
                        c=int(c+1)
                        data1.ts3=c 
                        data1.save()
                        a="time slot is 4 to 5" 
                        data.slot=a
                        data.save()
                    return render(request,"status.html",{'a':a})   
                else:   
                    return render(request,"status1.html")   
        else:  
            return render(request,"status5.html")  

  
def view_appointment(request):
    date=datetime.datetime.now().strftime ("%Y-%m-%d")
    uid=request.session['uid']
    items = tbl_appointment.objects.filter(doctor_id=uid).filter(date=date).filter(status="pending")
    return render(request,"view_appointment.html",{'items':items })     
def details(request,id):
    items = tbl_patient.objects.get(patient_id=id)
    return render(request,"details.html",{'items':items })    
def diagnosis(request,id):
    items = tbl_appointment.objects.get(appointment_id=id)
    return render(request,"diagnosis.html",{'items':items })     
def diagnosis1(request,id):
        data1=tbl_appointment.objects.get(id=id)
        data =tbl_diagnosis()
        data.diagnosis_id="na"
        data.appointment_id=data1.appointment_id
        data.doctor_id=data1.doctor_id
        data.date=datetime.datetime.now().strftime ("%Y-%m-%d")
        data.name=data1.name
        data.patient_id=data1.patient_id
        data.diagnosis=request.POST.get('diagnosis')
        data.save()


        data.diagnosis_id = "DIAGNOSIS_00" + str(data.id)
        data.save()
        return render(request,'medicine.html',{'d1':data.diagnosis_id,'a1':data1.appointment_id})    
def medicine1(request,id):
        data1=tbl_appointment.objects.get(appointment_id=id)
        data =tbl_medicine()
        data.medicine_id="na"
        data.appointment_id=data1.appointment_id
        data.patient_id=data1.patient_id
        data.name=data1.name
        data.diagnosis_id=request.POST.get('diagnosis_id')
        data.doctor_id=data1.doctor_id
        data.medicine=request.POST.get('medicine')
        data.dosage=request.POST.get('dosage')
        data.date=datetime.datetime.now().strftime ("%Y-%m-%d")
        
        
        
        data.save()


        data.medicine_id = "MEDICINE_00" + str(data.id)
        data.save()
        request.session['did']=request.POST.get('diagnosis_id')
        return render(request,'medicine.html',{'d1':request.POST.get('diagnosis_id'),'a1':data1.appointment_id})     
def lab_test1(request,id):
        data1=tbl_appointment.objects.get(appointment_id=id)
        data =tbl_labtest()
        data.test_id="na"
        data.appointment_id=data1.appointment_id
        data.patient_id=data1.patient_id
        data.doctor_id=data1.doctor_id
        data.test=request.POST.get('test')
        data.date=datetime.datetime.now().strftime ("%Y-%m-%d")
        did=request.session['did']
        data.save()

        
        data.test_id = "TEST_00" + str(data.id)
        data.save()
        return render(request,'medicine.html',{'d1':did,'a1':data1.appointment_id}) 
   
def lab_test(request,id):             
    return render(request,'labtest.html',{'a1':id})    
def finish(request,id):
    data1=tbl_appointment.objects.get(appointment_id=id)   
    data1.status="ok"
    data1.save()
    return redirect('/view_appointment')       
def view_diagnosis(request,id):
    items = tbl_diagnosis.objects.filter(patient_id=id)
    return render(request,"view_diagnosis.html",{'items':items })   
def view_medicine(request,id):
    items = tbl_medicine.objects.filter(appointment_id=id)
    return render(request,"view_medicine.html",{'items':items })  
def view_test(request,id):
    items = tbl_labtest.objects.filter(appointment_id=id)
    return render(request,"view_test.html",{'items':items })   
def logout(request):
    del request.session['uid']
    return redirect('/index')      
def view_diagnosis1(request,id):
    items = tbl_diagnosis.objects.filter(appointment_id=id)
    return render(request,"view_diagnosis1.html",{'items':items })   
def view_medicine1(request,id):
    items = tbl_medicine.objects.filter(appointment_id=id)
    return render(request,"view_medicine1.html",{'items':items })  
def view_test1(request,id):
    items = tbl_labtest.objects.filter(appointment_id=id)
    return render(request,"view_test1.html",{'items':items })  
def view_appointment1(request):
    items = tbl_appointment.objects.filter(patient_id=request.session['uid']).filter(status="ok")
    return render(request,"view_appointment1.html",{'items':items })         
def view_result(request):
    items = tbl_labtest.objects.all()
    return render(request,"view_test2.html",{'items':items })       
def view_result2(request,id):
    items = tbl_labtest.objects.get(appointment_id=id)
    return render(request,"view_test3.html",{'items':items})   
def view_result3(request,id):
    if request.method=='POST':
        items = tbl_labtest.objects.get(id=id)
        Photo = request.FILES['result']
        fs = FileSystemStorage()
        filename = fs.save(Photo.name, Photo) 
        uploaded_file_url = fs.url(filename)
        items.result=uploaded_file_url
        items.save()
        return render(request,"patient_home.html")     
def labs(request,id):
    items = tbl_labtest.objects.get(id=id)
    return render(request,"labs.html",{'items':items})      
def patientreg(request):
    return render(request,"patientreg.html")        
def doctorreg(request):
    data=tbl_department.objects.all()
    return render(request,"doctorreg.html",{'data':data}) 
def doctorreg1(request):
    if request.method == 'POST':
        data =tbl_doctor()
        data.doctot_id="na"
        data.account_id="na"
        data.department_id=request.POST.get('department_id')
        data.name=request.POST.get('name')
        data.qualification=request.POST.get('qualification')
        data.gender=request.POST.get('gender')
        data.remark=request.POST.get('remark')
        data.email=request.POST.get('email')
        data.phone=request.POST.get('phone')
        data.status="not"
        data.save()
        data.doctor_id = "DOCTOR_00" + str(data.id)
        data.save()
        return redirect('/doctorreg')   
def patientreg1(request):
    if request.method == 'POST':
        data =tbl_patient()
        data.patient_id="na"
        data.name=request.POST.get('name')
        data.age=request.POST.get('age')
        data.gender=request.POST.get('gender')
        data.address=request.POST.get('address')
        data.phone=request.POST.get('phone')
        data.email=request.POST.get('email')
        data.status="not"
        data.save()
        data.patient_id = "PATIENT_00" + str(data.id)
        data.save()
        return redirect('/patientreg')
def verifydoctor(request):
    items = tbl_doctor.objects.filter(status="not")
    return render(request,"verifydoctor.html",{'items':items })         
def verifypatient(request):
    items = tbl_patient.objects.filter(status="not")
    return render(request,"verifypatient.html",{'items':items })   
def verifydoctor1(request,id):
    items = tbl_doctor.objects.get(id=id)
    items.status="ok"
    items.save()
    data1=tbl_login()
    data1.username=items.doctor_id
    data1.password=items.phone
    data1.category="doctor"
    data1.save()
    send_mail('login','username'+items.doctor_id+'password'+items.phone,'from@example.co',[items.email,])
    return redirect('/verifydoctor')   
def rejectdoctor1(request,id):
    items = tbl_doctor.objects.get(id=id)
    items.status="rejected"
    items.save()
    return redirect('/verifydoctor')   
def verifypatient1(request,id):
    items = tbl_patient.objects.get(id=id)
    items.status="ok"
    items.save()
    data1=tbl_login()
    data1.username=items.patient_id
    data1.password=items.phone
    data1.category="patient"
    data1.save()
    send_mail('login','username'+items.patient_id+'password'+items.phone,'from@example.co',[items.email,])
    return redirect('/verifypatient')     
def view_appointments(request):
    date=datetime.datetime.now().strftime ("%Y-%m-%d")
    uid=request.session['uid']
    items = tbl_appointment.objects.filter(patient_id=uid).filter(date=date)   
    return render(request,"view_appointment.html",{'items':items })     
                                  
                              
            
         



# Create your views here.
