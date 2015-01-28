from loads.case import TestCase

class TestWP(TestCase):

	def test_root_blog(self):
		res = self.session.get('https://blog-dev.allizom.org/')
		self.assertEqual(res.status_code, 200)

	def test_viewing_beard_post_root_blog(self):
		res = self.session.get('https://blog-dev.allizom.org/blog/2014/07/28/chris-beard-named-ceo-of-mozilla/')
		self.assertEqual(res.status_code, 200)

	def test_viewing_yahoo_post_root_blog(self):
		res = self.session.get('https://blog-dev.allizom.org/press/2014/11/yahoo-and-mozilla-form-strategic-partnership/')
		self.assertEqual(res.status_code, 200)

	def test_negative_search(self):
		res = self.session.get('https://blog-dev.allizom.org/?s=orcs')
		self.assertEqual(res.status_code, 200)

	def test_positive_beard_search_root_blog(self):
		res = self.session.get('https://blog-dev.allizom.org/?s=beard')
		self.assertEqual(res.status_code, 200)

	def test_postitive_yahoo_search_root_blog(self):
		res = self.session.get('https://blog-dev.allizom.org/press/?s=Yahoo')
		self.assertEqual(res.status_code, 200)

	def test_rss_feeds_root(self):
		res = self.session.get('https://blog-dev.allizom.org/feed/')
		self.assertEqual(res.status_code, 200)

	def test_ux_blog(self):
		res = self.session.get('https://blog-dev.allizom.org/ux/')
		self.assertEqual(res.status_code, 200)

	def test_planet_blog(self):
		res = self.session.get('https://blog-dev.allizom.org/planet/')
		self.assertEqual(res.status_code, 200)

	def test_webqa_blog(self):
		res = self.session.get('https://blog-dev.allizom.org/webqa/')
		self.assertEqual(res.status_code, 200)

	def test_webqa_mbrandt_file_image(self):
		res = self.session.get('https://blog-dev.allizom.org/webqa/files/2015/01/mbrandt.jpg')
		self.assertEqual(res.status_code, 200)

	def test_webdev_blog(self):
		res = self.session.get('https://blog-dev.allizom.org/webdev/')
		self.assertEqual(res.status_code, 200)

	def test_sumo_blog(self):
		res = self.session.get('https://blog-dev.allizom.org/sumo/')
		self.assertEqual(res.status_code, 200)

	def test_press_blog(self):
		res = self.session.get('https://blog-dev.allizom.org/press/')
		self.assertEqual(res.status_code, 200)

	def test_openstandards_blog(self):
		res = self.session.get('https://blog-dev.allizom.org/openstandard-en/')
		self.assertEqual(res.status_code, 200)

	def test_positive_search_javascript_hacks_blog(self):
		res = self.session.get('https://hacks-dev.allizom.org/?s=javascript')
		self.assertEqual(res.status_code, 200)

