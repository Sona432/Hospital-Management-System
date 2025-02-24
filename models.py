from django.db import models
class tbl_account(models.Model):
    
    account_id = models.CharField(max_length=90)
    name = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    
    class Meta:
        db_table = "tbl_account"         
class tbl_login(models.Model):
    
    username = models.CharField(max_length=90)
    password = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    
    class Meta:
        db_table = "tbl_login"     
class tbl_department(models.Model):
    
    department_id = models.CharField(max_length=90)
    name = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    
    class Meta:
        db_table = "tbl_department"      
class tbl_doctor(models.Model):
    
    doctor_id = models.CharField(max_length=90)
    account_id = models.CharField(max_length=30)
    department_id = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    qualification = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    remark = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    phone= models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    
    class Meta:
        db_table = "tbl_doctor"    
class tbl_patient(models.Model):
    
    patient_id = models.CharField(max_length=90)
    name = models.CharField(max_length=30)
    age = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    
    class Meta:
        db_table = "tbl_patient"          



class tbl_patient1(models.Model):
    
    patient_id = models.CharField(max_length=90)
    name = models.CharField(max_length=30)
    age = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    
    class Meta:
        db_table = "tbl_patient1"       


        
                 
class tbl_opdays(models.Model):
    
    op_id = models.CharField(max_length=90)
    doctor_id = models.CharField(max_length=30)
    doctor_name = models.CharField(max_length=30)
    department_id = models.CharField(max_length=30)
    opday = models.CharField(max_length=30)
    total_tokens=models.IntegerField()
    booked_tokens=models.IntegerField()
    ts1=models.IntegerField()
    ts2=models.IntegerField()
    ts3=models.IntegerField()
    
    class Meta:
        db_table = "tbl_opdays"     
class tbl_appointment(models.Model):
    
    appointment_id = models.CharField(max_length=90)
    op_id = models.CharField(max_length=30)
    doctor_id = models.CharField(max_length=30)
    patient_id = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    date = models.CharField(max_length=30)
    time = models.CharField(max_length=30)
    status=models.CharField(max_length=30)
    slot=models.CharField(max_length=30)
    
    class Meta:
        db_table = "tbl_appointment"      
class tbl_diagnosis(models.Model):
    
    diagnosis_id = models.CharField(max_length=90)
    appointment_id = models.CharField(max_length=30)
    doctor_id = models.CharField(max_length=30)
    date = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    patient_id = models.CharField(max_length=30)
    diagnosis = models.CharField(max_length=30)
    
    
    class Meta:
        db_table = "tbl_diagnosis"      
class tbl_medicine(models.Model):
    
    medicine_id = models.CharField(max_length=90)
    appointment_id = models.CharField(max_length=30)
    patient_id = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    diagnosis_id = models.CharField(max_length=30)
    doctor_id = models.CharField(max_length=30)
    medicine = models.CharField(max_length=30)
    dosage = models.CharField(max_length=30)
    date = models.CharField(max_length=30)
    
    
    
    
    class Meta:
        db_table = "tbl_medicine"           
                                            
                                            
class tbl_labtest(models.Model):
    
    test_id = models.CharField(max_length=90)
    appointment_id = models.CharField(max_length=30)
    patient_id = models.CharField(max_length=30)
    doctor_id = models.CharField(max_length=30)
    test = models.CharField(max_length=30)
    result = models.CharField(max_length=30)
    date = models.CharField(max_length=30)
    
    
    
    
    class Meta:
        db_table = "tbl_labtest"                                       

# Create your models here.
