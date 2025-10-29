"""
Gradient descent for linear regression

yhat = wx + b

loss = mse = (y-yhat)**2 / N (samples)

optimal parameters to reduce loss
"""

import numpy as np

# intialize params
X = np.random.randn(10, 1)
Y = 5*X + np.random.rand()

# parameters
w = 0.0
b = 0.0

# hyperparameters
learning_rate = 0.01

# create gradient descent function
def descent(X, Y, w, b, learning_rate):
    dldw = 0.0
    dldb = 0.0

    N = X.shape[0]

    # loss = (y - (wx+b))**2 
    for xi, yi in zip(X, Y):
        dldw += 2 * (yi - (w * xi + b)) * -xi
        dldb += 2 * (yi - (w * xi + b)) * -1

    # updates
    w = w - learning_rate * (1/N) * dldw
    b = b - learning_rate * (1/N) * dldb

    return w, b


# iteratively make updates
for epoch in range(400):
    w, b = descent(X, Y, w, b, learning_rate)
    yhat = w * X + b
    loss = np.divide(np.sum((Y - yhat)**2, axis=0), X.shape[0])

    print(f"For epoch: {epoch}, loss: {loss}, parameters w: {w}, b: {b}")