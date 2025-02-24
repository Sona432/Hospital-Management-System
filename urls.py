"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views
from django.conf  import settings
from django.conf.urls.static import static
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index),
    path('add_account/',views.add_account),
    path('login/',views.login),
    path('logout/',views.logout),
    path('login1/',views.login1),
    path('admins/',views.admins),
    path('doctor/',views.doctor),
    path('patient/',views.patient),
    path('lab/',views.lab),
    path('add_department/',views.add_department),
    path('add_account1/',views.add_account1),
    path('add_department1/',views.add_department1),
    path('remove_account/',views.remove_account),
    path('remove_department/',views.remove_department),
    path('remove_account1/<int:id>',views.remove_account1),
    path('remove_department1/<int:id>',views.remove_department1),
    path('add_doctor/',views.add_doctor),
    path('add_doctor1/<int:id>',views.add_doctor1),
    path('add_doctor2/',views.add_doctor2),
    path('update_doctor/',views.update_doctor),
    path('update_doctor1/<int:id>',views.update_doctor1),
    path('update_doctor2/<int:id>',views.update_doctor2),
    path('add_patient/',views.add_patient),
    path('add_patient1/',views.add_patient1),
    path('update_patient/',views.update_patient),
    path('update_patient1/<int:id>',views.update_patient1),
    path('update_patient2/<int:id>',views.update_patient2),
    path('edit_profile/',views.edit_profile),
    path('edit_profiles/<int:id>',views.edit_profile1),
    path('opdays/',views.opdays),
    path('opdays1/<int:id>',views.opdays1),
    path('opdays2/<int:id>',views.opdays2),
    path('search_doctor/',views.search_doctor),
    path('search_doctor1/<str:id>',views.search_doctor1),
    path('search_doctor2/<str:id>',views.search_doctor2),
    path('view_appointment/',views.view_appointment),
    path('details/<str:id>',views.details),
    path('diagnosis/<str:id>',views.diagnosis),
    path('diagnosis1/<int:id>',views.diagnosis1),
    path('medicine1/<str:id>',views.medicine1),
    path('lab_test/<str:id>',views.lab_test),
    path('lab_testes/<str:id>',views.lab_test1),
    path('finish/<str:id>',views.finish),
    path('view_diagnosis/<str:id>',views.view_diagnosis),
    path('view_medicine/<str:id>',views.view_medicine),
    path('view_test/<str:id>',views.view_test),
    path('view_diagnosis1/<str:id>',views.view_diagnosis1),
    path('view_medicine1/<str:id>',views.view_medicine1),
    path('view_test1/<str:id>',views.view_test1),
    path('view_appointment1/',views.view_appointment1),
    path('view_result/',views.view_result),
    path('view_result2/<str:id>',views.view_result2),
    path('testes/<int:id>',views.view_result3),
    path('labs/<int:id>',views.labs),
    path('patientreg/',views.patientreg),
    path('doctorreg/',views.doctorreg),
    path('doctorreg1/',views.doctorreg1),
    path('patientreg1/',views.patientreg1),
    path('verifypatient/',views.verifypatient),
    path('verifydoctor/',views.verifydoctor),
    path('verifydoctor1/<int:id>',views.verifydoctor1),
    path('rejectdoctor1/<int:id>',views.rejectdoctor1),
    path('verifypatient1/<int:id>',views.verifypatient1),
    path('view_appointments/',views.view_appointments),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
