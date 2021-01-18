import logging

logging.basicConfig(filename = None, # or to a file 'example.log',
                    level = logging.DEBUG,  # Logging levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
                    format = '%(asctime)s.%(msecs)03d - %(name)s - %(levelname)s - %(message)s',
                    datefmt = '%Y-%m-%dT%H:%M:%S')

logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')

logging.error('Watch out!')    # will print a message to the console

logging.critical('ERROR!!!!!')