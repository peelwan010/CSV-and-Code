"""
matrix_operations.py

Independent implementations of matrix-based and numerical computations
developed to support analytical problem solving.

The focus of this module is clarity of logic, correctness of computation,
and translating derived mathematical relationships into executable Python code.

This module also includes visualization routines to validate and
inspect relationships between input variables and the derived output (X3).
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def generate_random_parameters(size=3000):
    """
    Generate random numerical parameters used as placeholders
    for structured scientific input data.
    """
    k12 = np.random.random(size)
    I1 = np.random.random(size)
    m12 = np.random.random(size)

    k21 = np.random.random(size)
    I2 = np.random.random(size)
    m21 = np.random.random(size)

    return k12, I1, m12, k21, I2, m21


def compute_normalized_terms(k, m, I):
    """
    Compute normalized and sign-inverted terms used
    in matrix-based analytical relationships.
    """
    k_over_I = k / I
    m_over_I = m / I

    negative_k_over_I = -k_over_I
    negative_m_over_I = -m_over_I

    return k_over_I, m_over_I, negative_k_over_I, negative_m_over_I


def build_matrix(k_I, m_I, neg_k_I, neg_m_I):
    """
    Construct a matrix using derived and normalized terms.

    The structure and sign symmetry of this matrix are defined
    by analytical constraints derived during problem formulation.
    """
    value_pool = np.array([k_I, m_I, neg_k_I, neg_m_I])
    sampled_values = np.random.choice(value_pool.ravel(), 4, replace=False)

    matrix = np.matrix(
        [
            [0, 1, 0, 0],
            sampled_values,
            [0, 0, 0, 1],
            sampled_values.copy(),
        ],
        dtype=object,
    )

    # Enforce analytical sign symmetry
    matrix[1, 2] = -matrix[1, 0]
    matrix[1, 3] = -matrix[1, 1]
    matrix[3, 0] = -matrix[3, 2]
    matrix[3, 1] = -matrix[3, 3]

    return matrix


def load_input_data():
    """
    Load structured input data from CSV files.
    """
    X1 = pd.read_csv("data/X1.csv").to_numpy().ravel()
    X2 = pd.read_csv("data/X2.csv").to_numpy().ravel()
    X2_diff = pd.read_csv("data/X2_diff.csv").to_numpy().ravel()

    return X1, X2, X2_diff


def compute_X3(k12, I1, m12, X1, X2, X2_diff):
    """
    Compute the derived output variable X3 using a
    matrix-based analytical relationship.

    This function implements a derived computational method
    that was essential for obtaining analytical results.
    """
    return ((k12 * X1) - (I1 * X2_diff) + (m12 * X2)) / k12


# ----------------------- Visualization -----------------------

def plot_primary_variables(X1, X2, X3):
    """
    Plot X1, X2, and X3 together to visually compare
    their relative behavior.
    """
    plt.figure(figsize=(10, 5))
    plt.plot(X1, label="X1", alpha=0.7)
    plt.plot(X2, label="X2", alpha=0.7)
    plt.plot(X3, label="X3", alpha=0.9)
    plt.xlabel("Sample Index")
    plt.ylabel("Value")
    plt.title("Comparison of X1, X2, and Derived X3")
    plt.legend()
    plt.tight_layout()
    plt.show()


def plot_parameter_distributions(k12, I1, m12):
    """
    Plot distributions of key parameters used in X3 computation.
    """
    plt.figure(figsize=(10, 5))
    plt.hist(k12, bins=50, alpha=0.6, label="k12")
    plt.hist(I1, bins=50, alpha=0.6, label="I1")
    plt.hist(m12, bins=50, alpha=0.6, label="m12")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.title("Distributions of Parameters")
    plt.legend()
    plt.tight_layout()
    plt.show()


def plot_X3_relationship(X1, X2, X3):
    """
    Scatter-based visualization showing how X3 varies
    with respect to X1 and X2.
    """
    plt.figure(figsize=(10, 5))
    plt.scatter(X1, X3, alpha=0.6, label="X3 vs X1")
    plt.scatter(X2, X3, alpha=0.6, label="X3 vs X2")
    plt.xlabel("Input Variables")
    plt.ylabel("X3")
    plt.title("Relationship Between Inputs and Derived X3")
    plt.legend()
    plt.tight_layout()
    plt.show()


def plot_final_X3(X3):
    """
    Final standalone plot of the derived variable X3.
    """
    plt.figure(figsize=(10, 5))
    plt.plot(X3, color="black")
    plt.xlabel("Sample Index")
    plt.ylabel("X3")
    plt.title("Final Derived Output Variable (X3)")
    plt.tight_layout()
    plt.show()


# ----------------------- Main Execution -----------------------

def main():
    k12, I1, m12, k21, I2, m21 = generate_random_parameters()

    X1_data, X2_data, X2_diff_data = load_input_data()

    X1 = np.random.choice(X1_data, size=3000)
    X2 = np.random.choice(X2_data, size=3000)
    X2_diff = np.random.choice(X2_diff_data, size=3000)

    X3 = compute_X3(k12, I1, m12, X1, X2, X2_diff)

    # Visualization for analytical validation
    plot_primary_variables(X1, X2, X3)
    plot_parameter_distributions(k12, I1, m12)
    plot_X3_relationship(X1, X2, X3)
    plot_final_X3(X3)

    return X3


if __name__ == "__main__":
    X3_result = main()
