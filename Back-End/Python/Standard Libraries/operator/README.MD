# OPERATOR MODULE
=======================


- operator — Standard operators as functions[DOCS](https://docs.python.org/3.8/library/operator.html)

The operator module exports a set of efficient functions corresponding to the intrinsic operators of Python


-----------------------------------------------------------------------------------------------------

## Arithmetic Function

- add(a, b)
- mul(a, b)
- pow(a, b)
- mod(a, b)
- floordiv(a, b)
- neg(a)

## Comparison and Boolean Operators

- lt(a, b)
- le(a, b)
- gt(a, b)
- ge(a, b)
- and_(a, b)
- or_(a,b)
- eq(a, b)
- ne(a, b)
- is_(a,b) is_not(a,b)
- not_(a,b)

## Sequence/Mapping Operator

- concat(s1, s2)
- contains(s, val)
- countOf(s, val)
- getitem(s, i)
- setitem(s, i, val)
- delitem(s, i)


## Item Getters

- itemgetter(i)s = [1, 2, 3] returns a callable which takes one parameter: a sequence object
- getitem(s, i) takes two parameters, and returns a value: s[i]


## Attribute Getters


- attrgetter is similar to itemgetter, but is used to retrieve object attributes

Return a callable object that fetches attr from its operand. If more than one attribute is requested, returns a tuple of attributes. The attribute names can also contain dots.


-----------------------------------------------------------------------------------------------------