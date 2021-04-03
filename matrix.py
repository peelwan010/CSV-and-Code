import numpy as np
import random
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

k12 = np.array([random.random() for _ in range(3000)])
I1 = np.array([random.random() for _ in range(3000)])
m12 = np.array([random.random() for _ in range(3000)])
_k12 = np.array([-x for x in k12])
_m12 = np.array([-x for x in m12])

k21 = np.array([random.random() for _ in range(3000)])
I2 = np.array([random.random() for _ in range(3000)])
m21 = np.array([random.random() for _ in range(3000)])
_k21 = np.array([-x for x in k21])
_m21 = np.array([-x for x in m21])

k12_I1 = np.array([i / j for i, j in zip(k12, I1)])
m12_I1 = np.array([i / j for i, j in zip(m12, I1)])
_k12_I1 = np.array([i / j for i, j in zip(_k12, I1)])
_m12_I1 = np.array([i / j for i, j in zip(_m12, I1)])

k21_I2 = np.array([i / j for i, j in zip(k21, I2)])
m21_I2 = np.array([i / j for i, j in zip(m21, I2)])
_k21_I2 = np.array([i / j for i, j in zip(_k21, I2)])
_m21_I2 = np.array([i / j for i, j in zip(_m21, I2)])

post_2 = np.array([k12_I1, m12_I1, _k12_I1, _m12_I1])
post_4 = np.array([k12_I1, m12_I1, _k12_I1, _m12_I1])

ran_post_2 = np.random.choice(post_2.ravel(),4,replace=False)
ran_post_4 = np.random.choice(post_4.ravel(),4,replace=False)

mat1 = np.matrix([[0,1,0,0],(ran_post_2),
                [0,0,0,1],(ran_post_4)],dtype=object)

second_0 = mat1[1,0]
mat1[1,2] = -(second_0)
second_1 = mat1[1,1]
mat1[1,3] = -(second_1)

fourth_2 = mat1[3,2]
mat1[3,0] = -(fourth_2)
fourth_3 = mat1[3,3]
mat1[3,1] = -(fourth_3)

# len(str(mat1[1,1]))

# print('• Matrix formed from random values of K, μ & I:-')
space=''
print(space)
# print(mat1)
print(space)

# x1 = random.randint(0,3000)
# x2 = random.randint(0,3000)
# x3 = random.randint(0,3000)
# x4 = random.randint(0,3000)

# X = np.matrix([[x1, x2, x3, x4]])
# print('• Matrix with X1, X2, X3 and X4:-')
# print(space)
# print(X)
# print(space)

# print('• Values of Y1, Y2, Y3, Y4 wrt K, μ & I * X1, X2, X3 and X4 ')
# print(space)
# Y = mat1.dot(X.T)
# print(Y)

# print(space)
# print ("Matrix Division : ")
# print (np.divide(Y,X))

# # Integration of X2 when C = 0 and x = 1
# x = sp.Symbol('x') 
# i = sp.integrate(inte, x)
# print(i)

X1_rd = np.array(pd.read_csv(r"C:/Users/Lenovo/Desktop/Temp/X1.csv"))
X2_rd = np.array(pd.read_csv(r"C:/Users/Lenovo/Desktop/Temp/X2.csv"))
X2_diff_rd = np.array(pd.read_csv(r"C:/Users/Lenovo/Desktop/Temp/X2_diff.csv"))

X1 = np.random.choice(X1_rd.ravel(),1,replace=False)
X2 = np.random.choice(X2_rd.ravel(),1,replace=False)
X2_diff = np.random.choice(X2_diff_rd.ravel(),1,replace=False)

k12_1 = np.random.choice(k12.ravel(),1,replace=False)
I1_1 = np.random.choice(I1.ravel(),1,replace=False)
m12_1 = np.random.choice(m12.ravel(),1,replace=False)

# X3 = ((k12_1*X1)-(I1_1*X2_diff)+(m12_1*X2))/k12_1
X3 = ((k12*X1)-(I1*X2_diff)+(m12*X2))/k12
# X3 = np.random.choice(X3_all.ravel(),3000,replace=False)

##############################################################################
# import scipy.integrate
# from numpy import exp
# f= lambda x:exp(0.34e-5)
# i = scipy.integrate.quad(f, 0, 1)
# print (i)

# from sympy import *
# init_printing(use_unicode=False, wrap_line=False)
# x = Symbol('x')
# i = integrate(2.54e-2)

#import sympy
# 1/(x^4(sqrt(x^2-a^2))), a > 0
#x, a = sympy.symbols('x, a')
#exp = X2_rd
#exp_int = sympy.integrate(exp, x)
#print(exp_int)


