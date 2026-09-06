import subprocess
import sys
import unittest


class HelloScriptTest(unittest.TestCase):
    def test_prints_hello_world(self):
        result = subprocess.run(
            [sys.executable, "hello.py"],
            capture_output=True,
            text=True,
            check=True,
        )

        self.assertEqual(result.stdout, "Hello, world!\n")


if __name__ == "__main__":
    unittest.main()
