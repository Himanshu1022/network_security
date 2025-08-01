import sys
from Networksecurity.logging import logger
class NetworkSecurityException(Exception):
    def __init__(self,error_message,error_detailed:sys):
        self.error_message = error_message
        _,_,exc_tb = error_detailed.exc_info()

        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return "error uccured in python script name[{0}] line number [{1}] error message [{2}]".format(self.file_name,self.lineno,str(self.error_message))
    
if __name__ == "__main__":
    try:
        logger.logging.info("enter the try block")
        a = 1/0
        print("this will not printed ",a)
    except Exception as e:
        raise NetworkSecurityException(e,sys)