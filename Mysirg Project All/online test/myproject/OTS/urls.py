from django.urls import path
from OTS.views import *
urlpatterns = [
    path('',welcome),
    path('new-candidate',candidateRegistrationForm,name='registrationForm'),
    path('store-candidate',candidateaRegistration),
    path('login',loginView,name='login'),
    path('home',candidateHome),
    path('test-paper',testpaper),
    path('calculate-result',calculateTestResult),
    path('test-history',testResultHistory),
    path('result',showTestResult),
    path('logout',loginView),
]
