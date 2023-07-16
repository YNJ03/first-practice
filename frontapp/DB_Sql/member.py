import cx_Oracle

def testData() :
    return "홍길동"

def mem_List() :
    ### 드라이버 연결
    dsn = cx_Oracle.makedsn('localhost', 1521, 'xe')
    
    ### DB 접속
    conn = cx_Oracle.connect('busan', 'dbdb', dsn)
    
    ### 커서 생성
    cursor = conn.cursor()
    
    ### SQL 요청 및 응답 결과 받아오기
    sql = """select Distinct mem_name, to_char(to_date(substr(cart_no,1,8),'yyyy-mm-dd'),'yyyy-mm-dd') as cart_no, prod_name
         from member, cart, prod
         where mem_id = cart_member and cart_prod = prod_id and
         prod_name like '%컴퓨터%'
         order by mem_name ASC
        """
    cursor.execute(sql)
    
    ### 결과 출력
    rows = cursor.fetchall()
    colnames = cursor.description
    cols_list = [colnames[i][0].lower() for i in range(len(colnames))]
    
    ### DB 접속 끊기
    cursor.close()
    conn.close()

    list_dict = []
    for row in rows :
        temp_dict = {}
        for i in range(len(cols_list)) :
            temp_dict[cols_list[i]] = row[i]
        
        list_dict.append(temp_dict)

    return list_dict   