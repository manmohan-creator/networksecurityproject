import sys
from networksecurity.logging import logger

class NetworkSecurityException(Exception):

    def error_message_detail(self, error_message, error_details: sys):
        self.error_message = error_message
        _, _, exc_tb = error_details.exc_info()
        self.file_name = exc_tb.tb_frame.f_code.co_filename
        self.lineno = exc_tb.tb_lineno

    def __str__(self):
        return "Error occurred in script: {file_name} at line {lineno} -> {str(error)}"
        self.file_name, self.lineno, str(self.error_message)



