from logger import Logger
from datetime import datetime
import configparser

if __name__ == '__main__':
    filename = 'logger_config.ini'
    cp = configparser.ConfigParser()
    cp.read(filename)
    print(cp['ts_format'])

    pe_logger = Logger(
        ts_format='%Y-%m-%d',
        log_level='INFO',
        sink_type='file',
        filename='app.log', 
        thread_model=None,
        write_mode=None
    )

    pe_logger.write('This is a 1st message', datetime.now())
    pe_logger.write('This is a 2nd message', datetime.now())
    pe_logger.write('This is a 3rd message', datetime.now())
    pe_logger.write('This is a 4th message', datetime.now())
    pe_logger.write('This is a 5th message', datetime.now())
    pe_logger.write('This is a 6th message', datetime.now())