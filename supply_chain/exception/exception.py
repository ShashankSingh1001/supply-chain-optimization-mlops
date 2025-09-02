import sys
from supply_chain.logging.logger import logging


class SupplyChainException(Exception):
    """
    Custom exception class for the Supply Chain project.
    Provides detailed error messages with filename and line number.
    """

    def __init__(self, error_message: str, error_detail: sys):
        super().__init__(error_message)
        self.error_message = SupplyChainException.get_detailed_error_message(
            error_message, error_detail
        )
        logging.error(self.error_message)

    @staticmethod
    def get_detailed_error_message(error_message: str, error_detail: sys) -> str:
        """
        Returns a detailed error string including filename and line number.
        """
        _, _, exc_tb = error_detail.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno

        return (
            f"Error occurred in file [{file_name}] "
            f"at line [{line_number}] : {error_message}"
        )

    def __str__(self):
        return self.error_message
