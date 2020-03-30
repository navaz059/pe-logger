import os
class Logger():
    def __init__(self, **kwargs):
        self.datetime_format=kwargs.pop('ts_format')
        self.level=kwargs.pop('log_level')
        self.sink_type=kwargs.pop('sink_type')
        self.filename=kwargs.pop('filename')
        self.thread_model=kwargs.pop('thread_model') if kwargs.get('thread_model') is not None else 'SYNC',
        self.write_mode=kwargs.pop('write_mode') if kwargs.get('write_mode') is not None else 'SINGLE'
    
    def write(self, msg, time):
        
        fomattted_msg = "{time}-{level}-{msg}".format(
            level=self.level, 
            time=time.strftime(self.datetime_format), 
            msg=msg
        )

        with open(self.filename, os.O_RDWR|os.O_CREAT) as f:
            f.write(fomattted_msg + os.linesep)
            f.close()

    def is_sync():
        return True if self.thread_model == 'SYNC' else False

    def is_single_threaded():
        return True if self.thread_model == "SINGLE" else False            