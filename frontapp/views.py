from django.shortcuts import render

from .DB_Sql.member import testData
### 또는 from .DB_Sql import member (일반적으로 사용됨)

from .DB_Sql.member import mem_List

from django.http import HttpResponse

# Create your views here.
def index(request) :
    return render(request, "frontapp/index.html", {})

def htmlView01(request) :
    return render(request, "frontapp/html/01_html.html", {})

def linkView(request) :
    return render(request, "frontapp/html/02_link.html", {})

def cssView(request) :
    return render(request, "frontapp/html/03_css.html", {})

def cssView04(request) :
    return render(request, "frontapp/html/04_css.html", {})

def cssView05(request) :
    return render(request, "frontapp/html/05_css.html", {})

def cssView06(request) :
    return render(request, "frontapp/html/06_css.html", {})

def tableView(request) :
    return render(request, "frontapp/html/07_table.html", {})

def tableView02(request) :
#    mem_id = "b001"
#    mem_name = "이순신"
#    mem_addr = "부산 금정구"
#    return render(request, "frontapp/html/08_table.html", {"mem_id" : mem_id, "mem_name" : mem_name, "mem_addr" : mem_addr})

    ### 테이블 기준으로 -> 딕셔너리 1개는 행 1개를 의미함...
    # - 많이 사용하므로 기억하기!!(중요)
    context = {"mem_id" : 'b001', "mem_name" : '홍길동2', "mem_addr" : '부산 수영구 수영동'}
    
    mem_list = [context, context, context]
    
    contexts = {"mem_list" : mem_list, "mem_id" : 'b001', "mem_name" : '홍길동2', "mem_addr" : '부산 수영구 수영동'}
    
    ### render()함수의 3번째 인자값은 딕셔너리 타입만 가능합니다.
    return render(request, "frontapp/html/08_table.html", contexts)

def mem_View(request) :
    return render(request, "frontapp/html/09_mem.html", {"name" : testData()})

### 또는 def mem_View(request) :
#            msg = member.testData()
#            return render(request, "frontapp/html/09_mem.html", {"msg" : msg)

def mem_View2(request) :
    msg1 = mem_List()
    return render(request, "frontapp/html/10_mem_list.html", {'msg1' : msg1})

def ulView(request) :
    return render(request, "frontapp/html/11_ul.html", {})

def divView(request) :
    return render(request, "frontapp/html/12_div.html", {})

def divView2(request) :
    return render(request, "frontapp/html/13_div.html", {})

def iframeView2(request) :
    return render(request, "frontapp/html/14_iframe.html", {})

def cssTableView(request) :
    return render(request, "frontapp/css/15_cssTable.html", {})

def cssTableView2(request) :
    return render(request, "frontapp/css/16_cssTable.html", {})

def cssNavView(request) :
    return render(request, "frontapp/css/17_cssNav.html", {})

def jsInputFormView(request) :
    mem_id = "b001"
    mem_pass = "1234"
    return render(request, "frontapp/js/18_jsInputForm.html", {"mem_id" : mem_id, "mem_pass" : mem_pass})

def jsLogin(request) :
    
    ### 요청 데이터 추출하기
    # post 방식
    # - request 변수가 모든 요청 정보를 가지고 있음
    # - method : 요청 시에 전송방식 확인
    # - 값을 추출하는 방식 : 딕셔너리 변수는 POST
    # - POST 딕셔너리 변수를 이용해서 파이썬 문법에 맞게 추출
    if request.method == "POST" :
        mem_id = request.POST["mem_id"]
        mem_pass = request.POST["mem_pass"]
    
    # GET 방식으로 요청이 들어온 경우 아래 처리..
    elif request.method == "GET" :
        mem_id = request.GET["mem_id"]
        mem_pass = request.GET["mem_pass"] 
         
    # rsmsg = "아이디 : {} / 패스워드 : {}".format(mem_id, mem_pass)
     
    ### 요청받은(입력받은) 데이터와 비교하기 위한 기준 데이터 정의
    # - 실제로는 DB에 조회해서 결과 확인 후 있으면 정상, 없으면 비정상 처리
        
    p_id = 'b001'
    p_pw = '1357'
    
    ### 조건 처리
    if (mem_id == p_id) and (mem_pass == p_pw) :
        rsmsg = "아이디 b001님 정상적으로 로그인 되었습니다"
    else :
        rsmsg = "아이디 또는 패스워드를 확인해 주세요!"
        
    ### 조건 처리 : 자바스크립트로 응답해주기
    if (mem_id == p_id) and (mem_pass == p_pw) :
        rsmsg = """
            <script type= 'text/javascript'>
            alert('아이디 b001님 정상적으로 로그인 되었습니다');
            url = "/front/";
            location.href = url;
            </script>
        """

    else :
        rsmsg = """
            <script type= 'text/javascript'>
            alert('아이디 또는 패스워드를 확인해 주세요!');
            history.go(-1);
            </script>
        """
        
    return HttpResponse(rsmsg)

def radioButtonView(request) :
    return render(request, "frontapp/js/20_radioButton.html", {})

