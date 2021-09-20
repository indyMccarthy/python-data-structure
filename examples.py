#if __name__ == '__main__':

# Dictionnaries
phonebook = {
    "bob": 7387,
    "alice": 3719,
    "jack": 7052,
}

squares = {x: x * x for x in range(6)}

# OrderedDict
import collections
d = collections.OrderedDict(one=1, two=2, three=3)

# defaultdict
from collections import defaultdict
dd = defaultdict(list)

# Accessing a missing key creates it and
# initializes it using the default factory,
# i.e. list() in this example:
dd["dogs"].append("Rufus")
# A new list containing "Rufus" is created and associated to the key "dogs"
dd["dogs"].append("Kathrin")

# ChainMap
# concat multiple dicts
# chain contient les pointeurs vers les dicts
# les dicts peuvent être modifié et pris en
# compte sans redéfinition de la variable 'chain'
from collections import ChainMap
dict1 = {"one": 1, "two": 2}
dict2 = {"three": 3, "four": 4}
chain = ChainMap(dict1, dict2)
dict1["five"]=5
print(chain["five"])

# Read only dict
from types import MappingProxyType
read_only = MappingProxyType(dict1)

# Tableau typé de float
import array
arr = array.array("f", (1.0, 1.5, 2.0, 2.5))

# Immutable array of single bytes < 256
arr = bytes((0, 1, 2, 3))
print(arr[1])

# Mutable array of single bytes
arr = bytearray((0, 1, 2, 3))


# create Numpy array
from numpy import array
l = [1.0, 2.0, 3.0]
a = array(l)
print(a)
print(a.shape)
print(a.dtype)
# [1. 2. 3.]
# (3,)
# float64

# Création d'une class avec attributs typés
from dataclasses import dataclass, fields
from pydantic import validate_arguments

# Validate argument allows to pass numeric as String and understand cast True as 1.0
# It throws an error if mileage="aaa"
@validate_arguments
@dataclass
class Car:
    color: str
    mileage: float
    automatic: bool

    # Add post_init to check data types (or add pydantic validate_arguments decorator)
    def __post_init__(self):
        for field in fields(self):
            value = getattr(self, field.name)
            if not isinstance(value, field.type):
                raise ValueError(f'Expected {field.name} to be {field.type}, '
                                 f'got {repr(value)}')


# Counter allows to aggregate dict with integer as value
# Also allows to count char in a string : c = Counter('abcdeabcdabcaba')
# c.most_common(3)
from collections import Counter
inventory = Counter()

loot = {"sword": 1, "bread": 3}
inventory.update(loot)
inventory
#Counter({'bread': 3, 'sword': 1})

more_loot = {"sword": 1, "apple": 1}
inventory.update(more_loot)
#inventory
#Counter({'bread': 3, 'sword': 2, 'apple': 1})