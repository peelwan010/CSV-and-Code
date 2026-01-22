"""
math_validation.py

Exploratory symbolic and numerical validation routines used during
the development of matrix-based analytical methods.

This module exists to verify mathematical expressions and inspect
their behavior using numerical integration (SciPy) and symbolic
integration (SymPy). It is intentionally separated from the main
computation pipeline to keep execution logic focused and clean.

The code here reflects validation and sanity-checking steps rather
than production computation.
"""

import numpy as np
from scipy import integrate
import sympy as sp


def numerical_integration_example():
    """
    Perform a simple numerical integration to validate
    constant or slowly varying analytical expressions.

    Returns:
    - result (float): numerical integral value
    - error (float): estimated numerical error
    """
    f = lambda x: np.exp(0.34e-5)
    result, error = integrate.quad(f, 0, 1)
    return result, error


def symbolic_integration_example():
    """
    Perform symbolic integration to inspect closed-form
    behavior of mathematically derived expressions.

    Returns:
    - integral (sympy expression): symbolic integral result
    """
    x, a = sp.symbols("x a", positive=True)
    expression = 1 / (x**4 * sp.sqrt(x**2 - a**2))
    integral = sp.integrate(expression, x)
    return integral


def symbolic_data_integration_example(data_expression):
    """
    Symbolically integrate a data-derived expression with
    respect to its variable to inspect analytical behavior.

    Parameters:
    - data_expression (sympy expression): expression to integrate

    Returns:
    - sympy expression: symbolic integral
    """
    x = sp.symbols("x")
    return sp.integrate(data_expression, x)


if __name__ == "__main__":
    numerical_result = numerical_integration_example()
    symbolic_result = symbolic_integration_example()

    print("Numerical integration result:", numerical_result)
    print("Symbolic integration result:", symbolic_result)
