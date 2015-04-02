#!/usr/bin/env python

# This script converts an old postlist to a new one, by adding one extra
# field to every post for a list of subscribers.
# 
# You should only need to run this once.

import blogtools

for i in blogtools.postlist:
	if len(blogtools.postlist[i]) == 4:
		blogtools.postlist[i].append([])

blogtools.save()
