import unittest 
from myBlog.models import AddArticle, Post

class TestBackgroundTask(unittest.TestCase):
    def test_remove_old_article(self):
        AddArticle.old_articles()
        self.assertFalse(AddArticle.objects.filter(title="Modern Education: Challenges and Innovations").exists())

if __name__ == '__main__': 
    unittest.main() 