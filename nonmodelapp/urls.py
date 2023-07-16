from django.urls import path

### oracleapp.py 폴더 하위에 있는 views.py 파일 읽어들이기 
# - 라이브러리 읽어들이는 것과 동일
from nonmodelapp import views

### 사용자가 요청할 수 있는 URL을 정의합니다.
# - url 하나당, views의 함수 1개를 호출할 수 있도록 매핑합니다.
# - url을 정의한다고 해서, 패턴(pattern) 정의라고 합니다.
urlpatterns = [
    # - http://127.0.0.1:8000/nonmodel/cart_list/
    path('cart_list/', views.getCartListPaging),
    
    # - http://127.0.0.1:8000/nonmodel/index/
    path('index/', views.Index),
    
    # - http://127.0.0.1:8000/nonmodel/
    path('', views.Index),
]
