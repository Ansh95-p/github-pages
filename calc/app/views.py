from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the calculator index.")

def calculator(request):
    result = None
    if request.method == "POST":
        num1 = request.POST.get("num1")
        num2 = request.POST.get("num2")
        operator = request.POST.get("operator")

        if operator == "+":
            result = int(num1) + int(num2)
        elif operator == "-":
            result = int(num1) - int(num2)
        elif operator == "*":
            result = int(num1) * int(num2)
        elif operator == "/":
            result = int(num1) / int(num2)

    return render(request, "calc.html", {"result": result})