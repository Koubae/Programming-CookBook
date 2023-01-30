C Roadmap - Data Types 2
=======================


- Data Types 2
    - pointers
        - double pointer
        - function pointer
        - restrict
    - volatile
    - struct (structure)
        - Access operator '.'  [struct].[proprerty]
        - Access operator pointer '->'  [struct]->[proprerty]
    - union 
    - enum 
    - size_t [What is size_t in C?](https://stackoverflow.com/questions/2550774/what-is-size-t-in-c)
    - typedef


Pointers
---------

- [Pointer declaration](https://en.cppreference.com/w/c/language/pointer)
- [Implicit conversions](https://en.cppreference.com/w/c/language/conversion)


- [Pointer Declarations](https://learn.microsoft.com/en-us/cpp/c-language/pointer-declarations?view=msvc-170)

- [valatile - cppreference.com](https://en.cppreference.com/w/c/language/volatile)
- [restrict - cppreference.com](https://en.cppreference.com/w/c/language/restrict)
- [Typedef ](https://en.cppreference.com/w/c/language/typedef)

- [Why is volatile needed in C?](https://stackoverflow.com/questions/246127/why-is-volatile-needed-in-c)


### const | volatile | typedef | restrict

- [Type Qualifiers](https://learn.microsoft.com/en-us/cpp/c-language/type-qualifiers?view=msvc-170)

Type qualifiers give one of two properties to an identifier. The const type qualifier declares an object to be nonmodifiable. The volatile type qualifier declares an item whose value can legitimately be changed by something beyond the control of the program in which it appears, such as a concurrently executing thread.

The type qualifiers, const, restrict, and volatile, can appear only once in a declaration. Type qualifiers can appear with any type specifier; however, they can't appear after the first comma in a multiple item declaration.