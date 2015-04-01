#!/usr/bin/env python

import cgi
import blogtools

query = cgi.FieldStorage()
email = str(query.getvalue('email'))
post = int(query.getvalue('post'))

	try:
	blogtools.postlist[post][4].remove(email)
	blogtools.save()
except ValueError:
	pass

print "Content-Type: text/html"
print 
print "<html><head><title>Unsubscribed</title></head><body>If you were subscribed to that post, you aren't any more.</body></html>"
