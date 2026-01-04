from django.urls import path
from .views import registerApi,login,AdminCurd,createProfile,addAddress,createdelivary_partner

urlpatterns=[
    path('register/',registerApi.as_view()),
    path('users/',AdminCurd.as_view()),
    path('delete/<str:email>/',AdminCurd.as_view()),
    path('update/<str:email>/',AdminCurd.as_view()),
    path('login/',login.as_view()),
    path('loginUser/',login.as_view()),
    path('createprofile/',createProfile.as_view()),
    path('updateProfile/',createProfile.as_view()),
    path('addAddress/',addAddress.as_view()),
    path('updateAddress/<int:id>/',addAddress.as_view()),
    path('deleate/<int:id>/',addAddress.as_view()),
    path('createPartner/',createdelivary_partner.as_view()),
]