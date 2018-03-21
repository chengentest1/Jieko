from logbook import Logger, StreamHandler, TimedRotatingFileHandler

import sys

import os

StreamHandler(sys.stdout).push_application()

log = Logger('Logbook')

log.info('Hello, World!')


LOG_DIR = os.path.join('log')

if not os.path.exists(LOG_DIR):

    os.makedirs(LOG_DIR)

TimedRotatingFileHandler(os.path.join(LOG_DIR, '%s.log' % 'user_log'), date_format='%Y%m%d', bubble=True).push_application()

user_log = Logger('user_log')

user_log.info('user_log mytest....')
