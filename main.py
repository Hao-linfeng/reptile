import run_sql
import pa
import time, threading
import stop

#标记爬取出现异常的页面
bad_article = []
bad_autor = []


def main():
    while True:
        try:
            pa.run()
        except Exception as e:
            print("kill")
            print(e)
            stop.stop_thread(t1)

        time.sleep(60*60)


if __name__ == '__main__':
    t1 = threading.Thread(target=main, args=())
    t1.start()

    while True:
        time.sleep(3)
        if not t1.is_alive():
            t1 = threading.Thread(target=main, args=())
            t1.start()




