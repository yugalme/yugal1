import logging

logging.basicConfig(level=logging.WARNING)

logger = logging.getLogger('hello')
a=[]
try:
    a[1]
except Exception as e:
    logger.exception(e)
