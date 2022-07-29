import logging

logging.basicConfig(filename="testlog3.log", level=logging.INFO, format='%(levelname)s %(asctime)s %(message)s')


def div(a, b):
    logging.info("Number entered by user %s %s ",a,b)
    return a / b


print(div(10, 10))
