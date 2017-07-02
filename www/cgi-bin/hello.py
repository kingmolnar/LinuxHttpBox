#!/usr/bin/env python
import os
print "Content-type: text/html"
print
print "<h1>This is a CGI</h1>"
print "<pre>"
args = os.getenv('QUERY_STRING').split('&')
for a in args:
	print a
print "</pre>"

