# Python Utils
=======================


## Comments
-----------

- **Codetags**[PEP 350](https://www.python.org/dev/peps/pep-0350/)

* NOTE: Description of how the code works (when it isn't self evident).

* XXX: Warning about possible pitfalls, can be used as NOTE:XXX:.

* REQ (REQUIREMENT, STORY) => Requirements: Satisfactions of specific, formal requirements.

* IDEA => Ideas: Possible RFE candidates, but less formal than RFE.

* ??? (QUESTION, QUEST, QSTN, WTF) Questions: Misunderstood details.

* !!! (ALERT) Alerts: In need of immediate attention.

* FAQ Frequently Asked Questions: Interesting areas that require external explanation.

* TODO: No problem, but additional code needs to be written, usually when you are skipping something.

* OPTIMIZE: Improve the Code.

* LAZY: Lighter than FIXME or HACK.

* FIXME: This works, sort of, but it could be done better. (usually code written in a hurry that needs rewriting).

* HACK: Not very well written or malformed code to circumvent a problem/bug. Should be used as HACK:FIXME:.

* BUG: There is a problem here.

* OCD (known overengineering).



### Add a TODO comment in PyCharm:


 You can add your own patterns and filter the list to show only TODO items that match certain patterns. For example, you can choose to mark places of possible optimization in your code with the OPTIMIZE pattern and ignore all other types of TODO items when viewing them in the TODO tool window.

1. In the Settings/Preferences dialog Ctrl+Alt+S, select Editor | TODO.

2. Use a regular expression to specify a custom pattern.

3. For example, to add a pattern for the OPTIMIZE items, click The Add button in the Patterns section of the TODO dialog, and type the following regular expression:

```
    \boptimize\b.*
```
    Then click OK to save the new pattern.

4. Add a filter to group TODO patterns and view the corresponding TODO items in the TODO tool window separately.

    For example, to add the Optimization filter with the new pattern, click The Add button in the Filters section of the TODO dialog, specify Optimization as its name and select the new pattern to be included in this filter.

    Then click OK to save the new filter.

5. Click OK to apply the changes in the TODO settings dialog.

6. To apply the new filter, in the TODO tool window, click the Filter TODO Items button and select the Optimization filter. 

The icon that you select for a pattern is displayed in the TODO tool window to better distinguish various TODO items. By enabling the Case Sensitive checkbox for a pattern, you can force the pattern to match only with the specified case. 






----------------------------------------------------------------------------------------------------