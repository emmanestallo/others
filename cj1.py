import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd 
 
#pearson correlation coefficient
x = np.array([int(i) for i in input("Enter values of x: ").split(",")])
y = np.array([int(j) for j in input("Enter values of y: ").split(",")])


#linear_regression
x_hat = np.sum(x)/len(x)
y_hat = np.sum(y)/len(y) 

a = x - x_hat 
b = y - y_hat 

ab = np.multiply(a,b)
a_sq = a**2 
b_sq = b**2 

r_val = np.sum(ab)/np.sqrt((np.sum(a_sq)*np.sum(b_sq)))
#slope and y-intercept 

m = np.sum(ab)/np.sum(a_sq)
y_int = y_hat - m*x_hat 

table = {   'x': x,
            'y': y, 
            'a': a,
            'b': b,
            'ab': ab,
            'a^2': a_sq,
            'b^2': b_sq 
}

df = pd.DataFrame(table, columns = ['x','y','a','b','ab','a^2','b^2'], index=[f'Data {i+1}' for i in range(len(x))])

print(df)
print(f'Pearson Correlation Coefficient (r) = {round(r_val,3)}')
print(f'Slope: {round(m,3)}, y-intercept: {round(y_int,3)}')