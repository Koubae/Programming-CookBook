# Numeric Types
=======================


- []()
-----------------------------------------------------------------------------------------------------

## Features

- [sys.getsizeof(object[, default])](https://docs.python.org/3/library/sys.html)

getsizeof() calls the object’s __sizeof__ method and adds an additional garbage collector overhead if the object is managed by the garbage collector.


- Floor division + % modulo (reminder)

```
 = d * (n // d) + (n % d)
```

---------------------------------------------------


- bin() bin(10) → '0b1010'

- oct() → '0o12'

- hex() hex(10) → '0xa'

---------------------------------------------------

### NOTES

What's the largest (base 10) integer number that can be represented using 8 bits?

If don't count negative integers than is **255**

If we count the negative of integer then **1 bit** is reserved to represent the sign of
the number, leaving us with only 7 bits.

The largest number we can represent using 7 bits is 27 – 1 = 127

*So, using 8 bits we are able to represent all the integers in the range **[-127, 127]***

Since 0 does not require a sign, we can squeeze out an extra number,and we end up with the range:

#### **[-128, 127]**

--------------------------------------

- If we want to use 16 bits to store (signed) integers, our range would be:

```
2(16-1) = 215 = 32,768 Range: [-32,768 … 32,767]
```

- Similarly, if we want to use 32 bits to store (signed) integers, our range would be:

```
2(32-1) = 231 = 2,147,483,648 Range: [-2,147,483,648 … 2,147,483,647]
```

If we had an unsigned integer type, using 32 bits our range would be:
```
[0, 232] = [0 … 4,294,967,296]
```

In a 32-bit OS memory spaces (bytes) are limited by their address number == > 32 bits.

```
4,294,967,296 bytes of addressable memory

= 4,294,967,296 / 1024 kB = 4,194,304 kB
= 4,194,304 / 1024 MB = 4,096 MB
= 4,096 / 1024 GB = 4 GB
```

So, how large an integer can be depends on how many bits are used to store the number.
Some languages (such as Java, C, …) provide multiple distinct integer data types that use a fixed number of bits:

*JAVA*
```
byte signed 8-bit numbers -128, …, 127

short signed 16-bit numbers -32,768, …, 32,767

int signed 32-bit numbers -231 …, 231 - 1

long -263 …, 263 signed 64-bit numbers - 1
```

**Python does not work this way**

The int object uses a variable number of bits, Can use 4 bytes (32 bits), 8 bytes (64 bits), 12 bytes (96 bits), etc

[since ints are actually objects, there is a further fixed overhead per integer]
Theoretically limited only by the amount of memory available

-----------------------------------------------------------------------------------------------------


-----------------------------------------------------------------------------------------------------