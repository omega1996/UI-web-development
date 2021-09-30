#!/usr/bin/env python3
import cgi
import os
print( "Content-type: text/html")
print()

import model

form = cgi.FieldStorage()

message = None
full_name = ""
# Test if the file is loaded for the upload
if 'image' in form:
    fileitem = form['image']
    fn = os.path.basename(fileitem.filename)
    full_name = os.path.join(os.getcwd(),'files',fn)
    open(full_name, 'wb').write(fileitem.file.read())
    message = 'The file "' + fn + '" was uploaded successfully'
    print("<p>"+str(model.process_image(full_name))+"</p>")

else:
    message = 'No file was uploaded'



print("<p>"+message+"</p>")

#chmod a+x result.py