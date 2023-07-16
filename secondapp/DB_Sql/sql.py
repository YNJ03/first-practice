import cx_Oracle

def getMem_List() :
    ### 드라이버 연결
    dsn = cx_Oracle.makedsn('localhost', 1521, 'xe')
    
    ### DB 접속
    conn = cx_Oracle.connect('busan', 'dbdb', dsn)
    
    ### 커서 생성
    cursor = conn.cursor()
    
    ### SQL 요청 및 응답 결과 받아오기
    sql = """select 
            mem_id, mem_name, extract(year from sysdate) - extract(year from mem_bir) as age, to_char(mem_bir, 'yyyy-mm-dd') as mem_bir
            from member
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