import cx_Oracle

def cart_List() :
    dsn = cx_Oracle.makedsn('localhost', 1521, 'xe')
    conn = cx_Oracle.connect('busan', 'dbdb', dsn)
    cursor = conn.cursor()
    
    ### SQL 요청 및 응답 결과 받아오기
    sql = """select cart_no, cart_member, cart_prod, cart_qty
         from cart
         order by cart_no DESC
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