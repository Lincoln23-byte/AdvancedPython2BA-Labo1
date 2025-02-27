import pytest
import utils
import math

def test_fact():
    assert utils.fact(5)==120

def test_roots():
    assert utils.roots(1, 2, -3)== (-3, 1)

def test_integrate():
    assert math.isclose(utils.integrate('x**2-1', -1, 1),-4/3,rel_tol=1e-5)
    