def jsRadioViews(request) :
    try : 
        ### 브라우저에서 요청한(입력한) 데이터 받아오기
        if request.method == "POST" :
            if request.POST.get("mem_addr") is not None :
                mem_addr = request.POST["mem_addr"]
                mem_addr1 = request.POST["mem_addr1"]
                # mem_addr = request.POST.get("mem_addr") - get은 오류 발생을 잘 안시킴
                
            else :
                rsmsg = """
                        <script text/javascript>
                        alert('잘못된 접근입니다.111');
                        history.go(-1);
                        </script>
                """
                return HttpResponse(rsmsg)
        
        ### post방식이 오류나거나 하면 무조건 get방식으로 접근함
        elif request.method == "GET" :
            if request.GET.get("mem_addr") is not None :
                mem_addr = request.GET["mem_addr"]
                mem_addr1 = request.GET["mem_addr1"]
            else :
                rsmsg = """
                        <script text/javascript>
                        alert('잘못된 접근입니다.333');
                        history.go(-1);
                        </script>
                """
                return HttpResponse(rsmsg)
        
        ### 결과 처리 영역
        # 부산인지 아닌지 비교하기
        if mem_addr1 == "부산" :
            rsmsg = """
                <script text/javascript>
                alert('{} 지역을 선택하셨습니다!!');
                location.href = '/front/';
                </script>
            """.format(mem_addr1)
        
        else :
            rsmsg = """
                <script text/javascript>
                alert('부산 지역이 아닙니다. 다시 선택해 주세요!');
                history.go(-1);
                </script>
            """
        
        ### 최종 결과 출력    
        return HttpResponse(rsmsg)
        
    except : 
        rsmsg = """
            <script text/javascript>
            alert('잘못된 접근입니다.222');
            history.go(-1);
            </script>
            """
        return HttpResponse(rsmsg)
    
def radioButtonView2(request) :
    return render(request, "frontapp/js/22_radioButton2.html", {"mem_addr" : "부산", "mem_addr1" : "부산"})
    
def jsRadioView2(request) :
    try : 
        ### 브라우저에서 요청한(입력한) 데이터 받아오기
        if request.method == "POST" :
            if request.POST.get("mem_addr") is not None :
                mem_addr = request.POST["mem_addr"]
                mem_addr1 = request.POST["mem_addr1"]
                # mem_addr = request.POST.get("mem_addr") - get은 오류 발생을 잘 안시킴
                
            else :
                rsmsg = """
                        <script text/javascript>
                        alert('잘못된 접근입니다.111');
                        history.go(-1);
                        </script>
                """
                return HttpResponse(rsmsg)
        
        ### post방식이 오류나거나 하면 무조건 get방식으로 접근함
        elif request.method == "GET" :
            if request.GET.get("mem_addr") is not None :
                mem_addr = request.GET["mem_addr"]
                mem_addr1 = request.GET["mem_addr1"]
            else :
                rsmsg = """
                        <script text/javascript>
                        alert('잘못된 접근입니다.333');
                        history.go(-1);
                        </script>
                """
                return HttpResponse(rsmsg)
        
        ### 결과 처리 영역
        # 부산인지 아닌지 비교하기
        if mem_addr1 == "부산" :
            rsmsg = """
                <script text/javascript>
                alert('{} 지역을 선택하셨습니다!!');
                location.href = '/front/';
                </script>
            """.format(mem_addr1)
        
        else :
            rsmsg = """
                <script text/javascript>
                alert('부산 지역이 아닙니다. 다시 선택해 주세요!');
                history.go(-1);
                </script>
            """          
        
        ### 최종 결과 출력    
        return HttpResponse(rsmsg)
        
    except : 
        rsmsg = """
            <script text/javascript>
            alert('잘못된 접근입니다.222');
            history.go(-1);
            </script>
            """
        return HttpResponse(rsmsg)  
    
def checkBoxView(request) :
    return render(request, "frontapp/js/24_checkbox.html", {})  
    
def checkBoxView2(request) :
    ### 딕셔너리 get은 무자열 데이터만 처리가능
    # - 리스트로 전송되는 데이터는 getlist() 함수를 사용해야 함
    if request.POST.get("mem_addr") is not None :
        mem_addr = request.POST.get("mem_addr")
        ### getlist() : 파이썬의 리스트 형태로 데이터 받음
        # - 예시 : ["서울", "부산"]
        mem_addr_list = request.POST.getlist("mem_addr")
        
        str_list = ""
        for i in range(len(mem_addr_list)) :
            str_list += mem_addr_list[i]
            if i < len(mem_addr_list)-1 :
                str_list += "," 
        
    return render(request, "frontapp/js/25_checkbox.html", {"mem_addr" : mem_addr, "mem_addr_list" : mem_addr_list, "str_list" : str_list})  

def selectBoxView(request) :
    return render(request, "frontapp/js/26_selectbox.html", {})  

def selectBoxView2(request) :
    if request.POST.get("mem_addr_multi") is not None :
        mem_addr_one = request.POST.get("mem_addr_one")
        mem_addr_multi_list = request.POST.getlist("mem_addr_multi")
        str_list = ""
        for i in range(len(mem_addr_list)) :
            str_list += mem_addr_list[i]
            if i < len(mem_addr_list)-1 :
                str_list += ","        
        
    return render(request, "frontapp/js/27_selectbox2.html", {"mem_addr_one" : mem_addr_one, "mem_addr_multi_list" : mem_addr_multi_list})  

def bootstrapView(request) :
    return render(request, "frontapp/bootstrap/28_bootstrap.html", {})

def bootstrapTableView(request) :
    return render(request, "frontapp/bootstrap/29_bootstrap_table.html", {})

def bootstrapFormView(request) :
    return render(request, "frontapp/bootstrap/30_bootstrap_form.html", {})

def bootstrapLayoutView(request) :
    return render(request, "frontapp/bootstrap/31_bootstrap_layout.html", {})

def includeIndexView(request) :
    return render(request, "frontapp/include/32_include_index.html", {})

def mainIndexView(request) :
    return render(request, "frontapp/include/33_main_index.html", {})

def extendLayoutView(request) :
    return render(request, "frontapp/extend/34_extend_layout.html", {})

def extendHello(request) :
    return render(request, "frontapp/extend/35_hello.html", {})


