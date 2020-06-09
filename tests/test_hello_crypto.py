"""Unit tests for the hello_crypto module."""

from hello_crypto import hello_crypto_def
import pytest

def test_function_1():
    assert hello_crypto_def.hello_crypto_world() == "hello_crypto_world"

def test_function_2():
    assert hello_crypto_def.add_crypto(3,2) == 5
