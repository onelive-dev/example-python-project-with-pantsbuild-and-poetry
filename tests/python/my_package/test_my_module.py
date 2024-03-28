# tests/python/my_package/test_my_module.py

from src.python.my_package.my_module import say_hello

def test_say_hello():
    assert say_hello("World") == "Hello, World!"
