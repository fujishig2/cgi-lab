#!/usr/bin/env python3


import os
import json
import cgi
import cgitb
cgitb.enable()

from cgi import escape

user = ""
passwd = ""
form = cgi.FieldStorage()
if(form.getvalue("username") and form.getvalue("password")):
    user = form["username"].value
    passwd = form["password"].value

    if (username == user or password == passwd): 
        print ("Set-Cookie" + user + "\r\n")
        print ("Set-Cookie" + passwd + "\r\n") 

class FollowingTheTAsInstructionsError(Exception):
    def __init__(self):
        Exception.__init__(self, (
            "You must edit secret.py to change the username, password, "
            "and to delete this error!"
        ))

# Edit the following two lines:
username = "Kyle"
password = "1234"

def login_page():
    """
    Returns the HTML for the login page.
    """

    return _wrapper(r"""
    <h1> Welcome! </h1>

    <form method="POST" action="login.py">
        <label> <span>Username:</span> <input autofocus type="text" name="username"></label> <br>
        <label> <span>Password:</span> <input type="password" name="password"></label>

        <button type="submit"> Login! </button>
    </form>
    """)

def _wrapper(page):
    """
    Wraps some text in common HTML.
    """
    return ("""
    <!DOCTYPE HTML>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            body {
                font-family: -apple-system, BlinkMacSystemFont, sans-serif;
                max-width: 24em;
                margin: auto;
                color: #333;
                background-color: #fdfdfd
            }

            .spoilers {
                color: rgba(0,0,0,0); border-bottom: 1px dashed #ccc
            }
            .spoilers:hover {
                transition: color 250ms;
                color: rgba(36, 36, 36, 1)
            }

            label {
                display: flex;
                flex-direction: row;
            }

            label > span {
                flex: 0;
            }

            label> input {
                flex: 1;
            }

            button {
                font-size: larger;
                float: right;
                margin-top: 6px;
            }
        </style>
    </head>
    <body>
    """ + page + """
    </body>
    </html>
    """)


print(login_page())
  