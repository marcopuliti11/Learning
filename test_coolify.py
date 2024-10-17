import unittest
import coolify as cl

class Test_coolify(unittest.TestCase):
    def test_name(self):
        test = "marco"
        self.assertTrue(cl.coolify(test) == "marco is cool")
        self.assertFalse(cl.coolify(test) == "marco")
        
if __name__ == "__main__":
    unittest.main()   