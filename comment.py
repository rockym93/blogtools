#!/usr/bin/env python
print "Content-Type: text/html"
print

import cgi
import cgitb
cgitb.enable()
import time
import yaml
import blogtools
import markdown
import io

form = cgi.FieldStorage()
if form.getvalue("captcha") == blogtools.config['captcha']:
	
	timestamp = int(time.time())
	author = form.getvalue("username")
	parent = int(form.getvalue("id"))
	email = form.getvalue("email")	
	
	blogtools.postlist[parent][3].append((timestamp,author))
	
	content = form.getvalue("comment")
	content = markdown.markdown(content.decode("utf-8"),safe_mode='escape')
	
	txtfile = io.open(blogtools.postlist[parent][2] + "." + str(timestamp), mode='wt', encoding='utf-8')
	txtfile.write(content)
	txtfile.close()
	
	blogtools.refresh(parent)
	
	blogtools.buildfront() #just in case
	
	blogtools.notify(parent)
	if email not in blogtools.postlist[parent][4]:
		blogtools.postlist[parent][4].append(email)
	
	blogtools.save()
	
	print "<html><head><title>Comment posted.</title></head><body>"
	print "Thanks, " + author + ". Your comment has been posted.<br>"
	print "<a href='" + blogtools.postlist[parent][2] + ".html'>&lt;Back</a>"
	print "</body></html>"
else:
	print "<html><head><title>Post failed.</title></head><body>"
	print "Sorry, your comment has not been posted.<br>"
	print "It looks like you failed the spambot filter. If you're not a spambot, why not go back and try again?"
	print "</body></html>"
