import logging

logging.basicConfig(filename="testlog.log", level=logging.INFO)

logging.info("This is test logging code")
logging.warning("This is test warning")
logging.error("This is test error msg")

lst = [1, 2, 3, 4, 5]

for i in lst:
    if i == 2:
        logging.info(i)
        logging.warning("2 found in list")
