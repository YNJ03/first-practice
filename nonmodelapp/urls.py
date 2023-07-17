from django.urls import path

### oracleapp.py 폴더 하위에 있는 views.py 파일 읽어들이기 
# - 라이브러리 읽어들이는 것과 동일
from nonmodelapp import views

### 사용자가 요청할 수 있는 URL을 정의합니다.
# - url 하나당, views의 함수 1개를 호출할 수 있도록 매핑합니다.
# - url을 정의한다고 해서, 패턴(pattern) 정의라고 합니다.
urlpatterns = [
    ### 지도맵 시각화
    # - http://127.0.0.1:8000/nonmodel/map_view/
    path('map_view/', views.map_Visualization),
    
    ### 데이터 시각화
    # - http://127.0.0.1:8000/nonmodel/data_view/
    path('data_view/', views.data_Visualization),
        
    ### 파일 업로드/다운로드 처리
    # - 파일 다운로드 처리
    # - http://127.0.0.1:8000/nonmodel/file_down/
    path('file_down/', views.setDownload),
    
    # - 파일 업로드 처리
    # - http://127.0.0.1:8000/nonmodel/file_upload/
    path('file_upload/', views.getFileUpload),
    
    # - 파일 업로드 페이지 처리
    # - http://127.0.0.1:8000/nonmodel/file_upload_form/
    path('file_upload_form/', views.getFileUploadForm),
    
    ### 로그인/로그아웃 처리
    # - 로그인 처리
    # - http://127.0.0.1:8000/nonmodel/login_chk/
    path('login_chk/', views.login_chk),
    
    # - 로그아웃 처리
    # - http://127.0.0.1:8000/nonmodel/logout_chk/
    path('logout_chk/', views.logout_chk),
    
    
    ### 페이징 처리
    # - http://127.0.0.1:8000/nonmodel/cart_list/
    path('cart_list/', views.getCartListPaging),
    
    

    # - http://127.0.0.1:8000/nonmodel/index/
    path('index/', views.Index),
    
    # - http://127.0.0.1:8000/nonmodel/
    path('', views.Index),
]
