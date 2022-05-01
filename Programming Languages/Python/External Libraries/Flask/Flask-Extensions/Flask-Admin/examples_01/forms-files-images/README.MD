# Flask-Admin - Forms- Files - Image With Redis and Pillow
=============================


#### Taken from [Flask-Admin Docs](#https://github.com/flask-admin/flask-admin/tree/master/examples/forms-files-images)


>> This example shows how you can:

```

* define your own custom forms by using form rendering rules
* handle generic static file uploads
* handle image uploads
* turn a TextArea field into a rich WYSIWYG editor using WTForms and CKEditor
* set up a Flask-Admin view as a Redis terminal
* Vendor external script [HERE](#<script src="https://cdn.ckeditor.com/ckeditor5/11.1.1/classic/ckeditor.js"></script>)

<script src="https://cdn.ckeditor.com/ckeditor5/11.1.1/classic/ckeditor.js"></script>


```

---------------------------------------------

## Note!!!

This example uses Bootstrap4 templates which is not included in flask_admin pip install. Need to add 'boostrap4' folder in the flask_admion package. The directory is added here so semplicity.


>> Analisis.

The issue is solved if added a CSS and JavaScript link in here  boostrap4/admin/base.html (taken from [SOURCE](#https://getbootstrap.com/) )

```

<!-- CSS only -->
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">

<!-- JS, Popper.js, and jQuery -->
<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>

```

After further analisys in boostrap4/admin/base.html, I see that the link for bootstrap4 are by default called by 'admin_static.url' which is an import:

```

{% import 'admin/static.html' as admin_static with context %}

```

Hence boostrap4/admin/static.html is a macro calling the url() macro :

```

{% macro url() -%}
    {{ get_url('admin.static', *varargs, **kwargs) }}
{%- endmacro %}

```

Basicallly you need to add:

- 1. flask_admin\forms-files-images\env\Lib\site-packages\flask_admin\static\admin\css\[bootstrap4]

folder can be found [HERE](#https://github.com/flask-admin/flask-admin/tree/master/flask_admin/static/admin/css/bootstrap4)

- 2. flask_admin\forms-files-images\env\Lib\site-packages\flask_admin\static\bootstrap\[bootstrap4]

Folder can be found [HERE](#https://github.com/flask-admin/flask-admin/tree/master/flask_admin/static/bootstrap/bootstrap4)


## Whole list of missing components/folder:

- flask-admin/flask_admin/static/admin/css/bootstrap4 OK

- flask-admin/flask_admin/static/admin/js/bs4_filters.js => OK
- flask-admin/flask_admin/static/admin/js/bs4_modal.js => OK

- flask-admin/flask_admin/static/**bootstrap**/bootstrap4

**THIS IS VERY INTERESTING [Check it out](#https://github.com/flask-admin/flask-admin/tree/master/flask_admin/static/vendor/bootstrap-daterangepicker)**
- flask-admin/flask_admin/static/vendor/bootstrap-daterangepicker/daterangepicker-bs4.css 
- flask-admin/flask_admin/static/vendor/bootstrap4
**Not really needed but [Check it out](#https://github.com/flask-admin/flask-admin/tree/master/flask_admin/static/vendor/multi-level-dropdowns-bootstrap)**
- flask-admin/flask_admin/static/vendor/multi-level-dropdowns-bootstrap/

- flask-admin/flask_admin/static/vendor/x-editable/css/bootstrap4-editable.css
- flask-admin/flask_admin/static/vendor/x-editable/js/bootstrap4-editable.min.js



###  @listens_for

This application uses the decorator @listens_for imported from sqlalchemy.event.

> [DOCS](#https://docs.sqlalchemy.org/en/13/core/event.html)

```

When using named argument passing, the names listed in the function argument specification will be used as keys in the dictionary.

Named style passes all arguments by name regardless of the function signature, so specific arguments may be listed as well, in any order, as long as the names match up:

```

Basically it uses the after_delete from the **sqlalchemy.orm.events.MapperEvents** [DOC](#https://docs.sqlalchemy.org/en/13/orm/events.html#sqlalchemy.orm.events.MapperEvents.after_delete)
[DOC2](#https://www.kite.com/python/docs/sqlalchemy.orm.events.MapperEvents.after_delete)

In this case it uses the after_delete event listens to delete the 'File'  or the 'Image' both pic and thumbnail pic from the directory 'static' called 'files' (not as default 'static') -->
```

app = Flask(__name__, static_folder='files')

```

-----------------------

# CkEditor


## CKTextAreaWidget(widgets.TextArea):

>[Source](#https://wtforms.readthedocs.io/en/2.3.x/_modules/wtforms/widgets/core/#TextArea)


```

class TextArea(object):
    """
    Renders a multi-line text area.

    `rows` and `cols` ought to be passed as keyword args when rendering.
    """
    def __call__(self, field, **kwargs):
        kwargs.setdefault('id', field.id)
        if 'required' not in kwargs and 'required' in getattr(field, 'flags', []):
            kwargs['required'] = True
        return Markup('<textarea %s>\r\n%s</textarea>' % (
            html_params(name=field.name, **kwargs),
            escape(field._value())
        ))

```

In: 

```

class CKTextAreaWidget(widgets.TextArea):

    def __call__(self, field, **kwargs):  

```

The attribute *field* is taken from the class **class Field(object):** found in:

>>> flask_admin\forms-files-images\env\lib\site-packages\wtforms\fields\core.py

## create_page.html /edit_page.html [DOCS](#http://cdn.ckeditor.com/):


> It uses CKEditor 5. 

- classic - the Classic editor
- inline - the Inline editor
- balloon - the Balloon editor
- balloon-block - the Balloon block editor
- decoupled-document - the Document editor

```

<script src="https://cdn.ckeditor.com/ckeditor5/22.0.0/classic/ckeditor.js"></script>
    <script>
        ClassicEditor
            .create(document.querySelector('.ckeditor'))
            .catch(error => {
                console.error( error );
            });
    </script>

```






-----------------------


### Markup class jinja2.Markup

> [DOCS](#https://jinja.palletsprojects.com/en/2.11.x/api/?highlight=markup#jinja2.Markup)

A string that is ready to be safely inserted into an HTML or XML document, either because it was escaped or because it was marked safe.

Passing an object to the constructor converts it to text and wraps it to mark it safe without escaping. To escape the text, use the escape() class method instead.

-----------------------

