import unittest
from microdot import URLPattern


class TestURLPattern(unittest.TestCase):
    def test_static(self):
        p = URLPattern('/')
        self.assertEqual(p.match('/'), {})
        self.assertIsNone(p.match('/foo'))

        p = URLPattern('/foo/bar')
        self.assertEqual(p.match('/foo/bar'), {})
        self.assertIsNone(p.match('/foo'))
        self.assertIsNone(p.match('/foo/bar/'))

        p = URLPattern('/foo//bar/baz/')
        self.assertEqual(p.match('/foo//bar/baz/'), {})
        self.assertIsNone(p.match('/foo/bar/baz/'))
        self.assertIsNone(p.match('/foo'))
        self.assertIsNone(p.match('/foo/bar/baz'))

    def test_string_argument(self):
        p = URLPattern('/<arg>')
        self.assertEqual(p.match('/foo'), {'arg': 'foo'})
        self.assertIsNone(p.match('/'))
        self.assertIsNone(p.match('/foo/'))

        p = URLPattern('/<arg>/')
        self.assertEqual(p.match('/foo/'), {'arg': 'foo'})
        self.assertIsNone(p.match('/'))
        self.assertIsNone(p.match('/foo'))

        p = URLPattern('/<string:arg>')
        self.assertEqual(p.match('/foo'), {'arg': 'foo'})
        self.assertIsNone(p.match('/'))
        self.assertIsNone(p.match('/foo/'))

        p = URLPattern('/<string:arg>/')
        self.assertEqual(p.match('/foo/'), {'arg': 'foo'})
        self.assertIsNone(p.match('/'))
        self.assertIsNone(p.match('/foo'))

        p = URLPattern('/foo/<arg1>/bar/<arg2>')
        self.assertEqual(p.match('/foo/one/bar/two'),
                         {'arg1': 'one', 'arg2': 'two'})
        self.assertIsNone(p.match('/'))
        self.assertIsNone(p.match('/foo/'))

    def test_int_argument(self):
        p = URLPattern('/users/<int:id>')
        self.assertEqual(p.match('/users/123'), {'id': 123})
        self.assertIsNone(p.match('/users/'))
        self.assertIsNone(p.match('/users/abc'))
        self.assertIsNone(p.match('/users/123abc'))
        self.assertIsNone(p.match('/users/123/abc'))

        p = URLPattern('/users/<int:id>/<int:id2>/')
        self.assertEqual(p.match('/users/123/456/'), {'id': 123, 'id2': 456})
        self.assertEqual(p.match('/users/123/-456/'), {'id': 123, 'id2': -456})
        self.assertIsNone(p.match('/users/'))
        self.assertIsNone(p.match('/users/123/-456'))
        self.assertIsNone(p.match('/users/123/abc/'))
        self.assertIsNone(p.match('/users/123/-456/abc'))
        self.assertIsNone(p.match('/users/--123/456/'))

    def test_path_argument(self):
        p = URLPattern('/users/<path:path>')
        self.assertEqual(p.match('/users/123'), {'path': '123'})
        self.assertEqual(p.match('/users/123/'), {'path': '123/'})
        self.assertEqual(p.match('/users/abc/def'), {'path': 'abc/def'})
        self.assertIsNone(p.match('/users/'))

        p = URLPattern('/users/<path:path>/foo')
        self.assertEqual(p.match('/users/123/foo'), {'path': '123'})
        self.assertEqual(p.match('/users/foo/foo'), {'path': 'foo'})
        self.assertEqual(p.match('/users/abc/def/foo'), {'path': 'abc/def'})
        self.assertIsNone(p.match('/users/'))
        self.assertIsNone(p.match('/users/foo'))
        self.assertIsNone(p.match('/users/foo/'))

    def test_regex_argument(self):
        p = URLPattern('/users/<re:[a-c]+:id>')
        self.assertEqual(p.match('/users/ab'), {'id': 'ab'})
        self.assertEqual(p.match('/users/bca'), {'id': 'bca'})
        self.assertIsNone(p.match('/users/abcd'))

    def test_many_arguments(self):
        p = URLPattern('/foo/<path:path>/<int:id>/bar/<name>')
        self.assertEqual(p.match('/foo/abc/def/123/bar/test'),
                         {'path': 'abc/def', 'id': 123, 'name': 'test'})
        self.assertIsNone(p.match('/foo/123/bar/test'))
        self.assertIsNone(p.match('/foo/abc/def/ghi/bar/test'))
        self.assertIsNone(p.match('/foo/abc/def/123/bar'))
        self.assertIsNone(p.match('/foo/abc/def/123/bar/'))
        self.assertIsNone(p.match('/foo/abc/def/123/test'))

    def test_invalid_url_patterns(self):
        self.assertRaises(ValueError, URLPattern, '/users/<foo/bar')
        self.assertRaises(ValueError, URLPattern, '/users/<badtype:id>')
