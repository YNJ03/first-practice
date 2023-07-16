from django.shortcuts import render
from .DB_Sql import sql

# Create your views here.
from django.http import HttpResponse

### secondapp의 최초 페이지 만들기
def getIndex(request) :
    ### HTML 파일 사용..
    return render(request, "secondapp/index.html", {})

def getIndex2(request) :
    return HttpResponse("<b>secondapp의 index2 페이지 입니다.</b>")

def getIndex02(request) :
    return HttpResponse("getIndex02 :: 페이지 잘 호출 됩니다.")

def html01(request) :
    return render(request, "secondapp/html/html01.html", {})

def html02(request) :
    return render(request, "secondapp/html/html02.html", {})

def getMem_List1(request) :
    msg = sql.getMem_List()
    return render(request, "secondapp/html/mem_list.html", {"msg" : msg})

