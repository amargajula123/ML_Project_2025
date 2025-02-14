import os
import sys

class HosingException(Exception):
    def __init__(self,error_massage:Exception,error_detail:sys):
        super().__init__(error_massage)
        self.error_massage=HosingException.get_detailed_error_message(error_massage=error_massage,
                                                                      error_detail=error_detail)

    @staticmethod
    def get_detailed_error_message(error_massage:Exception,error_detail:sys)->str:
        """
        error_massage: Exception object
        error_detail: object of sys module
        """
        _,_,exec_tb = error_detail.exc_info()
        file_number=exec_tb.tb_frame.f_lineno
        file_name = exec_tb.tb_frame.f_code.co_filename

        error_massage = f"Error occured in scrip: [{file_name}] at line number : [{file_number}]\
        error message:[{error_massage}]"

        return error_massage
    
    def __str__(self):
        return self.error_message


    def __repr__(self) -> str:
        return HousingException.__name__.str()