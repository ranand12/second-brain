# Prettify Your Data Structures With Pretty Print in Python – Real Python

Column: https://realpython.com/python-pretty-print/
Processed: No
created on: December 29, 2021 12:04 PM
topics: money, python, tech-stuff

![](Prettify%20Your%20Data%20Structures%20With%20Pretty%20Print%20in%20367332a2a5ab42f4a036b1259c618d78/Python_s-Pretty-Print-pprint_Watermarked.a3e409650f59.jpeg)

Table of Contents

- [Working With pprint](https://realpython.com/python-pretty-print/#working-with-pprint)
- [Exploring Optional Parameters of pprint()](https://realpython.com/python-pretty-print/#exploring-optional-parameters-of-pprint)
- [Creating a Custom PrettyPrinter Object](https://realpython.com/python-pretty-print/#creating-a-custom-prettyprinter-object)
- [Getting a Pretty String With pformat()](https://realpython.com/python-pretty-print/#getting-a-pretty-string-with-pformat)
- [Handling Recursive Data Structures](https://realpython.com/python-pretty-print/#handling-recursive-data-structures)
- [Conclusion](https://realpython.com/python-pretty-print/#conclusion)

[](https://img.realpython.net/16bf1efe41b538fae54711c58c701f0e)

Dealing with data is essential for any Pythonista, but sometimes that data is just not very pretty. Computers don’t care about formatting, but without good formatting, humans may find something hard to read. The output isn’t pretty when you use `print()` on large dictionaries or long lists—it’s efficient, but not pretty.

The `pprint` module in Python is a utility module that you can use to print data structures in a readable, **pretty** way. It’s a part of the standard library that’s especially useful for debugging code dealing with API requests, large JSON files, and data in general.

**By the end of this tutorial, you’ll:**

- Understand **why** the `pprint` module is **necessary**
- Learn how to use **`pprint()`**, **`PrettyPrinter`**, and their **parameters**
- Be able to create your own instance of **`PrettyPrinter`**
- Save **formatted string output** instead of printing it
- Print and recognize **recursive data structures**

Along the way, you’ll also see an HTTP request to a public API and [JSON parsing](https://realpython.com/python-json/) in action.

**Free Bonus:** Click here to get a Python Cheat Sheet and learn the basics of Python 3, like working with data types, dictionaries, lists, and Python functions.

## Understanding the Need for Python’s Pretty Print

The Python `pprint` module is helpful in many situations. It comes in handy when making API requests, dealing with [JSON files](https://realpython.com/python-json/), or handling complicated and nested data. You’ll probably find that using the normal [`print()`](https://realpython.com/python-print/) function isn’t adequate to efficiently explore your data and [debug](https://realpython.com/python-debugging-pdb/) your application. When you use `print()` with [dictionaries](https://realpython.com/python-dicts/) and [lists](https://realpython.com/python-lists-tuples/), the output doesn’t contain any newlines.

Before you start exploring `pprint`, you’ll first use `urllib` to make a request to get some data. You’ll make a request to [{JSON} Placeholder](https://jsonplaceholder.typicode.com/) for some mock user information. The first thing to do is to make the HTTP `GET` request and put the response into a dictionary:

```
>>> from urllib import request
>>> response = request.urlopen("https://jsonplaceholder.typicode.com/users")
>>> json_response = response.read()
>>> import json
>>> users = json.loads(json_response)

```

Here, you make a basic `GET` request and then parse the response into a dictionary with `json.loads()`. With the dictionary now in a variable, a common next step is to print the contents with `print()`:

```
>>> print(users)
[{'id': 1, 'name': 'Leanne Graham', 'username': 'Bret', 'email': 'Sincere@april.biz', 'address': {'street': 'Kulas Light', 'suite': 'Apt. 556', 'city': 'Gwenborough', 'zipcode': '92998-3874', 'geo': {'lat': '-37.3159', 'lng': '81.1496'}}, 'phone': '1-770-736-8031 x56442', 'website': 'hildegard.org', 'company': {'name': 'Romaguera-Crona', 'catchPhrase': 'Multi-layered client-server neural-net', 'bs': 'harness real-time e-markets'}}, {'id': 2, 'name': 'Ervin Howell', 'username': 'Antonette', 'email': 'Shanna@melissa.tv', 'address': {'street': 'Victor Plains', 'suite': 'Suite 879', 'city': 'Wisokyburgh', 'zipcode': '90566-7771', 'geo': {'lat': '-43.9509', 'lng': '-34.4618'}}, 'phone': '010-692-6593 x09125', 'website': 'anastasia.net', 'company': {'name': 'Deckow-Crist', 'catchPhrase': 'Proactive didactic contingency', 'bs': 'synergize scalable supply-chains'}}, {'id': 3, 'name': 'Clementine Bauch', 'username': 'Samantha', 'email': 'Nathan@yesenia.net', 'address': {'street': 'Douglas Extension', 'suite': 'Suite 847', 'city': 'McKenziehaven', 'zipcode': '59590-4157', 'geo': {'lat': '-68.6102', 'lng': '-47.0653'}}, 'phone': '1-463-123-4447', 'website': 'ramiro.info', 'company': {'name': 'Romaguera-Jacobson', 'catchPhrase': 'Face to face bifurcated interface', 'bs': 'e-enable strategic applications'}}, {'id': 4, 'name': 'Patricia Lebsack', 'username': 'Karianne', 'email': 'Julianne.OConner@kory.org', 'address': {'street': 'Hoeger Mall', 'suite': 'Apt. 692', 'city': 'South Elvis', 'zipcode': '53919-4257', 'geo': {'lat': '29.4572', 'lng': '-164.2990'}}, 'phone': '493-170-9623 x156', 'website': 'kale.biz', 'company': {'name': 'Robel-Corkery', 'catchPhrase': 'Multi-tiered zero tolerance productivity', 'bs': 'transition cutting-edge web services'}}, {'id': 5, 'name': 'Chelsey Dietrich', 'username': 'Kamren', 'email': 'Lucio_Hettinger@annie.ca', 'address': {'street': 'Skiles Walks', 'suite': 'Suite 351', 'city': 'Roscoeview', 'zipcode': '33263', 'geo': {'lat': '-31.8129', 'lng': '62.5342'}}, 'phone': '(254)954-1289', 'website': 'demarco.info', 'company': {'name': 'Keebler LLC', 'catchPhrase': 'User-centric fault-tolerant solution', 'bs': 'revolutionize end-to-end systems'}}, {'id': 6, 'name': 'Mrs. Dennis Schulist', 'username': 'Leopoldo_Corkery', 'email': 'Karley_Dach@jasper.info', 'address': {'street': 'Norberto Crossing', 'suite': 'Apt. 950', 'city': 'South Christy', 'zipcode': '23505-1337', 'geo': {'lat': '-71.4197', 'lng': '71.7478'}}, 'phone': '1-477-935-8478 x6430', 'website': 'ola.org', 'company': {'name': 'Considine-Lockman', 'catchPhrase': 'Synchronised bottom-line interface', 'bs': 'e-enable innovative applications'}}, {'id': 7, 'name': 'Kurtis Weissnat', 'username': 'Elwyn.Skiles', 'email': 'Telly.Hoeger@billy.biz', 'address': {'street': 'Rex Trail', 'suite': 'Suite 280', 'city': 'Howemouth', 'zipcode': '58804-1099', 'geo': {'lat': '24.8918', 'lng': '21.8984'}}, 'phone': '210.067.6132', 'website': 'elvis.io', 'company': {'name': 'Johns Group', 'catchPhrase': 'Configurable multimedia task-force', 'bs': 'generate enterprise e-tailers'}}, {'id': 8, 'name': 'Nicholas Runolfsdottir V', 'username': 'Maxime_Nienow', 'email': 'Sherwood@rosamond.me', 'address': {'street': 'Ellsworth Summit', 'suite': 'Suite 729', 'city': 'Aliyaview', 'zipcode': '45169', 'geo': {'lat': '-14.3990', 'lng': '-120.7677'}}, 'phone': '586.493.6943 x140', 'website': 'jacynthe.com', 'company': {'name': 'Abernathy Group', 'catchPhrase': 'Implemented secondary concept', 'bs': 'e-enable extensible e-tailers'}}, {'id': 9, 'name': 'Glenna Reichert', 'username': 'Delphine', 'email': 'Chaim_McDermott@dana.io', 'address': {'street': 'Dayna Park', 'suite': 'Suite 449', 'city': 'Bartholomebury', 'zipcode': '76495-3109', 'geo': {'lat': '24.6463', 'lng': '-168.8889'}}, 'phone': '(775)976-6794 x41206', 'website': 'conrad.com', 'company': {'name': 'Yost and Sons', 'catchPhrase': 'Switchable contextually-based project', 'bs': 'aggregate real-time technologies'}}, {'id': 10, 'name': 'Clementina DuBuque', 'username': 'Moriah.Stanton', 'email': 'Rey.Padberg@karina.biz', 'address': {'street': 'Kattie Turnpike', 'suite': 'Suite 198', 'city': 'Lebsackbury', 'zipcode': '31428-2261', 'geo': {'lat': '-38.2386', 'lng': '57.2232'}}, 'phone': '024-648-3804', 'website': 'ambrose.net', 'company': {'name': 'Hoeger LLC', 'catchPhrase': 'Centralized empowering task-force', 'bs': 'target end-to-end models'}}]

```

Oh dear! One huge line with no newlines. Depending on your console settings, this might appear as one very long line. Alternatively, your console output might have its word-wrapping mode on, which is the most common situation. Unfortunately, that doesn’t make the output much friendlier!

If you look at the first and last characters, you can see that this appears to be a list. You might be tempted to start writing a loop to print the items:

```
for user in users:
    print(user)

```

This `for` loop would print each object on a separate line, but even then, each object takes up way more space than can fit on a single line. Printing in this way does make things a bit better, but it’s by no means ideal. The above example is a relatively simple data structure, but what would you do with a deeply nested dictionary 100 times the size?

Sure, you could write a function that uses [recursion](https://realpython.com/python-recursion/) to find a way to print everything. Unfortunately, you’ll likely run into some edge cases where this won’t work. You might even find yourself writing a whole module of functions just to get to grips with the structure of the data!

Enter the `pprint` module!

[](https://img.realpython.net/32dc2b8267d0b6061434a93732943fa5)

## Working With `pprint`

`pprint` is a Python module made to print data structures in a pretty way. It has long been part of the Python standard library, so installing it separately isn’t necessary. All you need to do is to import its `pprint()` function:

```
>>> from pprint import pprint

```

Then, instead of going with the normal `print(users)` approach as you did in the example above, you can call your new favorite function to make the output pretty:

```
>>> pprint(users)

```

This function prints `users`—but in a new-and-improved *pretty* way:

```
>>> pprint(users)
[{'address': {'city': 'Gwenborough',
              'geo': {'lat': '-37.3159', 'lng': '81.1496'},
              'street': 'Kulas Light',
              'suite': 'Apt. 556',
              'zipcode': '92998-3874'},
  'company': {'bs': 'harness real-time e-markets',
              'catchPhrase': 'Multi-layered client-server neural-net',
              'name': 'Romaguera-Crona'},
  'email': 'Sincere@april.biz',
  'id': 1,
  'name': 'Leanne Graham',
  'phone': '1-770-736-8031 x56442',
  'username': 'Bret',
  'website': 'hildegard.org'},
 {'address': {'city': 'Wisokyburgh',
              'geo': {'lat': '-43.9509', 'lng': '-34.4618'},
              'street': 'Victor Plains',
              'suite': 'Suite 879',
              'zipcode': '90566-7771'},
  'company': {'bs': 'synergize scalable supply-chains',
              'catchPhrase': 'Proactive didactic contingency',
              'name': 'Deckow-Crist'},
  'email': 'Shanna@melissa.tv',
  'id': 2,
  'name': 'Ervin Howell',
  'phone': '010-692-6593 x09125',
  'username': 'Antonette',
  'website': 'anastasia.net'},

 ...

 {'address': {'city': 'Lebsackbury',
              'geo': {'lat': '-38.2386', 'lng': '57.2232'},
              'street': 'Kattie Turnpike',
              'suite': 'Suite 198',
              'zipcode': '31428-2261'},
  'company': {'bs': 'target end-to-end models',
              'catchPhrase': 'Centralized empowering task-force',
              'name': 'Hoeger LLC'},
  'email': 'Rey.Padberg@karina.biz',
  'id': 10,
  'name': 'Clementina DuBuque',
  'phone': '024-648-3804',
  'username': 'Moriah.Stanton',
  'website': 'ambrose.net'}]

```

How pretty! The keys of the dictionaries are even visually indented! This output makes it so much more straightforward to scan and visually analyze data structures.

**Note:** The output you’ll see will be longer if you run the code yourself. This code block truncates the output for readability.

If you’re a fan of typing as little as possible, then you’ll be pleased to know that `pprint()` has an alias, `pp()`:

```
>>> from pprint import pp
>>> pp(users)

```

`pp()` is just a wrapper around `pprint()`, and it’ll behave exactly the same way.

**Note:** Python has included this alias since [version 3.8.0 alpha 2](https://github.com/python/cpython/tree/96831c7fcf888af187bbae8254608cccb4d6a03c).

However, even the default output may be too much information to scan at first. Maybe all you really want is to verify that you’re dealing with a list of plain objects. For that, you’ll want to tweak the output a little.

For these situations, there are various parameters you can pass to `pprint()` to make even the tersest data structures pretty.

## Exploring Optional Parameters of `pprint()`

In this section, you’ll learn about all the parameters available for `pprint()`. There are seven parameters that you can use to configure your Pythonic pretty printer. You don’t need to use them all, and some will be more useful than others. The one you’ll find most valuable will probably be `depth`.

### Summarizing Your Data: `depth`

One of the handiest parameters to play around with is `depth`. The following Python command will only print the full contents of `users` if the data structure is at or lower than the specified depth—all while keeping things pretty, of course. The contents of deeper data structures are replaced with three dots:

```
>>> pprint(users, depth=1)
[{...}, {...}, {...}, {...}, {...}, {...}, {...}, {...}, {...}, {...}]

```

Now you can immediately see that this is indeed a list of dictionaries. To explore the data structure further, you can increase the depth by one level, which will print all the top-level keys of the dictionaries in `users`:

```
>>> pprint(users, depth=2)
[{'address': {...},
  'company': {...},
  'email': 'Sincere@april.biz',
  'id': 1,
  'name': 'Leanne Graham',
  'phone': '1-770-736-8031 x56442',
  'username': 'Bret',
  'website': 'hildegard.org'},
 {'address': {...},
  'company': {...},
  'email': 'Shanna@melissa.tv',
  'id': 2,
  'name': 'Ervin Howell',
  'phone': '010-692-6593 x09125',
  'username': 'Antonette',
  'website': 'anastasia.net'},

  ...

 {'address': {...},
  'company': {...},
  'email': 'Rey.Padberg@karina.biz',
  'id': 10,
  'name': 'Clementina DuBuque',
  'phone': '024-648-3804',
  'username': 'Moriah.Stanton',
  'website': 'ambrose.net'}]

```

Now you can quickly check whether all the dictionaries share their top-level keys. This is a valuable observation to make, especially if you’re tasked with developing an application that consumes data like this.

[](https://img.realpython.net/babd32c4a9b6cf2453889710f58b5914)

### Giving Your Data Space: `indent`

The `indent` parameter controls how indented each level of the pretty-printed representation will be in the output. The default indent is just `1`, which translates to one space character:

```
>>> pprint(users[0], depth=1)
{'address': {...},
 'company': {...},
 'email': 'Sincere@april.biz',
 'id': 1,
 'name': 'Leanne Graham',
 'phone': '1-770-736-8031 x56442',
 'username': 'Bret',
 'website': 'hildegard.org'}

>>> pprint(users[0], depth=1, indent=4)
{   'address': {...},
    'company': {...},
    'email': 'Sincere@april.biz',
    'id': 1,
    'name': 'Leanne Graham',
    'phone': '1-770-736-8031 x56442',
    'username': 'Bret',
    'website': 'hildegard.org'}

```

The most important part of the indenting behavior of `pprint()` is keeping all the keys aligned visually. How much indentation is applied depends on both the `indent` parameter and where the key is.

Since there’s no nesting in the examples above, the amount of indentation is based completely on the `indent` parameter. In both examples, note how the opening curly bracket (`{`) is counted as a unit of indentation for the first key. In the first example, the opening single quote for the first key comes right after `{` without any spaces in between because the indent is set to `1`.

When there is nesting, however, the indentation is applied to the first element in-line, and `pprint()` then keeps all following elements aligned with the first one. So if you set your `indent` to `4` when printing `users`, the first element will be indented by four characters, while the nested elements will be indented by more than eight characters because the indentation starts from the end of the first key:

```
>>> pprint(users[0], depth=2, indent=4)
{   'address': {   'city': 'Gwenborough',
                   'geo': {...},
                   'street': 'Kulas Light',
                   'suite': 'Apt. 556',
                   'zipcode': '92998-3874'},
    'company': {   'bs': 'harness real-time e-markets',
                   'catchPhrase': 'Multi-layered client-server neural-net',
                   'name': 'Romaguera-Crona'},
    'email': 'Sincere@april.biz',
    'id': 1,
    'name': 'Leanne Graham',
    'phone': '1-770-736-8031 x56442',
    'username': 'Bret',
    'website': 'hildegard.org'}

```

This is just another part of the *pretty* in Python’s `pprint()`!

### Limiting Your Line Lengths: `width`

By default, `pprint()` will only output up to eighty characters per line. You can customize this value by passing in a `width` argument. `pprint()` will make an effort to fit the contents on one line. If the contents of a data structure go over this limit, then it’ll print every element of the current data structure on a new line:

```
>>> pprint(users[0])
{'address': {'city': 'Gwenborough',
             'geo': {'lat': '-37.3159', 'lng': '81.1496'},
             'street': 'Kulas Light',
             'suite': 'Apt. 556',
             'zipcode': '92998-3874'},
 'company': {'bs': 'harness real-time e-markets',
             'catchPhrase': 'Multi-layered client-server neural-net',
             'name': 'Romaguera-Crona'},
 'email': 'Sincere@april.biz',
 'id': 1,
 'name': 'Leanne Graham',
 'phone': '1-770-736-8031 x56442',
 'username': 'Bret',
 'website': 'hildegard.org'}

```

When you leave the width at the default of eighty characters, the dictionary at `users[0]['address']['geo']` only contains a `'lat'` and a `'lng'` attribute. This means that taking the sum of the indent and the number of characters needed to print out the dictionary, including the spaces in between, comes to less than eighty characters. Since it’s less than eighty characters, the default width, `pprint()` puts it all on one line.

However, the dictionary at `users[0]['company']` would go over the default width, so `pprint()` puts each key on a new line. This is true of dictionaries, lists, tuples, and sets:

```
>>> pprint(users[0], width=160)
{'address': {'city': 'Gwenborough', 'geo': {'lat': '-37.3159', 'lng': '81.1496'}, 'street': 'Kulas Light', 'suite': 'Apt. 556', 'zipcode': '92998-3874'},
 'company': {'bs': 'harness real-time e-markets', 'catchPhrase': 'Multi-layered client-server neural-net', 'name': 'Romaguera-Crona'},
 'email': 'Sincere@april.biz',
 'id': 1,
 'name': 'Leanne Graham',
 'phone': '1-770-736-8031 x56442',
 'username': 'Bret',
 'website': 'hildegard.org'}

```

If you set the width to a large value like `160`, then all the nested dictionaries fit on one line. You can even take it to extremes and use a huge value like `500`, which, for this example, prints the whole dictionary on one line:

```
>>> pprint(users[0], width=500)
{'address': {'city': 'Gwenborough', 'geo': {'lat': '-37.3159', 'lng': '81.1496'}, 'street': 'Kulas Light', 'suite': 'Apt. 556', 'zipcode': '92998-3874'}, 'company': {'bs': 'harness real-time e-markets', 'catchPhrase': 'Multi-layered client-server neural-net', 'name': 'Romaguera-Crona'}, 'email': 'Sincere@april.biz', 'id': 1, 'name': 'Leanne Graham', 'phone': '1-770-736-8031 x56442', 'username': 'Bret', 'website': 'hildegard.org'}

```

Here, you get the effects of setting `width` to a relatively large value. You can go the other way and set `width` to a low value such as `1`. However, the main effect that this will have is making sure every data structure will display its components on separate lines. You’ll still get the visual indentation that lines up the components:

```
>>> pprint(users[0], width=5)
{'address': {'city': 'Gwenborough',
             'geo': {'lat': '-37.3159',
                     'lng': '81.1496'},
             'street': 'Kulas '
                       'Light',
             'suite': 'Apt. '
                      '556',
             'zipcode': '92998-3874'},
 'company': {'bs': 'harness '
                   'real-time '
                   'e-markets',
             'catchPhrase': 'Multi-layered '
                            'client-server '
                            'neural-net',
             'name': 'Romaguera-Crona'},
 'email': 'Sincere@april.biz',
 'id': 1,
 'name': 'Leanne '
         'Graham',
 'phone': '1-770-736-8031 '
          'x56442',
 'username': 'Bret',
 'website': 'hildegard.org'}

```

It’s hard to get Python’s `pprint()` to print ugly. It’ll do everything it can to be pretty!

In this example, on top of learning about `width`, you’re also exploring how the printer splits up long lines of text. Note how `users[0]["company"]["catchPhrase"]`, which was initially `'Multi-layered client-server neural-net'`, has been split on each space. The printer avoids dividing this string mid-word because that would make it hard to read.

[](https://img.realpython.net/4abc783883f79f916711682eb20f448e)

### Squeezing Your Long Sequences: `compact`

You might think that `compact` refers to the behavior you explored in the section about `width`—that is, whether `compact` makes data structures appear on one line or separate lines. However, `compact` only affects the output once a line goes *over* the `width`.

**Note:** `compact` only affects the output of sequences: lists, sets, and tuples, and *not* dictionaries. This is intentional, though it’s not clear why this decision was taken. There’s an ongoing discussion about that in [Python Issue #34798](https://bugs.python.org/issue34798).

If `compact` is `True`, then the output will wrap onto the next line. The default behavior is for each element to appear on its own line if the data structure is longer than the width:

```
>>> pprint(users, depth=1)
[{...}, {...}, {...}, {...}, {...}, {...}, {...}, {...}, {...}, {...}]

>>> pprint(users, depth=1, width=40)
[{...},
 {...},
 {...},
 {...},
 {...},
 {...},
 {...},
 {...},
 {...},
 {...}]

>>> pprint(users, depth=1, width=40, compact=True)
[{...}, {...}, {...}, {...}, {...},
 {...}, {...}, {...}, {...}, {...}]

```

Pretty-printing this list using the default settings prints out the abbreviated version on one line. Limiting `width` to `40` characters, you force `pprint()` to output all the list’s elements on separate lines. If you then set `compact=True`, then the list will wrap at forty characters and be more compact than it would typically look.

**Note:** Beware that setting the width to less than seven characters— which, in this case, is equivalent to the `[{...},` output— seems to bypass the `depth` argument completely, and `pprint()` ends up printing everything without any folding. This has been reported as [bug #45611](https://bugs.python.org/issue45611).

`compact` is useful for long sequences with short elements that would otherwise take up many lines and make the output less readable.

### Directing Your Output: `stream`

The `stream` parameter refers to the output of `pprint()`. By default, it goes to the same place that `print()` goes to. Specifically, it goes to [`sys.stdout`](https://docs.python.org/3/library/sys.html#sys.stdout), which is actually a [file object](https://docs.python.org/3/glossary.html#term-file-object) in Python. However, you can redirect this to any file object, just like you can with `print()`:

```
>>> with open("output.txt", mode="w") as file_object:
...     pprint(users, stream=file_object)

```

Here you create a file object with [`open()`](https://docs.python.org/3/library/functions.html#open), and then you set the `stream` parameter in `pprint()` to that file object. If you then open the `output.txt` file, you should see that you’ve pretty-printed everything in `users` there.

Python does have its own [logging module](https://realpython.com/python-logging/). However, you can also use `pprint()` to send pretty outputs to files and have these act as logs if you prefer.

### Preventing Dictionary Sorting: `sort_dicts`

Although dictionaries are generally considered unordered data structures, since Python 3.6, [dictionaries are ordered by insertion](https://docs.python.org/3.6/whatsnew/3.6.html#new-dict-implementation).

`pprint()` orders the keys alphabetically for printing:

```
>>> pprint(users[0], depth=1)
{'address': {...},
 'company': {...},
 'email': 'Sincere@april.biz',
 'id': 1,
 'name': 'Leanne Graham',
 'phone': '1-770-736-8031 x56442',
 'username': 'Bret',
 'website': 'hildegard.org'}

>>> pprint(users[0], depth=1, sort_dicts=False)
{'id': 1,
 'name': 'Leanne Graham',
 'username': 'Bret',
 'email': 'Sincere@april.biz',
 'address': {...},
 'phone': '1-770-736-8031 x56442',
 'website': 'hildegard.org',
 'company': {...}}

```

Unless you set `sort_dicts` to `False`, Python’s `pprint()` sorts the keys alphabetically. It keeps the output for dictionaries consistent, readable, and—well—pretty!

When `pprint()` was first implemented, dictionaries were unordered. Without alphabetically ordering the keys, a dictionary’s keys could have theoretically differed at each print.

### Prettifying Your Numbers: `underscore_numbers`

The `underscore_numbers` parameter is a feature introduced in [Python 3.10](https://realpython.com/python310-new-features/) that makes long numbers more readable. Considering that the example you’ve been using so far doesn’t contain any long numbers, you’ll need a new example to try it out:

```
>>> number_list = [123456789, 10000000000000]
>>> pprint(number_list, underscore_numbers=True)
[123_456_789, 10_000_000_000_000]

```

If you tried running this call to `pprint()` and got an error, you’re not alone. As of October 2021, this argument doesn’t work when calling `pprint()` directly. The Python community noticed this quickly, and it’s [been fixed](https://github.com/python/cpython/pull/29133) in the December 2021 [3.10.1 bug fix release](https://www.python.org/dev/peps/pep-0619/#bugfix-releases). The folks at Python care about their pretty printer! They’ll probably have fixed this by the time you’re reading this tutorial.

If `underscore_numbers` doesn’t work when you call `pprint()` directly and you really want pretty numbers, there is a workaround: When you create your own `PrettyPrinter` object, this parameter should work just like it does in the example above.

Next, you’ll cover how to create a `PrettyPrinter` object.

[](https://img.realpython.net/2f88361b887b78ff6d7d0ccb73261a45)

## Creating a Custom `PrettyPrinter` Object

It’s possible to create an instance of `PrettyPrinter` that has defaults you’ve defined. Once you have this new instance of your custom `PrettyPrinter` object, you can use it by calling the `.pprint()` method on the `PrettyPrinter` instance:

```
>>> from pprint import PrettyPrinter
>>> custom_printer = PrettyPrinter(
...     indent=4,
...     width=100,
...     depth=2,
...     compact=True,
...     sort_dicts=False,
...     underscore_numbers=True
... )
...
>>> custom_printer.pprint(users[0])
{   'id': 1,
    'name': 'Leanne Graham',
    'username': 'Bret',
    'email': 'Sincere@april.biz',
    'address': {   'street': 'Kulas Light',
                   'suite': 'Apt. 556',
                   'city': 'Gwenborough',
                   'zipcode': '92998-3874',
                   'geo': {...}},
    'phone': '1-770-736-8031 x56442',
    'website': 'hildegard.org',
    'company': {   'name': 'Romaguera-Crona',
                   'catchPhrase': 'Multi-layered client-server neural-net',
                   'bs': 'harness real-time e-markets'}}
>>> number_list = [123456789, 10000000000000]
>>> custom_printer.pprint(number_list)
[123_456_789, 10_000_000_000_000]

```

With these commands, you:

- **Imported** `PrettyPrinter`, which is a class definition
- Created a **new instance** of that class with certain parameters
- **Printed** the first user in `users`
- Defined a **list** of a couple of long numbers
- **Printed `number_list`**, which also demonstrates `underscore_numbers` in action

Note that the arguments you passed to `PrettyPrinter` are exactly the same as the default `pprint()` arguments, except that you skipped the first parameter. In `pprint()`, this is the object you want to print.

This way, you can have various printer presets—perhaps some going to different streams—and call them when you need them.

## Getting a Pretty String With `pformat()`

What if you don’t want to send the pretty output of `pprint()` to a stream? Perhaps you want to do some [regex](https://realpython.com/regex-python/) matching and replace certain keys. For plain dictionaries, you might find yourself wanting to remove the brackets and quotes to make them look even more human-readable.

Whatever it is that you might want to do with the string pre-output, you can get the string by using [`pformat()`](https://docs.python.org/3/library/pprint.html#pprint.pformat):

```
>>> from pprint import pformat
>>> address = pformat(users[0]["address"])
>>> chars_to_remove = ["{", "}", "'"]
>>> for char in chars_to_remove:
...     address = address.replace(char, "")
...
>>> print(address)
city: Gwenborough,
 geo: lat: -37.3159, lng: 81.1496,
 street: Kulas Light,
 suite: Apt. 556,
 zipcode: 92998-3874

```

`pformat()` is a tool you can use to get between the pretty printer and the output stream.

Another use case for this might be if you’re [building an API](https://realpython.com/api-integration-in-python/#rest-and-python-building-apis) and want to send a pretty string representation of the JSON string. Your end users would probably appreciate it!

## Handling Recursive Data Structures

Python’s `pprint()` is recursive, meaning it’ll pretty-print all the contents of a dictionary, all the contents of any child dictionaries, and so on.

Ask yourself what happens when a recursive function runs into a recursive data structure. Imagine that you have dictionary `A` and dictionary `B`:

- `A` has one attribute, `.link`, which points to `B`.
- `B` has one attribute, `.link`, which points to `A`.

If your imaginary recursive function has no way to handle this circular reference, it’ll never finish printing! It would print `A` and then its child, `B`. But `B` also has `A` as a child, so it would go on into infinity.

Luckily, both the normal `print()` function and the `pprint()` function handle this gracefully:

```
>>> A = {}
>>> B = {"link": A}
>>> A["link"] = B
>>> print(A)
{'link': {'link': {...}}}
>>> from pprint import pprint
>>> pprint(A)
{'link': {'link': <Recursion on dict with id=3032338942464>}}

```

While Python’s regular `print()` just abbreviates the output, `pprint()` explicitly notifies you of recursion and also adds the ID of the dictionary.

If you want to explore why this structure is recursive, you can learn more about [passing by reference](https://realpython.com/python-pass-by-reference/).

[](https://img.realpython.net/cc86980015e727765da60f4377ac2185)

## Conclusion

You’ve explored the primary usage of the `pprint` module in Python and some ways to work with `pprint()` and `PrettyPrinter`. You’ll find that `pprint()` is especially handy whenever you’re developing something that deals with complex data structures. Maybe you’re developing an application that uses an unfamiliar API. Perhaps you have a data warehouse full of deeply-nested JSON files. These are all situations where `pprint` can come in handy.

In this tutorial, you’ve learned how to:

- **Import** `pprint` for use in your programs
- Use **`pprint()`** in place of the regular `print()`
- Understand all the **parameters** you can use to customize your pretty-printed output
- Get the formatted output as a **string** before printing it
- Create a custom instance of **`PrettyPrinter`**
- Recognize **recursive data structures** and how `pprint()` handles them

To help you get to grips with the function and parameters, you used an example of a data structure representing some users. You also explored some situations where you might use `pprint()`.

Congratulations! You’re now better equipped to deal with complex data by using Python’s `pprint` module.

🐍 Python Tricks 💌

![](Prettify%20Your%20Data%20Structures%20With%20Pretty%20Print%20in%20367332a2a5ab42f4a036b1259c618d78/pytrick-dict-merge.4201a0125a5e.png)

About **Ian Currie**

*Each tutorial at Real Python is created by a team of developers so that it meets our high quality standards. The team members who worked on this tutorial are:*

Master Real-World Python Skills
With Unlimited Access to Real Python

![](Prettify%20Your%20Data%20Structures%20With%20Pretty%20Print%20in%20367332a2a5ab42f4a036b1259c618d78/lesson-locked.f5105cfd26db.svg)

**Join us and get access to hundreds of tutorials, hands-on video courses, and a community of expert Pythonistas:**