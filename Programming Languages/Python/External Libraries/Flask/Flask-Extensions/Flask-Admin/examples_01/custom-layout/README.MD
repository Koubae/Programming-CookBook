# Flask-Admin - Custom-Layout
=============================

#### Taken from [Flask-Admin Docs](#https://github.com/flask-admin/flask-admin/tree/master/examples/custom-layout)



This example shows how you can customize the look & feel of the admin interface. 


> The custom template are create.html, edit.html, layout.html, list.html  found in Templates/

The base layout is layout.html define in admin.add_view:

```

admin = admin.Admin(app, 'Admin Console', base_template='layout.html', template_mode='bootstrap3')

```

> edit, list and create is overwriten here:

```

class CustomView(ModelView):
    list_template = 'list.html'
    create_template = 'create.html'
    edit_template = 'edit.html'

```

----------------------------

### In list.html:

There is the use of admin_view, which is a ***__main__.UserAdmin object ***

In this scenario UserAdmin is a Customized Admin Interface class, which inherits from 'CustomView' which inherit from ModelView


### In create.html:

There is the user of Jinja {% call %}
In some cases it can be useful to pass a macro to another macro. For this purpose, you can use the special call block.

```

{% macro render_dialog(title, class='dialog') -%}
    <div class="{{ class }}">
        <h2>{{ title }}</h2>
        <div class="contents">
            {{ caller() }}
        </div>
    </div>
{%- endmacro %}

{% call render_dialog('Hello World') %}
    This is a simple dialog rendered by using a macro and
    a call block.
{% endcall %}

```

```

{% macro dump_users(users) -%}
    <ul>
    {%- for user in users %}
        <li><p>{{ user.username|e }}</p>{{ caller(user) }}</li>
    {%- endfor %}
    </ul>
{%- endmacro %}

{% call(user) dump_users(list_of_user) %}
    <dl>
        <dl>Realname</dl>
        <dd>{{ user.realname|e }}</dd>
        <dl>Description</dl>
        <dd>{{ user.description }}</dd>
    </dl>
{% endcall %}

```