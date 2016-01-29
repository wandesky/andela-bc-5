To bring dictionary comprehensions into perspective, you might want to know the case
in which you might find them useful.
Most of the time, you'll find them most useful when you have to reverse the keys of
a dictionary to become the values, and the values to become the keys, such that
```python
lookup = {97: 'a', 105: 'i', 107: 'k', 110: 'n', 116: 't', 121: 'y', 122: 'z'}
```
now becomes
```python
lookup = {'a': 97, 'i': 105, 'k': 107, 'n': 110, 't': 116, 'y': 121, 'z': 122}
```

Now, to achieve that, you could do
```python
lookup = {97: 'a', 105: 'i', 107: 'k', 110: 'n', 116: 't', 121: 'y', 122: 'z'}
new_dict = {}
for key, value in lookup.items():
    new_dict[value] = key
print new_dict

```

Or you could *just* do
```python
# Original lookup
lookup = {97: 'a', 105: 'i', 107: 'k', 110: 'n', 116: 't', 121: 'y', 122: 'z'}
print lookup

# Reversed lookup
lookup = {value: key for key, value in lookup.items()}
print lookup

```
Notice in the version using the ```for``` loop, you will have to create a new dictionary.
Using ```dictionary comprehensions``` eliminates the need for that, and you have to admit,
*the code looks infinitely more sexy* :smile:

**You can try that in your Python console.**

*As a side note, if the dictionary is large and you're not using Python 3, you might want to use ```dict.iteritems()``` instead of ```dict.items()``` because of [the reasons explained here.](http://stackoverflow.com/questions/10458437/what-is-the-difference-between-dict-items-and-dict-iteritems)*
