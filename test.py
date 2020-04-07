#!C:\Python3\python.exe
import os
from http import cookies

#new_cookie = cookies.SimpleCookie()
# new_cookie["name"] = "Mike"
# new_cookie["name"]["path"] = "/"
# #new_cookie["name"]["expires"] = ""
# new_cookie["name"]["httponly"] = 1
# print(new_cookie.output())
cookie = cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
 
print ("Content-Type: text/html")
print("")

print ("<html><head>")
print ("")
print ("</head><body>")
print ("<h1>Привет!!!</h1>")
print(cookie.get("name").value)
print ("</body></html>")