'''
1 需求
    1)需要将所有级别的日志都写在磁盘文件中
    2)all.log文件中记录所有日志信息 日志格式：日期和时间 - 日志级别 - 日志信息
    3)error.log文件中单独记录error及以上级别的日志信息，格式：日期和时间 - 日志级别 - 文件名[: 行号] - 日志信息
    4)all.log每天凌晨进行日志切割
2 分析
    1)日志器的有效level需要设置为最低级别 -- DEBUG；
    2)日志被发送到两个不同的目的地，因此 需要为日志器设置两个handler;另外，两个目的地都是磁盘文件，因此这两个handler都是与FileHandler相关的；
    3)all.log要求按照时间进行日志切割，因此需要用logging.handlers.TimedRotatingFileHandler;而error.log没有要求日志切割，因此可以使用FileHandler;
    4)两个日志文件的格式不同，需要对两个handler分别设置格式器

'''
import logging
import logging.handlers
import datetime

#定义logger
logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)
#when=midnight和interval表示每隔一天的午夜,backupCount决定留几个日志文件，0表示全留,datetime.time(0,0,0,0)
#为两个不同的文件设置不同的handler
rf_handler = logging.handlers.TimedRotatingFileHandler('all.log', when='midnight', interval=1, backupCount=7, atTime=datetime.time(0, 0, 0, 0))
rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))



f_handler = logging.FileHandler('error.log')
f_handler.setLevel(logging.ERROR)
f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

# 把相应的处理器组装到logger上
logger.addHandler(rf_handler)
logger.addHandler(f_handler)


logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')