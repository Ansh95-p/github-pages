from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import math

def index(request):
    return render(request, 'calc.html')
    # return HttpResponse("Hello, world. You're at the calculator index.")

def calculator(request):
    try:
        expression = request.GET.get('expression', '')
        expression = expression.replace('%', '/100')
        if "sqrt" in expression:
            expression += ')'
        res = eval(expression, {"sqrt": math.sqrt})
        return JsonResponse({
            'result': res
        })
    except Exception as e:
        return JsonResponse({
            'error': str(e)
        })