from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse(f'<h1>Hello World</h1>')
def soma(request, num1, num2):
    soma = num1+num2
    return HttpResponse(f'<h1>A soma dos valores digitados é: {soma}</h1>')
def subtração(request, num1, num2):
    sub = num1-num2
    return HttpResponse(f'<h1>A subtração dos valores digitados é: {sub}</h1>')
def multiplicação(request, num1, num2):
    multi = num1*num2
    return HttpResponse(f'<h1>A multiplicação dos valores digitados é: {multi}</h1>')
def divisão(request, num1, num2):
    div = num1/num2
    return HttpResponse(f'<h1>A divisão dos valores digitados é: {div}</h1>')