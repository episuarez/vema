import unittest

from vema.src.page import Page

class Page_tests(unittest.TestCase):
    def test_md(self):
        page = Page("pages/example.md");
        self.assertGreaterEqual(len(page.properties), 3);
        self.assertGreater(len(page.content), 5);

    def test_html(self):
        Page("pages/index.html");

if __name__ == "__main__":
    unittest.main();