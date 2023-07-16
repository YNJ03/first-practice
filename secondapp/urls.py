from django.urls import path

### firstapp.py 폴더 하위에 있는 views.py 파일 읽어들이기 
# - 라이브러리 읽어들이는 것과 동일
from . import views

### 사용자가 요청할 수 있는 URL을 정의합니다.
# - url 하나당, views의 함수 1개를 호출할 수 있도록 매핑합니다.
# - url을 정의한다고 해서, 패턴(pattern) 정의라고 합니다.
urlpatterns = [
    ### 클라이언트(User)가 웹브라우저 URL창에 아래 주소 입력하면 index 호출
    
    # - http://127.0.0.1:8000/second/
    path('', views.getIndex),
    
        # - http://127.0.0.1:8000/second/index/
    path('index/', views.getIndex),
    
    # - http://127.0.0.1:8000/second/index02/
    path('index02/', views.getIndex02),
    
    # - http://127.0.0.1:8000/second/html01/
    path('html01/', views.html01),
    
    # - http://127.0.0.1:8000/second/html02/
    path('html02/', views.html02),
    # - http://127.0.0.1:8000/second/mem_list/
    path('mem_list/', views.getMem_List1),
]