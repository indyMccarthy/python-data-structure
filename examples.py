if __name__ == '__main__':

phonebook = {
    "bob": 7387,
    "alice": 3719,
    "jack": 7052,
}

squares = {x: x * x for x in range(6)}

import collections
d = collections.OrderedDict(one=1, two=2, three=3)

from collections import defaultdict
dd = defaultdict(list)

# Accessing a missing key creates it and
# initializes it using the default factory,
# i.e. list() in this example:
dd["dogs"].append("Rufus")
dd["dogs"].append("Kathrin")

# concat multiple dicts
# chain contient les pointeurs vers les dicts
# les dicts peuvent être modifié et pris en
# compte sans redéfinition de la variable 'chain'
from collections import ChainMap
dict1 = {"one": 1, "two": 2}
dict2 = {"three": 3, "four": 4}
chain = ChainMap(dict1, dict2)
dict1["five"]=5
chain["five"]

from types import MappingProxyType
read_only = MappingProxyType(dict1)

# Tableau de float
import array
arr = array.array("f", (1.0, 1.5, 2.0, 2.5))

# Immutable array of single bytes < 256
arr = bytes((0, 1, 2, 3))
arr[1]

# Mutable
arr = bytearray((0, 1, 2, 3))


# create Numpy array
from numpy import array
l = [1.0, 2.0, 3.0]
a = array(l)
print(a)
print(a.shape)
print(a.dtype)

# Création d'une class avec attributs typés
from dataclasses import dataclass, fields
from pydantic import validate_arguments


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



from collections import Counter
inventory = Counter()

loot = {"sword": 1, "bread": 3}
inventory.update(loot)
inventory
#Counter({'bread': 3, 'sword': 1})

more_loot = {"sword": 1, "apple": 1}
inventory.update(more_loot)
#inventory
