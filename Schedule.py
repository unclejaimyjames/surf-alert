
# https://schedule.readthedocs.io/en/stable/

import schedule
import time

def job():
    print("Test")

schedule.every().day.at("12:30").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)


