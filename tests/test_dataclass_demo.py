import pytest

from dataclass_demo import Banana, Puppy


def test_banana_created_corectly_with_args():
    banana = Banana(120, 3, 'Chiquita')
    assert banana.weight_grams == 120
    assert banana.curvature == 3
    assert banana.brand_name == 'Chiquita'


def test_banana_created_corectly_with_kwargs():
    banana = Banana(curvature=3, brand_name='Chiquita', weight_grams=120)
    assert banana.weight_grams == 120
    assert banana.curvature == 3
    assert banana.brand_name == 'Chiquita'


def test_puppy_created_corectly_with_args():
    puppy = Puppy(200, 4, 'Daisy')
    assert puppy.age_days == 200
    assert puppy.leg_count == 4
    assert puppy.name == 'Daisy'


def test_puppy_created_corectly_with_kwargs():
    puppy = Puppy(age_days=200, leg_count=4, name='Daisy')
    assert puppy.age_days == 200
    assert puppy.leg_count == 4
    assert puppy.name == 'Daisy'


def test_can_alter_properties_of_banana():
    banana = Banana(curvature=3, brand_name='Chiquita', weight_grams=120)
    banana.curvature = 4
    assert banana.curvature == 4


def test_can_alter_properties_of_puppy():
    puppy = Puppy(age_days=200, leg_count=4, name='Daisy')
    puppy.name = 'Molly'
    assert puppy.name == 'Molly'


def test_can_compare_bananas():
    assert Banana(100, 2, 'Noboa') == Banana(brand_name='Noboa', curvature=2, weight_grams=100)


def test_can_compare_puppies():
    assert Puppy(300, 4, 'Luna') == Puppy(leg_count=4, age_days=300, name='Luna')


def test_can_not_compare_bananas_with_puppies():
    banana = Banana(150, 4, 'Chiquita')
    puppy = Puppy(150, 4, 'Chiquita')
    assert banana != puppy
