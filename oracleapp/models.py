from django.db import models

### DB에서 문자열을 관리하는 타입은 CharField 사용
from django.db.models.fields import CharField
### DB에서 숫자값을 관리하는 타입은 IntergerField 사용 
from django.db.models.fields import IntegerField

# Create your models here.

### <클래스가 만들어진 후 매핑 작업 수행하기>
# - python manage.py makemigrations oracleapp
# - python manage.py migrate
# - 최초에 1회만 진행 : 이후 수정 후 그대로 사용 가능
# - 단, 수정 후 반영이 안되는 경우에는 위의 매핑 작업 수행 필요

### 회원정보 테이블 매핑
class Member(models.Model) :
    mem_id = CharField(primary_key=True, max_length=15, null=False)
    mem_pass = CharField(max_length=15, null=False)
    mem_name = CharField(max_length=20, null=False)
    mem_add1 = CharField(max_length=100, null=False)
    
    ### 내부클래스 정의 : 메타클래스
    class Meta :
        ### 실제 DB의 테이블 이름 정의
        db_table = "member"
        
        ### 사용할 app 이름 정의
        app_label = "oracleapp"
        
        ### 외부 DB에 테이블이 존재하는지 여부
        # - 존재하면 : False
        # - 존재하지 않으면 : True
        # - DBMS와 같은 외부 DB서버와 연결할 때는 
        #   일반적으로 DB가 설계됟어 만들어진 상태에서 사용되기에
        #   False로 설정한 후 사용하는 것이 일반적임
        managed = False
        
### 주문정보 테이블 매핑
# - PK가 여러개인 경우에는 여러개 중에 하나만 pk로 정의하면 됩니다.
class Cart(models.Model) :
    cart_no = CharField(primary_key=True, max_length=13, null=False)
    cart_member = CharField(max_length=15, null=False)
    cart_prod = CharField(max_length=10, null=False)
    cart_qty = IntegerField(null=False)
    
    class Meta :
        ### 실제 DB의 테이블 이름 정의
        db_table = "cart"
        
        ### 사용할 app 이름 정의
        app_label = "oracleapp"
        
        ### 외부 DB에 테이블이 존재하는지 여부
        # - 존재하면 : False
        # - 존재하지 않으면 : True
        # - DBMS와 같은 외부 DB서버와 연결할 때는 
        #   일반적으로 DB가 설계됟어 만들어진 상태에서 사용되기에
        #   False로 설정한 후 사용하는 것이 일반적임
        managed = False
        
### 상품분류정보 테이블 매핑
class Lprod(models.Model):
    lprod_gu = CharField(primary_key=True,max_length=4, null=False)
    lprod_id = IntegerField(null=False)
    lprod_nm = CharField(max_length=40, null=False)
    
    class Meta:
        db_table = 'lprod'
        app_label = "oracleapp"
        managed = False
        
### 상품정보 테이블 매핑
class Prod(models.Model) :
    prod_id = CharField(primary_key=True, max_length=10, null=False)
    prod_name = CharField(max_length=40, null=False)
    prod_lgu = CharField(max_length=4, null=False)
    prod_cost = IntegerField(null=False)
    prod_price = IntegerField(null=False)
    prod_sale = IntegerField(null=False)
    
    class Meta :
        db_table = "prod"
        app_label = "oracleapp"
        managed = False
        
        
### 주문정보 테이블 매핑
# - PK가 여러개인 경우에는 여러개 중에 하나만 pk로 정의하면 됩니다.
class CartMember(models.Model) :
    # PK
    cart_no = CharField(primary_key=True, max_length=13, null=False)
    
    # FK
    # cart_member = CharField(max_length=15, null=False)
    ### ForeignKey() : 부모클래스(테이블)와 관계(join) 맺기(연결하기)
    # - 첫번째 값 : 부모 클래스(테이블) 이름
    # - 두번째 값(to_field) : 부모 클래스(테이블)의 PK 변수(컬럼)명 지정
    # - 세번째 값(db_column) : 자식 클래스(테이블)의 FK 변수(컬럼)명 지정
    # - 네번째 값(on_delete) : 부모 클래스(테이블)의 정보 삭제시 허락할 것인지 여부
    #                       : PROTECT -> 자식이 있는 부모 클래스(테이블)의 정보가 삭제될 수 없도록 함
    #                       : CASCADE -> 자식이 있는 부모 클래스(테이블)의 정보가 삭제될 수 있도록 함
    cart_member = models.ForeignKey(Member, to_field="mem_id", db_column="cart_member", on_delete=models.PROTECT)
    
    # FK & PK
    cart_prod = CharField(max_length=10, null=False)
    cart_qty = IntegerField(null=False)
    
    class Meta :
        ### 실제 DB의 테이블 이름 정의
        db_table = "cart"
        
        ### 사용할 app 이름 정의
        app_label = "oracleapp"
        
        ### 외부 DB에 테이블이 존재하는지 여부
        # - 존재하면 : False
        # - 존재하지 않으면 : True
        # - DBMS와 같은 외부 DB서버와 연결할 때는 
        #   일반적으로 DB가 설계됟어 만들어진 상태에서 사용되기에
        #   False로 설정한 후 사용하는 것이 일반적임
        managed = False
        
        
### 주문정보 테이블 매핑
# - PK가 여러개인 경우에는 여러개 중에 하나만 pk로 정의하면 됩니다.
class CartMemberProd(models.Model) :
    # PK
    cart_no = CharField(primary_key=True, max_length=13, null=False)
    
    # FK
    # cart_member = CharField(max_length=15, null=False)
    ### ForeignKey() : 부모클래스(테이블)와 관계(join) 맺기(연결하기)
    # - 첫번째 값 : 부모 클래스(테이블) 이름
    # - 두번째 값(to_field) : 부모 클래스(테이블)의 PK 변수(컬럼)명 지정
    # - 세번째 값(db_column) : 자식 클래스(테이블)의 FK 변수(컬럼)명 지정
    # - 네번째 값(on_delete) : 부모 클래스(테이블)의 정보 삭제시 허락할 것인지 여부
    #                       : PROTECT -> 자식이 있는 부모 클래스(테이블)의 정보가 삭제될 수 없도록 함
    #                       : CASCADE -> 자식이 있는 부모 클래스(테이블)의 정보가 삭제될 수 있도록 함
    cart_member = models.ForeignKey(Member, to_field="mem_id", db_column="cart_member", on_delete=models.PROTECT)
    
    # FK & PK
    # cart_prod = CharField(max_length=10, null=False)
    cart_prod = models.ForeignKey(Prod, to_field="prod_id", db_column="cart_prod", on_delete=models.PROTECT)
    
    cart_qty = IntegerField(null=False)
    
    class Meta :
        ### 실제 DB의 테이블 이름 정의
        db_table = "cart"
        
        ### 사용할 app 이름 정의
        app_label = "oracleapp"
        
        ### 외부 DB에 테이블이 존재하는지 여부
        # - 존재하면 : False
        # - 존재하지 않으면 : True
        # - DBMS와 같은 외부 DB서버와 연결할 때는 
        #   일반적으로 DB가 설계됟어 만들어진 상태에서 사용되기에
        #   False로 설정한 후 사용하는 것이 일반적임
        managed = False