import requests
import logging
import schedule
import time

from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger("Rotating Log")
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger.setLevel(logging.INFO)

handler = TimedRotatingFileHandler("healthcheck.log",
                                   when="d",
                                   interval=1,
                                   backupCount=5)
handler.setFormatter(formatter)
logger.addHandler(handler)


def invoke_healthcheck():
    try:
        appname = "helloservice"
        r = requests.get("http://localhost:8080/actuator/health")
        print(r.content)
        print(r.status_code)
    except:
        logger.info("Exception occurred in %s", appname)


schedule.every().minute.do(invoke_healthcheck)

while 1:
    schedule.run_pending()
    time.sleep(1)
