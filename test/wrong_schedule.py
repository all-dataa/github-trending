import datetime
import schedule
import time
import pytz


def daily_task():
    print('hello')

if __name__ == '__main__':
    try:
        beijing_tz = pytz.timezone('Asia/Shanghai')
        now = datetime.datetime.now(beijing_tz)

        schedule.every().day.at("23:40", beijing_tz).do(daily_task)

        while True:
            schedule.run_pending()
            time.sleep(1)
    except Exception as e:
        print(f"{e} occured~")
