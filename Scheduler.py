import time
import schedule
from bot.py import job 

#schedule.every().tuesday.at("11:25").do(job)
schedule.every(1).second.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)