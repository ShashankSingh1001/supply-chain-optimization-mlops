import sys
import pytest
from supply_chain.exception.exception import SupplyChainException


def test_custom_exception_message():
    """Check if SupplyChainException generates correct error message."""
    try:
        raise ValueError("Test error")
    except ValueError as e:
        custom_exception = SupplyChainException(str(e), sys)
        error_message = str(custom_exception)

        assert "Test error" in error_message
        assert "Error occurred in file" in error_message
        assert "at line" in error_message


def test_exception_str_representation():
    """Check __str__ method returns detailed message."""
    try:
        1 / 0
    except Exception as e:
        custom_exception = SupplyChainException(str(e), sys)
        assert str(custom_exception) == custom_exception.error_message
