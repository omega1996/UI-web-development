#!/usr/bin/env python3
import cgi
import os
print( "Content-type: text/html")

form = cgi.FieldStorage()

message = None

# Test if the file is loaded for the upload
if 'image' in form:
    fileitem = form['image']
    fn = os.path.basename(fileitem.filename)
    open(os.path.join(os.getcwd(),'files',fn,), 'wb').write(fileitem.file.read())
    message = 'The file "' + fn + '" was uploaded successfully'
else:
    message = 'No file was uploaded'



print()
print("<h1>Hello world!</h1>")  
print("<p>"+os.getcwd()+"</p>")
print("<p>"+message+"</p>")



#chmod a+x result.py