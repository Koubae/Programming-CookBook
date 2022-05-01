

## WIDGET.PY

> 'Select2Widget', 'DatePickerWidget', 'DateTimePickerWidget', 'RenderTemplateWidget', 'Select2TagsWidget'



> **class Select2Widget(widgets.select):**

```

Select2 <https://github.com/ivaynberg/select2>`_ styled select widget.

You must include select2.js, form-x.x.x.js and select2 stylesheet for it to
work.

```

------------------------

> class Select2TagsWidget(widgets.TextInput):


```

Select2 <http://ivaynberg.github.com/select2/#tags>`_ styled text widget.
You must include select2.js, form-x.x.x.js and select2 stylesheet for it to work.
    
```

------------------------

> class DataPickerWidget(widgets.TextInput):

```

Date picker widget.

You must include bootstrap-datepicker.js and form-x.x.x.js for styling to work.

```

------------------------

> class TimePickerWidget(widgets.TextInput):

```
        
Date picker widget.
You must include bootstrap-datepicker.js and form-x.x.x.js for styling to work.

```

------------------------

> class RenderTemplateWidget(object):

```

WTForms widget that renders Jinja2 template


```

------------------------

## FIELDS.PY


```

An understanding of WTForms's Custom Widgets is helpful for understanding this code:
http://wtforms.simplecodes.com/docs/0.6.2/widgets.html#custom-widgets

```

--------------------------

> class DateTimeField(fields.DateTimeField):

```
Allows modifying the datetime format of a DateTimeField using form_args.

```

--------------------------

> class TimeField(fields.Field):

```

A text field which stores a `datetime.time` object.
Accepts time string in multiple formats: 20:10, 20:10:00, 10:00 am, 9:30pm, etc.

```

--------------------------

> class TimeField(fields.Field):

```

A text field which stores a `datetime.time` object.
Accepts time string in multiple formats: 20:10, 20:10:00, 10:00 am, 9:30pm, etc.

```

--------------------------


> class Select2Field(fields.SelectField):

```

Select2 <https://github.com/ivaynberg/select2>`_ styled select widget.

You must include select2.js, form-x.x.x.js and select2 stylesheet for it to
work.

```


> class Select2TagsField(fields.StringField):

```

Select2 <http://ivaynberg.github.com/select2/#tags>`_ styled text field.
You must include select2.js, form-x.x.x.js and select2 stylesheet for it to work.

```

--------------------------

## FIELDS.PY


**'FileUploadInput', 'FileUploadField', 'ImageUploadInput', 'ImageUploadField', 'namegen_filename', 'thumbgen_filename'**


> class ImageUploadField(FileUploadField):

Default allowed extensions: ('gif', 'jpg', 'jpeg', 'png', 'tiff')

```

Image upload field.
Does image validation, thumbnail generation, updating and deleting images.
Requires PIL (or Pillow) to be installed.

```

**keep_image_formats = ('PNG',)**

If field detects that uploaded image is not in this list, it will save image as PNG
