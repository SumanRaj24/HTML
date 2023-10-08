from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from OTS.models import *

def welcome(requst):
    template=loader.get_template('welcome.html')
    return HttpResponse(template.render())
def candidateRegistrationForm(request):
    pass
def candidateaRegistration(request):
    pass
def loginView(request):
    pass
def candidateHome(request):
    pass
def testpaper(request):
    pass
def calculateTestResult(request):
    pass
def testResultHistory(request):
    pass
def showTestResult(request):
    pass
def logout(request):
    pass

