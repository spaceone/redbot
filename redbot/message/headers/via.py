#!/usr/bin/env python

__author__ = "Mark Nottingham <mnot@mnot.net>"
__copyright__ = """\
Copyright (c) 2008-2013 Mark Nottingham

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""


import redbot.speak as rs
from redbot.message import headers as rh
from redbot.message import http_syntax as syntax


@rh.GenericHeaderSyntax
@rh.CheckFieldSyntax(
    r'(?:%s/)?%s\s+[^,\s]+(?:\s+%s)?' % (
      syntax.TOKEN, syntax.TOKEN, syntax.COMMENT),
    rh.rfc2616 % "section-14.45")
def parse(subject, value, red):
    return value
    
def join(subject, values, red):
    via_list = u"<ul>" + u"\n".join(
           [u"<li><code>%s</code></li>" % v for v in values]
                       ) + u"</ul>"
    red.add_note(subject, rs.VIA_PRESENT, via_list=via_list)
    