from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def array_addition(request):
    if request.method == "GET":
        try:
            number = int(request.GET.get("number"))
            return HttpResponse(f"Square of Number {number} is {number*number}")
        except:
            return HttpResponse("Send Parameter number in url")

    if request.method == "POST":
        try:
            number = int(request.POST.get("number"))
            return HttpResponse(f"Square of Number {number} is {number*number}")
        except:
            return HttpResponse("Send Parameter number in data")


@csrf_exempt
def array_addition(request, number=None):

    if request.method == "PUT":
        try:
            return JsonResponse({"data": f"Square of Number {number} is {number*number}"})
        except:
            return HttpResponse("Send Parameter as array_addition/<number>")

    if request.method == "DELETE":
        try:
            return JsonResponse({"data": f"Square of Number {number} is {number*number}"})
        except:
            return HttpResponse("Send Parameter as array_addition/<number>")


@csrf_exempt
def palindrome_check(request):
    if request.method == "GET":
        try:
            string = request.GET.get("string")
            if string == string[::-1]:
                return HttpResponse(f"{string} is a palindrome")
            else:
                return HttpResponse(f"{string} is not a palindrome")
        except:
            return HttpResponse("Send Parameter string in url")

    if request.method == "POST":
        try:
            string = request.POST.get("string")
            if string == string[::-1]:
                return HttpResponse(f"{string} is a palindrome")
            else:
                return HttpResponse(f"{string} is not a palindrome")
        except:
            return HttpResponse("Send Parameter string in data")


@csrf_exempt
def palindrome_check(request, string=None):
    if request.method == "PUT":
        try:
            if string == string[::-1]:
                return JsonResponse({"result": f"{string} is palindrome"})
            else:
                return HttpResponse(f"{string} is not a palindrome")
        except:
            return HttpResponse("Send Parameter string in data")

    if request.method == "DELETE":
        try:
            if string == string[::-1]:
                return JsonResponse({"result": f"{string} is palindrome"})
            else:
                return HttpResponse(f"{string} is not a palindrome")
        except:
            return HttpResponse("Send Parameter string in data")


@csrf_exempt
def index(request):
    if request.method == "GET":
        try:
            csv_string = request.GET.get("array")
            string = csv_string.split(",")
            list = []
            for num in string:
                list.append(int(num))

            return HttpResponse(f"Sum is {sum(list)}")
        except:
            return HttpResponse("Send Parameter array in url as comma seperated 2,3,4")

    if request.method == "POST":
        try:
            csv_string = request.POST.get("array")
            string = csv_string.split(",")
            list = []
            for num in string:
                list.append(int(num))

            return HttpResponse(f"Sum is {sum(list)}")
        except:
            return HttpResponse("Send Parameter array in data as comma seperated 2,3,4")
