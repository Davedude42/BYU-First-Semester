# Remember to import from the lab10 file and pytest
import lab10 as l
import pytest
# Write your test code here for Q1

def test_product():
    assert l.product(1) == 1
    assert l.product(5) == 120

    with pytest.raises(ValueError):
        l.product(0)
    with pytest.raises(ValueError):
        l.product(-1)
    with pytest.raises(ValueError):
        l.product("string")

def test_summation():
    assert l.summation(0) == 0
    assert l.summation(1) == 1
    assert l.summation(5) == 15

    with pytest.raises(ValueError):
        l.summation(-1)
    with pytest.raises(ValueError):
        l.summation("string")


# Q2
#####################################

def test_square():
    assert l.square(2) == 4

def test_sqrt():
    assert l.sqrt(4) == 2

def test_mean():
    assert l.mean([1, 2, 3, 4, 5]) == 3


def test_median():
    assert l.median([2, 3, 4, 5, 6, 7]) == pytest.approx(4.5)


def test_mode():
    assert l.mode([2, 3, 4, 5, 3, 6]) == 3


def test_std_dev():
    assert l.std_dev([1, 2, 3, 4, 5, 6]) == pytest.approx(1.7078251, 0.1)


def test_stat_analysis():
    res = l.stat_analysis([1, 1, 2, 3, 4, 5, 6])

    assert res["mean"] == pytest.approx(3.1428571)
    assert res["median"] == 3
    assert res["mode"] == 1
    assert res["std_dev"] == pytest.approx(1.8070158, 0.1)

    #with pytest.raises(ValueError):
    #    l.stat_analysis("string")
    #with pytest.raises(ValueError):
    #    l.stat_analysis([])


# OPTIONAL
#####################################

def test_accumulate():
    """Write your code here"""


def test_product_short():
    """Write your code here"""


def test_summation_short():
    """Write your code here"""


def test_invert():
    """Write your code here"""


def test_change():
    """Write your code here"""


def test_invert_short():
    """Write your code here"""


def test_change_short():
    """Write your code here"""
