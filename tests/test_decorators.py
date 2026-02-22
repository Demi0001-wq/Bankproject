import unittest
import os
from src.decorators import log

@log(filename="test_log.txt")
def add(x, y):
    return x + y

@log()
def greet(name):
    return f"Hello, {name}"

@log(filename="test_log.txt")
def fail_func():
    raise ValueError("Expected fail")

class TestDecorators(unittest.TestCase):
    def test_log_to_file(self):
        if os.path.exists("test_log.txt"):
            os.remove("test_log.txt")
            
        add(1, 2)
        self.assertTrue(os.path.exists("test_log.txt"))
        with open("test_log.txt") as f:
            content = f.read()
            self.assertIn("add ok", content)
            
    def test_log_error_to_file(self):
        if os.path.exists("test_log.txt"):
            os.remove("test_log.txt")
            
        with self.assertRaises(ValueError):
            fail_func()
            
        self.assertTrue(os.path.exists("test_log.txt"))
        with open("test_log.txt") as f:
            content = f.read()
            self.assertIn("fail_func error: ValueError", content)

    def test_log_to_console(self):
        # Simply calling it to check it doesn't crash console
        # In a real scenario we might capture stdout
        self.assertEqual(greet("Alice"), "Hello, Alice")
