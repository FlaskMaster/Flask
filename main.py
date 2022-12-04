import time
import schedule

def job():
    print("Я повторяюсь каждые 2 секунды")

schedule.every(2).seconds.do(job)


def job2():
    print("Я повторяюсь каждую минуту")
  
schedule.every(1).minutes.do(job2)

def job3():
    print("Я повторяюсь каждый день в 12:00")
  
schedule.every().day.at("12:00").do(job3)



while True:
    schedule.run_pending()
    # Эта задержка влияет только на точность запуска задач.
    time.sleep(2)