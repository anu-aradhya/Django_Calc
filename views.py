from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,"calc.html",{"name":"Anu Aradhya"})

def add(request):
    n1 = int(request.POST["num1"])
    n2 = int(request.POST["num2"])
    op = (request.POST["opr"])
    if op == "+":
        res = n1 + n2
    elif op == "-":
        res = n1 - n2
    elif op == "*":
        res = n1 * n2
    elif op == "/":
        if n2 != 0:
            res = n1 / n2
        else:
            messages.error(request,"Zero div Error")
            return render(request,"result.html",{"result" :"Enter a non zero number"})
    else:
        messages.error(request,"Invalid Operator")
        return render(request,"result.html",{"result":"Enter a valid operator!!"})
    return render(request,"result.html",{"result" : res})