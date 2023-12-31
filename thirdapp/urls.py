from django.urls import path

### firstapp.py 폴더 하위에 있는 views.py 파일 읽어들이기 
# - 라이브러리 읽어들이는 것과 동일
from . import views

### 사용자가 요청할 수 있는 URL을 정의합니다.
# - url 하나당, views의 함수 1개를 호출할 수 있도록 매핑합니다.
# - url을 정의한다고 해서, 패턴(pattern) 정의라고 합니다.
urlpatterns = [
    ### 클라이언트(User)가 웹브라우저 URL창에 아래 주소 입력하면 index 호출
    
    # - http://127.0.0.1:8000/third/
    path('', views.getIndex2),
    
    # - http://127.0.0.1:8000/third/index/
    path('index/', views.getIndex2),
    
    # - http://127.0.0.1:8000/third/table/
    path('table/', views.tableView),
    
    # - http://127.0.0.1:8000/third/jsInputForm/
    path('jsInputForm/', views.jsLogin2),
    
    # - http://127.0.0.1:8000/third/login/
    path('login/', views.jsLogin3),
    
]