from logbook import Logger,StreamHandler
import sys
handler=StreamHandler(sys.stdout)
handler.push_application()
log=Logger('test')
def main():
    log.info('something logging')

if __name__=='__main__':
    main()
    