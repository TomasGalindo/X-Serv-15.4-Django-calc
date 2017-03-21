from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def suma(request,op1,Operando,op2):
    if Operando == "+":
        return HttpResponse('<h1>Sumo! '+ str(int(op1) + int(op2))+ '</h1>')
    elif Operando == "-":
        return HttpResponse('<h1>Resto! '+ str(int(op1) - int(op2))+ '</h1>')
    elif Operando == "*":
        return HttpResponse('<h1>Multiplico! '+ str(int(op1) * int(op2))+ '</h1>')
    elif Operando == "/":
        return HttpResponse('<h1>Divido! ' + str(int(op1) / int(op2))+ '</h1>')

def notfound(request):
    return HttpResponse('<h1>No tengo ese recurso</h1>')
