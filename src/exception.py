import sys
import logging

logging.basicConfig(
    format="[ %(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in Python script [{0}] name line number [{1}] error message[{2}]".format(file_name,exc_tb.tb_lineno,str(error))
    return error_message

class CustomException(Exception):
    def __init__(self,error,error_detail:sys):
        super().__init__(str(error))
        self.error_message=error_message_detail(error,error_detail=error_detail)

    def __str__(self):
        return self.error_message
    
if __name__ == "__main__":
    try:
        a = 1/0
    except Exception as e:
        logging.info("Divide by zero error")
        raise CustomException(e,sys)