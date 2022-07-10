"""
Usage of a module may be 'deprecated', which means that it may
be removed from a future Python release. The rationale for
deprecating a module is also collected in this PEP.
If the rationale turns out faulty, the module may become
'undeprecated'.

If you need to mark a function or a method as deprecated,
you can use the @deprecated decorator:
"""
#  $ pip install Deprecated

from deprecated import deprecated


@deprecated(version='1.2.1', reason="You should use another function")
def some_old_function(x, y):
    return x + y


class SomeClass(object):
    @deprecated(version='1.3.0', reason="This method is deprecated")
    def some_old_method(self, x, y):
        return x + y


some_old_function(12, 34)
obj = SomeClass()
obj.some_old_method(5, 8)


#  OutPut:
    # $ python hello.py
    # hello.py:15: DeprecationWarning: Call to deprecated function (or staticmethod) some_old_function.
    # (You should use another function) -- Deprecated since version 1.2.0.
    #   some_old_function(12, 34)
    # hello.py:17: DeprecationWarning: Call to deprecated method some_old_method.
    # (This method is deprecated) -- Deprecated since version 1.3.0.
    #   obj.some_old_method(5, 8)











