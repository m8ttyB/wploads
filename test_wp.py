from loads.case import TestCase

class TestWP(TestCase):

	def test_root_blog(self):
		res = self.session.get('https://blog-dev.allizom.org/')
		self.assertEqual(res.status_code, 200)

	def test_webqa_blog(self):
		res = self.session.get('https://blog-dev.allizom.org/webqa/')
		self.assertEqual(res.status_code, 200)

	def test_rss_feeds_root(self):
		res = self.session.get('https://blog-dev.allizom.org/feed/')
		self.assertEqual(res.status_code, 200)

	def test_viewing_post(self):
		res = self.session.get('https://blog-dev.allizom.org/blog/2014/07/28/chris-beard-named-ceo-of-mozilla/')
		self.assertEqual(res.status_code, 200)

	def test_negative_search(self):
		res = self.session.get('https://blog-dev.allizom.org/?s=orcs')
		self.assertEqual(res.status_code, 200)

	def test_positive_search(self):
		res = self.session.get('https://blog-dev.allizom.org/?s=beard')
		self.assertEqual(res.status_code, 200)		

