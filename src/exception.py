import sys 

def error_massage_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    FileExistsError = exc_tb.tb_frame.f_code.co_filename
    errror_massage = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        FileExistsError, exc_tb.tb_lineno, str(error)
    )
    class CustomException(Exception):
        def __init__(self,error_message , error_detail:sys):
            super().__init__(error_message)
            self.error_message = error_massage_detail(error_message,detail=error_detail)
        def __str__(self):
            return self.error_message 
