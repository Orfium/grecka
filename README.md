# grecka

Grecka is a python script to convert Greek to Greeklish based on ELOT 743 (the standard conversion prototype ).

# Install

To install from source run the following commands:

~~~
$ python setup.py bdist_wheel
$ pip install dist/grecka-{version}-py3-none-any.whl
~~~

Remember to replace the version to your current (0.0.1) version.

How to use
----------

Via python:

~~~python
from grecka.convert import Grecka

print(Grecka.toGreeklish("Ελληνικό κείμενο"))
~~~

Via the entrypoint CLI:

~~~
$ grecka to-greeklish "Ελληνικό κείμενο"
~~~

Methods
-------

`Grecka` is a class with one static method that you can use. 

**Prototype**: `toGreeklish(greekText)` --> Returns the string to its
ELOT 743 greeklish representation.
