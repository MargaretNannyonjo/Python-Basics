def type_checker(obj):
    if isinstance(obj,(int)):
        raise TypeError("Object is an integer")
    if isinstance(obj,(str)):
        raise TypeError("Object is string")
    if isinstance(obj,(list)):
        raise TypeError("Object is a list")

type_checker([1,2,3])
type_checker(5)
type_checker("star")
