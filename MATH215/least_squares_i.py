# -*- coding: utf-8 -*-
"""Least_squares_I.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/146creYltd62T-fmkbijLPorGTqOMpRrJ

#**Lab 6 - Least squares I**

Enter your code in the spaces provided. Do not change any of the variable names or function names that are already provided for you. In places where we specify the name of the return value, make sure that your code produces the a value with the correct name.
"""

# Do not edit this cell.

LabID="Lab6"

try:
  from graderHelp import ISGRADEPLOT
except ImportError:
  ISGRADEPLOT = True

"""**Enter your name, section number, and BYU NetID**"""

# Enter your first and last names in between the quotation marks.

first_name="David"

last_name="Haroldsen"

# Enter your Math 215 section number in between the quotation marks.

section_number="2"

# Enter your BYU NetID in between the quotation marks.  NOT YOUR BYU ID NUMBER!

BYUNetID="davedude"

"""**Import NumPy**"""

import numpy as np

"""**Problem 1**"""

# Replace the values of 0 with the NumPy arrays from Problem 1.

X1=np.array([[1, n] for n in range(5, 55, 5)])

Y1=np.array([3.33, 4.43, 4.39, 5.23, 5.67, 6.06, 7.01, 7.16, 8.03, 8.78])

"""**Problem 2**"""

# Replace the values of 0 with the normal equation coefficient matrix and normal equation right-hand side respectively from Problem 2.

normal_coef1=np.transpose(X1) @ X1

normal_vect1=np.transpose(X1) @ Y1

"""**Problem 3**"""

# Replace the value of 0 with the least squares solution beta1 you found in Problem 3.

beta1=np.linalg.solve(normal_coef1, normal_vect1)

# Define a function whose graph is the line of best fit.

def ls1_line(x):
  return beta1[0] + beta1[1] * x

import matplotlib.pyplot as plt

# Construct your plot of ls1_line and the corresponding data points here. Put all of your code to create the plots inside the function below.

def create_plots1():
  x = np.linspace(0, 50, 100)
  pred = ls1_line(x)
  plt.plot(x, pred)
  plt.plot(X1[:,1],Y1,'.',markersize=5,alpha=1)
  plt.show()
  return None

# Replace the value of 0 with your prediction of the satellite's velocity at t=60.

pred1=ls1_line(60)

"""**Problem 4**"""

# Replace the values of 0 with the NumPy arrays from Problem 4.

X2=np.array([[n, n**2] for n in range(5, 55, 5)])

Y2=np.array([20.57, 87.48, 197.45, 347.67, 546.12, 784.35, 1066.02, 1390.97, 1761.85, 2177.34])

"""**Problem 5**"""

# Replace the values of 0 with the normal equation coefficient matrix and normal equation right-hand side, and least squares solution from Problem 5.

normal_coef2=np.transpose(X2) @ X2

normal_vect2=np.transpose(X2) @ Y2

beta2=np.linalg.solve(normal_coef2, normal_vect2)

"""**Problem 6**"""

# Define a function whose graph is the parabola of best fit.

def ls2_par(x):
  # Put your code here.
  return beta2[0] * x + beta2[1] * x * x

# Construct your plot of ls2_par and the corresponding data points here. Put all of your code to create the plots inside the function below.

def create_plots2():
  x = np.linspace(0, 50, 100)
  pred = ls2_par(x)
  plt.plot(x, pred)
  plt.plot(X2[:,0],Y2,'.',markersize=5,alpha=1)
  plt.show()
  return None

# Replace the value of 0 with your prediction of the satellite's position at t=60.

pred2=ls2_par(60)

create_plots2()

"""**Problem 7**"""

# Replace the values of 0 with the NumPy arrays from Problem 7.

X3=np.array([[1, np.log(T)] for T in [87.77, 224.70, 365.25, 686.95, 4332.62, 10759.2]])

Y3=np.log(np.array([0.389, 0.724, 1, 1.524, 5.2, 9.510]))

# Replace the values of 0 with the normal equation coefficient matrix and normal equation right-hand side from Problem 7.

normal_coef3=np.transpose(X3) @ X3

normal_vect3=np.transpose(X3) @ Y3


# Replace the value of 0 with the least squares solution from Problem 7.

beta3=np.linalg.solve(normal_coef3, normal_vect3)

"""**Problem 8**"""

# Replace the values of 0 with your predictions for the semi-major axes of Uranus and Neptune.

def pred(T):
  return np.exp(beta3[0]) * (T ** beta3[1])

pred_Uran=pred(30687.15)

pred_Nept=pred(60190.03)

"""**STOP!  BEFORE YOU SUBMIT THIS LAB:**  Go to the "Runtime" menu at the top of this page, and select "Restart and run all".  If any of the cells produce error messages, you will either need to fix the error(s) or delete the code that is causing the error(s).  Then use "Restart and run all" again to see if there are any new errors.  Repeat this until no new error messages show up.

**You are not ready to submit until you are able to select "Restart and run all" without any new error messages showing up.  Your code will not be able to be graded if there are any error messages.**

To submit your lab for grading you must first download it to your compute as .py file. In the "File" menu select "Download .py". The resulting file can then be uploaded to [gradescope.com](https://gradescope.com) for grading.
"""