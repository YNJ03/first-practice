from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def getIndex(request) :
    return HttpResponse("<b>third/index :: 페이지 호출...</b>")

def getIndex2(request) :
    return render(request, "thirdapp/index.html", {})

def tableView(request) :
    context = {'prod_id' : 'c001', 'prod_name' : '전자제품', 'buyer_add' : '부산 남구'}
    mem_list = [context, context, context, context, context]
    contexts = {'mem_list' : mem_list}
    
    return render(request, "thirdapp/html/table.html", contexts)

def jsLogin2(request) :
    return render(request, "thirdapp/html/jsInputForm.html", {})

def jsLogin3(request) :
    ### post
    if request.method == "POST" :
        mem_mail = request.POST["mem_mail"]
        mem_age = request.POST["mem_age"]
        mem_pw = request.POST["mem_pw"]
        
    ### get    
    elif request.method == "GET" :
        mem_mail = request.GET["mem_mail"]
        mem_age = request.GET["mem_age"]
        mem_pw = request.GET["mem_pw"]        
    
    p_mail = "test@test.co.kr"
    p_age = "18"
    p_pw = "asdf1234"
        
    if (mem_mail == p_mail) and (mem_age == p_age) and (mem_pw == p_pw) :
        msg = """
            <script type='text/javascript'>
                alert('정상입력 입니다.');
                location.href = '/front/';
            </script>
        """
    else :
        msg = """
            <script type='text/javascript'>
                alert('비정상 입력 입니다.');
                history.go(-1);
            </script>        
        """
    return HttpResponse(msg)
    