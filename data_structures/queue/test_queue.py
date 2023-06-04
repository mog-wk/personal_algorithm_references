import unittest
import queue as qu

# python -m unittest <name>

class TestQueue(unittest.TestCase):

    def test_peek(self):
        q1 = qu.Queue([1, 2, 3, 4, 5])
        self.assertEqual(q1.peek, 5)

    def test_dequeue():




f __name__ == "__main__":
    unittest.main()

