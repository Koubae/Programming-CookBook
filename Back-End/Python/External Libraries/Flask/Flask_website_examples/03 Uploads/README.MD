# Flask Uploading File
=========================

**Demostration to How to upload file.**



### Project A - Straight from Flask Documentation


> **[DOCS](https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/#uploading-files)**


Requirements:

- Flask
- Flask - send_from_directory
- werkzeug.utilis - secure_filename

Demostration of how to upload file using Vanila Flask excatly as it's explained into Flask Docs.


-  [secure_filename()](https://werkzeug.palletsprojects.com/en/1.0.x/utils/#werkzeug.utils.secure_filename) 


Pass it a filename and it will return a secure version of it. This filename can then safely be stored on a regular file system and passed to os.path.join(). The filename returned is an ASCII only string for maximum portability.

--------------------------------------------------------------------------------------------

### Project B - My Own Solution.

**Simple Flask App for uploading picture in a database.**

Requirements:

- [base64](https://docs.python.org/3/library/base64.html) - b64encode
- [io](https://docs.python.org/3/library/io.html) - [BytesIO](https://docs.python.org/3/library/io.html?highlight=bytesio#io.BytesIO)
- Flask
- Flask-SQLAlchemy / SQLAlchemy / Sqlite3


### Features

* 1 Basic CRUD system for picutes & files.

* 2 With class **class FileContent(db.Model):**, saves the file into 2 format, one for in bytes in order to download the file the other into a string so that it can be displyed into the Web Page -View.

* 3 Downloads the file and pics

* 4 Show the pic into Web Page



##### NOTE

Initially I wanted to use flask_uploads however it seems that is not longer supported with the new Werkzeug version (last working version is Werkzeug==0.16.0


- Using [Bootstrap4](https://getbootstrap.com/) for front-end.

```

<!-- CSS only -->
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">

<!-- JS, Popper.js, and jQuery -->
<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>


```

--------------------------------------------------------------------------------------------