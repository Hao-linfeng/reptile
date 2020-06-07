import pymysql

# 连接database
#执行sql语句
def con(sql, autorname, url, title, article_text, article_describe, fbtime):
    conn = pymysql.connect(host='localhost', user='root',password='保密',database='interview',charset='utf8')
  
    # 得到一个可以执行SQL语句的光标对象
    cursor = conn.cursor()
 
    # 执行SQL语句
    res = cursor.execute(sql, (autorname, url, title, article_text, article_describe, fbtime))
 
    # 关闭光标对象
    cursor.close()
  
    #提交
    conn.commit()
 
    # 关闭数据库连接
    conn.close()

    # 返回数据
    return res


