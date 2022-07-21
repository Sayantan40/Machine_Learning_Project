## Importing the necessary liraries / modules

import os
import sys


## Creating our own custom class "HousingException" with Exception being the Parent class.
class HousingException(Exception):

    # defining a constructor/initializer
    def __init__(self, error_message:Exception , error_detail:sys):
    

        super().__init__(error_message) ## passing the error_message to Exception class like Exception(error_message).
        self.error_message = HousingException.get_detailed_error_message(error_message=error_message,error_detail=error_detail)
        pass


    @staticmethod
    def get_detailed_error_message(error_message:Exception , error_detail:sys)->str:

        """
        error_message : object of Exception
        error_message gives the type of the error.
        error_detail : object of sys module.
        error_details gives the well detail information of the error like which line is causing error,
        which file is causing the error.

        """
        
        ## the reason for the @staticmethod is that we dont want to use any object to call this function,
        ## we can directly use the class name "HousingException"


        ## returns most exception caught by except clause in tuple format
        _,_ ,exec_tb = error_detail.exc_info()

        ## the underscore _ parts we dont need basically they are type and value
        ## we only need trackback

        exception_block_line_number = exec_tb.tb_frame.f_lineno
        ## gives the line number which causing the error

        try_block_line_number = exec_tb.tb_lineno

        file_name = exec_tb.tb_frame.f_code.co_filename
        ## gives the name of the file causing the error

        error_message = f"""Error occurred in script: [ {file_name} ] at try block line number: [ {try_block_line_number} ] 
                            and then exception block line number: [ {exception_block_line_number} ] 
                            error message : [ {error_message} ]"""
        ## the variable holding the error message and error details



        return error_message


    def __str__(self) :
        return self.error_message

    ## __str__(self) whenever we try to print the object of the class(any class),
    ## what information should be displayed in the print statement that we can define in  __str__(self) method.



    def __repr__(self) -> str:
        return HousingException.__name__.str()



