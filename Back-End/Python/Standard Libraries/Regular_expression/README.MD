# re — Regular expression operations
=======================


- [DOCS](https://docs.python.org/3/library/re.html)
- [REGEXR](https://regexr.com/)
-----------------------------------------------------------------------------------------------------

Tutorial
---------

- *

    - Causes the resulting RE to match 0 or more repetitions of the preceding RE, 
    as many repetitions as are possible. ab* will match ‘a’, ‘ab’, or ‘a’ followed by 
    any number of ‘b’s.

- ?

    - Causes the resulting RE to match 0 or 1 repetitions of the preceding RE. ab? 
    will match either ‘a’ or ‘ab’.


- *?, +?, ??

    - The '*', '+', and '?' qualifiers are all greedy; they match as much text as possible. 
    Sometimes this behaviour isn’t desired; if the RE <.*> is matched against '<a> b <c>', 
    it will match the entire string, and not just '<a>'. Adding ? after the qualifier makes it 
    perform the match in non-greedy or minimal fashion; as few characters as possible will be matched. 
    Using the RE <.*?> will match only '<a>'.

    
### 


-----------------------------------------------------------------------------------------------------