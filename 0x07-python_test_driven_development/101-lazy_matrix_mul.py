#!/usr/bin/python3

"""a module module contains a function that multiplies two matrices with
the help of an external module"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices. """
    return (np.matmul(m_a, m_b))
