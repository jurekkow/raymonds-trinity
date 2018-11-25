from dataclasses import dataclass

@dataclass
class Banana:
    """
    Cool representation of banana
    >>> banana = Banana(weight_grams=120, curvature=3, brand_name='Chiquita')
    >>> banana.weight_grams
    120
    >>> banana.curvature
    3
    >>> banana.brand_name
    'Chiquita'
    """
    weight_grams: int
    curvature: int
    brand_name: str


@dataclass
class Puppy:
    """
    Cool representation of puppy
    >>> puppy = Puppy(age_days=200, leg_count=4, name='Daisy')
    >>> puppy.age_days
    200
    >>> puppy.leg_count
    4
    >>> puppy.name
    'Daisy'
    """
    age_days: int
    leg_count: int
    name: str


if __name__ == '__main__':
    import doctest
    doctest.testmod()
