from django.urls import path

from . import views

urlpatterns = [
    # - http:127.0.0.1:8000/front/
    	path('',views.index),
     
     # - http:127.0.0.1:8000/front/01_html
        path('01_html/', views.htmlView01),
        
    # - http:127.0.0.1:8000/front/02_link/
        path('02_link/', views.linkView),
        
    # - http:127.0.0.1:8000/front/03_css/
        path('03_css/', views.cssView),
        
    # - http:127.0.0.1:8000/front/04_css/
        path('04_css/', views.cssView04),
        
    # - http:127.0.0.1:8000/front/05_css/
        path('05_css/', views.cssView05),    

    # - http:127.0.0.1:8000/front/06_css/
        path('06_css/', views.cssView06),        
        
    # - http:127.0.0.1:8000/front/07_table/
        path('07_table/', views.tableView), 
        
    # - http:127.0.0.1:8000/front/08_table/
        path('08_table/', views.tableView02),  
         
    # - http:127.0.0.1:8000/front/09_mem/
        path('09_mem/', views.mem_View),    
    # - http:127.0.0.1:8000/front/10_mem_list/
        path('10_mem_list/', views.mem_View2),  
        
    # - http:127.0.0.1:8000/front/11_ul/
        path('11_ul/', views.ulView),  
        
    # - http:127.0.0.1:8000/front/12_div/
        path('12_div/', views.divView),
          
    # - http:127.0.0.1:8000/front/13_div/
        path('13_div/', views.divView2),  
        
    # - http:127.0.0.1:8000/front/14_iframe/
        path('14_iframe/', views.iframeView2),  
        
    # - http:127.0.0.1:8000/front/15_cssTable/
        path('15_cssTable/', views.cssTableView),  
        
    # - http:127.0.0.1:8000/front/16_cssTable/
        path('16_cssTable/', views.cssTableView2),  
        
    # - http:127.0.0.1:8000/front/17_cssNav/
        path('17_cssNav/', views.cssNavView),  
        
    # - http:127.0.0.1:8000/front/18_jsInputForm/
        path('18_jsInputForm/', views.jsInputFormView),  
        
    # - http:127.0.0.1:8000/front/19_login/
        path('19_login/', views.jsLogin),  
        
    # - http:127.0.0.1:8000/front/20_radioButton/
        path('20_radioButton/', views.radioButtonView),  
        
    # - http:127.0.0.1:8000/front/21_radio/
        path('21_radio/', views.jsRadioViews),  
        
    # - http:127.0.0.1:8000/front/22_radioButton2/
        path('22_radioButton2/', views.radioButtonView2),  
        
    # - http:127.0.0.1:8000/front/23_radio2/
        path('23_radio2/', views.jsRadioView2),  
        
    # - http:127.0.0.1:8000/front/24_checkbox/
        path('24_checkbox/', views.checkBoxView),  
        
    # - http:127.0.0.1:8000/front/25_checkbox2/
        path('25_checkbox2/', views.checkBoxView2),  
        
    # - http:127.0.0.1:8000/front/26_selectbox/
        path('26_selectbox/', views.selectBoxView),  
        
    # - http:127.0.0.1:8000/front/27_selectbox2/
        path('27_selectbox2/', views.selectBoxView2),  
        
    # - http:127.0.0.1:8000/front/28_bootstrap/
        path('28_bootstrap/', views.bootstrapView),  

        
    # - http:127.0.0.1:8000/front/29_bootstrap_table/
        path('29_bootstrap_table/', views.bootstrapTableView),  
        
    # - http:127.0.0.1:8000/front/30_bootstrap_form/
        path('30_bootstrap_form/', views.bootstrapFormView),  
        
    # - http:127.0.0.1:8000/front/31_bootstrap_layout/
        path('31_bootstrap_layout/', views.bootstrapLayoutView),  
        
    # - http:127.0.0.1:8000/front/32_include_index/
        path('32_include_index/', views.includeIndexView),  
        
    # - http:127.0.0.1:8000/front/33_main_index/
        path('33_main_index/', views.mainIndexView),  
        
    # - http:127.0.0.1:8000/front/34_extend_layout/
        path('34_extend_layout/', views.extendLayoutView),  
        
    # - http:127.0.0.1:8000/front/35_hello/
        path('35_hello/', views.extendHello),  
]