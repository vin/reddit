#!/usr/bin/python

import unittest
import markdown

class MarkdownEscapingTest(unittest.TestCase):
    def setUp(self):
        self.md = markdown._Markdown()

    def testBasicEscaping(self):
        self.roundtrip("foo")
        self.roundtrip('<a href="foo">bar</a>')
        self.roundtrip('<a<b><c<d>>>>')
        self.roundtrip('<?a?>')
        self.roundtrip('[a]')
        self.roundtrip('<')
        self.roundtrip('>?!(*(&')

    def testEscapeTableChars(self):
        for value in self.md.escapetable.values():
            self.roundtrip('<a%s>' % value)

    def roundtrip(self, s):
        escaped = self.md._EscapeSpecialChars(s)
        unescaped = self.md._UnescapeSpecialChars(escaped)
        self.assertEquals(s, unescaped)

if __name__ == '__main__':
    unittest.main()
