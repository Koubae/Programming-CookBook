Docstrings
=======================




## CREDIT From Stack Overflow [daouzli](https://stackoverflow.com/a/24385103/13903942)
-------

Python docstrings can be written following several formats as the other posts showed. However the default Sphinx docstring format was not mentioned and is based on **reStructuredText (reST)**. You can get some information about the main formats in [this blog post](http://daouzli.com/blog/docstring.html).

*Note that the reST is recommended by the [PEP 287](https://www.python.org/dev/peps/pep-0287)*

There follows the main used formats for docstrings.

-----------------------------------------------------------------------------------------------------

### Epytext

Historically a **javadoc** like style was prevalent, so it was taken as a base for [Epydoc](http://epydoc.sourceforge.net) (with the called `Epytext` format) to generate documentation.

> Example:

    """
    This is a javadoc style.

    @param param1: this is a first param
    @param param2: this is a second param
    @return: this is a description of what is returned
    @raise keyError: raises an exception
    """

- reST
- Nowadays, the probably more prevalent format is the **reStructuredText** (reST) format that is used by [Sphinx](http://sphinx-doc.org) to generate documentation.
*Note: it is used by default in JetBrains PyCharm (type triple quotes after defining a method and hit enter). It is also used by default as output format in Pyment.*

> Example:

    """
    This is a reST style.

    :param param1: this is a first param
    :param param2: this is a second param
    :returns: this is a description of what is returned
    :raises keyError: raises an exception
    """

-----------------------------------------------------------------------------------------------------

## Google


Google has their own [format](https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings) that is often used. It also can be interpreted by Sphinx (ie. using [Napoleon plugin](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/)). 

Example:

    """
    This is an example of Google style.

    Args:
        param1: This is the first param.
        param2: This is a second param.

    Returns:
        This is a description of what is returned.

    Raises:
        KeyError: Raises an exception.
    """

Even [more examples](https://www.sphinx-doc.org/en/master/usage/extensions/example_google.html#example-google)

-----------------------------------------------------------------------------------------------------

### Numpydoc

Note that Numpy recommend to follow their own [numpydoc](https://numpydoc.readthedocs.io/en/latest/) based on Google format and usable by Sphinx.

    """
    My numpydoc description of a kind
    of very exhautive numpydoc format docstring.

    Parameters
    ----------
    first : array_like
        the 1st param name `first`
    second :
        the 2nd param
    third : {'value', 'other'}, optional
        the 3rd param, by default 'value'

    Returns
    -------
    string
        a value in a string

    Raises
    ------
    KeyError
        when a key error
    OtherError
        when an other error
    """

Converting/Generating
=

It is possible to use a tool like [Pyment](https://github.com/dadadel/pyment) to automatically generate docstrings to a Python project not yet documented, or to convert existing docstrings (can be mixing several formats) from a format to an other one.

*Note: The examples are taken from the [Pyment documentation](https://github.com/dadadel/pyment/blob/master/README.rst)*


-----------------------------------------------------------------------------------------------------