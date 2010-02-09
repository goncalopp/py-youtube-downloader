#!/usr/bin/env python
# encoding: utf-8

def assertEqual(x, y):
    assert x == y, "%r not equal to %r"

import youtube as y
def test_getPageToken():
    """Tests pageToken method returns sensible string
    """
    token = y.Youtube("QkzCi5mHvkc").pageToken()
    assert isinstance(token, basestring)
    assert len(token) > 0, "Token was zero length"

def test_getPageTitle():
    """Tests retrieval of page title
    """
    title = y.Youtube("QkzCi5mHvkc").title()
    assertEqual(title, "65daysofstatic - radio protector")

if __name__ == '__main__':
    import nose
    nose.main()