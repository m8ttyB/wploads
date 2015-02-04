from loads.case import TestCase

class TestWP(TestCase):

	server_url = 'https://blog-dev.allizom.org'

	def test_root_blog(self):
		res = self.session.get(self.server_url)
		self.assertEqual(res.status_code, 200)

	def test_viewing_beard_post_root_blog(self):
		res = self.session.get(self.server_url + '/blog/2014/07/28/chris-beard-named-ceo-of-mozilla/')
		self.assertEqual(res.status_code, 200)

	def test_viewing_yahoo_post_root_blog(self):
		res = self.session.get(self.server_url + '/press/2014/11/yahoo-and-mozilla-form-strategic-partnership/')
		self.assertEqual(res.status_code, 200)

	def test_negative_search_root_blog(self):
		res = self.session.get(self.server_url + '/?s=orcs')
		self.assertEqual(res.status_code, 200)

	def test_positive_beard_search_root_blog(self):
		res = self.session.get(self.server_url + '/?s=beard')
		self.assertEqual(res.status_code, 200)

	def test_postitive_yahoo_search_press_blog(self):
		res = self.session.get(self.server_url + '/press/?s=Yahoo')
		self.assertEqual(res.status_code, 200)

	def test_rss_feeds_root(self):
		res = self.session.get(self.server_url + '/feed/')
		self.assertEqual(res.status_code, 200)

	def test_ux_blog(self):
		res = self.session.get(self.server_url + '/ux/')
		self.assertEqual(res.status_code, 200)

	def test_planet_blog(self):
		res = self.session.get(self.server_url + '/planet/')
		self.assertEqual(res.status_code, 200)

	def test_webqa_blog(self):
		res = self.session.get(self.server_url + '/webqa/')
		self.assertEqual(res.status_code, 200)

	def test_webqa_mbrandt_file_image(self):
		res = self.session.get(self.server_url + '/webqa/files/2015/01/mbrandt.jpg')
		self.assertEqual(res.status_code, 200)

	def test_webdev_blog(self):
		res = self.session.get(self.server_url + '/webdev/')
		self.assertEqual(res.status_code, 200)

	def test_sumo_blog(self):
		res = self.session.get(self.server_url + '/sumo/')
		self.assertEqual(res.status_code, 200)

	def test_press_blog(self):
		res = self.session.get(self.server_url + '/press/')
		self.assertEqual(res.status_code, 200)

	def test_openstandards_blog(self):
		res = self.session.get(self.server_url + '/openstandard-en/')
		self.assertEqual(res.status_code, 200)

	def test_positive_search_javascript_hacks_blog(self):
		res = self.session.get('https://hacks-dev.allizom.org/?s=javascript')
		self.assertEqual(res.status_code, 200)

