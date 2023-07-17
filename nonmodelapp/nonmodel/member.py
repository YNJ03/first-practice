import cx_Oracle

### 회원 로그인 처리에 사용
def getLoginChk(mem_id, mem_pass) :
    dsn = cx_Oracle.makedsn('localhost', 1521, 'xe')
    conn = cx_Oracle.connect('busan', 'dbdb', dsn)
    cursor = conn.cursor()
    
    ### SQL 요청 및 응답 결과 받아오기
    sql = """select mem_id, mem_pass, mem_name
             from member
             where mem_id = '{}' and mem_pass = '{}'
        """.format(mem_id, mem_pass)
        
    cursor.execute(sql)
    
    ### ('a001', '1357', '김은대')
    row = cursor.fetchone()
    
    ### 조회 결과가 없으면 아래 처리 안하고 return 시키기
    # - 회원정보가 없는 회원으로 판단하기
    if row == None :
        cursor.close()
        conn.close()
        
        return {"result" : "None"}
    
    ### 컬럼 데이터 추출하기
    colnames = cursor.description
    cols_list = [colnames[i][0].lower() for i in range(len(colnames))]
    
    ### DB 접속 끊기
    cursor.close()
    conn.close()

    ### 딕셔너리 형태로 변환하기
    # {'mem_id' : 'a001', 'mem_pass' : '1357', 'mem_name' : '김은대'} 
    dict_row = {}
    for i in range(len(cols_list)) :
        dict_row[cols_list[i]] = row[i]

    return dict_row   