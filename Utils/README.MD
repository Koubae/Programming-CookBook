# Programming Utils
=======================


Markdown
--------

- [Mastering Markdown](https://guides.github.com/features/mastering-markdown/)
- [How to Write a Good Markdown, realypython.com](https://realpython.com/jobs/tutorial-editor/editing-sample/)




\```pycon
>>> def greet( someone ):
>>>
...   print('Hello, ' +someon)
... 
>>> greet("Chad")

Traceback (most recent call last):
  File "", line 1, in 
  File "", line 2, in greet
NameError: name 'someon' is not defined
```

GitHub
---------

### Pull Request

1. Fork project.
2. Clone it.
3. Create a new branch.  => ```git checkout -b new_branch ```

    * Create a new remote => ``` git remote add upstream [link]```  

4. Perform Changes.
5. Commit Changes and Push to Forked Repo.
    ```
        git add .
        git commit -S -m "..."
        git push -u origin new_branch

    ```
6. Compare & pull request button.
7. Create pull request to open a new pull request.


Scripts Comments
----------------

```
# ============================ < MESSAGE > ============================ #
```


-----------------------------------------------------------------------------------------------------