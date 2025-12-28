import unittest
import xmlrunner
from app import app

class TestApp(unittest.TestCase):
    def test_ping(self):
        with app.test_client() as c:
            resp = c.get("/ping")
            self.assertEqual(resp.status_code, 200)
            self.assertEqual(resp.get_data(as_text=True), "pong")

if __name__ == "__main__":
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
