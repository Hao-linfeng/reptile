from urllib.request import urlopen
from bs4 import BeautifulSoup
import run_sql
import pymysql
import re
import time
import datetime
import main


#目标用户
urls = [
    "https://36kr.com/user/1931717417",
    "https://36kr.com/user/1356496270",
    "https://36kr.com/user/1864046570",
    "https://36kr.com/user/14240586",
    "https://36kr.com/user/1452700527",
    "https://36kr.com/user/375349",
    "https://36kr.com/user/1554725818",
    "https://36kr.com/user/1864046570",
    "https://36kr.com/user/1207766167",
    "https://36kr.com/user/980118315",
    "https://36kr.com/user/1195854171",
    "https://36kr.com/user/1005465726",
    "https://36kr.com/user/14880677",
    "https://36kr.com/user/1032552207",	
    "https://36kr.com/user/19881307",	
    "https://36kr.com/user/1466675620",
    "https://36kr.com/user/669723995",
    "https://36kr.com/user/1195854171",
    "https://36kr.com/user/5087265",
    "https://36kr.com/user/167870", ]

#爬取文章内容
def do_article(url):
    try:
        html = urlopen(url)
        bs = BeautifulSoup(html, 'html.parser') 
        article_text = bs.find('div',{'class':'article-wrapper common-width'}).get_text()
    except Exception as e:
        article_text = "error_error"
        print(e)
    return article_text

def do_article_info(url,article,author,describe):
     #爬取文章url
    article_url = article.find('a',{'class':'article-item-title weight-bold'})['href']
    final_url = "https://36kr.com" + article_url
    print(final_url)

    #爬取文章内容
    article_text = do_article(final_url)

    #爬取文章发表时间
    article_time = article.find('span',{'class':'kr-flow-bar-time'}).get_text()


                
    if "小时前" in article_time:
        num = article_time[0]
        num = int(num)
        now = datetime.datetime.now()
        article_time = now + datetime.timedelta(hours = -num)
        article_time = str(article_time)
    if "昨" in article_time:
        now = datetime.datetime.now()
        article_time = now + datetime.timedelta(days = -1)
        article_time = str(article_time)

    print(article_time)
                
    #爬取文章标题
    article_title = article.find('a',{'class':'article-item-title weight-bold'}).get_text().strip()

    print(article_title)

    sql = "INSERT INTO user3 (autorname, url, title, article_text, article_describe, fbtime)VALUES(%s, %s, %s, %s, %s, %s);"
    print(sql)
    run_sql.con(sql, author, final_url, article_title, article_text, describe, article_time)


def do_url(url):

    html = urlopen(url)
    bs = BeautifulSoup(html, 'html.parser') 
    author = bs.find('a', {'class': "author-name ellipsis-1"}).get_text()
    describe = bs.find('span', {'class':"author-role"}).get_text()
    H = bs.find('div',{'class':'author-detail-flow-list'}).children

    for article in H:
        try:
            do_article_info(url, article, author,describe)    
        except Exception as e:
            print(e)
            main.bad_article.append(article)

def run():
    for url in urls:
        try:
            if url not in main.bad_autor:
                do_url(url)
                print("下一个用户")
        except Exception as e:
            print(e)
            main.bad_autor.append(url)

# do_url("https://36kr.com/user/1931717417")

