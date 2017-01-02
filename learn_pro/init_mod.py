'''
desc: 用于集中初始化需要初始化的模块,放入中间件的最前面处理
'''
import sys
import logging

logging.config.fileConfig("log.conf")
logger = logging.getLogger("qzMasterLogger")

def process_request(request):
    '''
    :param request:
    :return: none
    '''
    logger.info("logger init...")

    return None

