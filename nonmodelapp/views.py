from django.shortcuts import render
from django.http import HttpResponse

from nonmodelapp.nonmodel import cart

### 페이징처리 라이브러리
from django.core.paginator import Paginator

### 페이징(paging) 처리하기
def getCartListPaging(request) :
    ################# paging - 초기 변수값 처리 시작 ######################
    ### 현재 페이지 번호 설정
    now_page = request.GET.get("page", "1")
    # 전송되는 모든 데이터 타입은 문자열
    # - now_page 값은 숫자로 사용 : 숫자형태로 형변환 시켜야 합니다.
    now_page = int(now_page)
    ##### paging 처리 끝...
    
    cart_list = cart.cart_List()
    
    ################# paging - 목록 변수값 처리 시작 ######################
    ### 한 화면에 10개 행씩 보여주기 위해 조회한 결과에서 10개 추출하기
    ### 한 화면에 보여줄 행의 개수 지정
    num_row = 10
    
    ### Paginator() : 행의 개수만큼 데이터 추출하는 라이브러리
    p = Paginator(cart_list, num_row)
    
    ### 현재 페이지번호에 대항하는 10개 데이터 추출하기
    # - 최초 now_page는 1입니다.
    # - Paginator가 10개 행씩 가지고 있는 순서 중 1번째 그룹을 추출
    rows_data = p.get_page(now_page)
    ##### paging 처리 끝...
    
    ################# paging - 하단 페이지 처리 시작 ######################
    ### 시작페이지 번호(start_page) 계산하기
    start_page = (now_page - 1) // num_row * num_row + 1
    
    ### 종료페이지 번호(end_page) 계산하기
    end_page = start_page + 9
    
    ### 종료페이지의 번호가 전체 행의 개수보다 크면...
    # p.num_pages : 전체 행의 개수
    if end_page > p.num_pages : 
        end_page = p.num_pages
    ##### paging 처리 끝...
    
    ################# paging - 다음/이전 버튼 처리 시작 ######################
    ### 다음/이전 버튼을 보여줄지 여부에 대한 체크 변수
    # - 이전버튼 체크를 위한 초기값
    is_prev = False
    # - 다음버튼 체크를 위한 초기값
    is_next = False
    
    ### 이전버튼 보여줄지 여부 처리
    if start_page > 1 :
        is_prev = True
        
    ### 다음버튼 보여줄지 여부 처리
    if end_page < p.num_pages : 
        is_next = True
    ##### paging 처리 끝...
    
    context = {
        ### 데이터 목록 리스트
        "cart_list" : rows_data,
        ### 현재 페이지 번호 : 현재 선택된 값을 유지하기 위해서 사용
        "now_page" : now_page,
        ### 이전버튼 처리 변수
        "is_prev" : is_prev,
        ### 다음버튼 처리 변수
        "is_next" : is_next,
        ### 시작페이지 번호
        "start_page" : start_page,
        ### 페이지번호의 시작(start_page) ~ 종료페이지(end_page) 범위
        "page_range" : range(start_page, end_page + 1)
    }
    
    return render(request, "nonmodelapp/paging/cart_list.html", context)

### nonmodelapp 최초 페이지 처리
def Index(request) :
    return render(request, "nonmodelapp/index.html", {})

# Create your views here.
