#!/usr/bin/env python3
import cgi
import os
import json

envi = dict(os.environ)
qry = json.dumps(envi["QUERY_STRING"]) 
browser = json.dumps(envi["HTTP_USER_AGENT"])

print ("Content-type:text/html\r\n\r\n")
print ('<html>')
print ('<head>')
print ('<title>CGI Lab</title>')
print ('</head>')
print ('<body>')
print ('<p>Query String:' + qry + '</p>')
print ('<p>Browser Info:' + browser + '</p>')
print ('</body>')
print ('</html>')

