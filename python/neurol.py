import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Hàm sigmoid
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Đạo hàm sigmoid
def sigmoid_derivative(x):
    return x * (1 - x)

class NeuralNetwork:
    def __init__(self, layers, alpha=0.1):
        self.layers = layers
        self.alpha = alpha
        self.W = []
        self.b = []
        self.loss_history = []  # Lưu loss theo epochs
        
        for i in range(len(layers) - 1):
            w_ = np.random.randn(layers[i], layers[i + 1]) / layers[i]
            b_ = np.zeros((layers[i + 1], 1))
            self.W.append(w_)
            self.b.append(b_)

    def fit_partial(self, x, y, epoch):
        print(f"================ Epoch {epoch} ================")
        A = [x]
        for i in range(len(self.layers) - 1):
            x = sigmoid(np.dot(x, self.W[i]) + self.b[i].T)
            A.append(x)
        
        y = y.reshape(-1, 1)
        dA = [-(y / A[-1] - (1 - y) / (1 - A[-1]))]
        dW, db = [], []
        
        for i in reversed(range(len(self.layers) - 1)):
            dw_ = np.dot(A[i].T, dA[-1] * sigmoid_derivative(A[i + 1]))
            db_ = np.sum(dA[-1] * sigmoid_derivative(A[i + 1]), axis=0, keepdims=True).T
            dA_ = np.dot(dA[-1] * sigmoid_derivative(A[i + 1]), self.W[i].T)
            
            dW.append(dw_)
            db.append(db_)
            dA.append(dA_)
        
        dW, db = dW[::-1], db[::-1]
        
        for i in range(len(self.layers) - 1):
            print(f"Layer {i+1}:")
            print(f"  W trước cập nhật: \n{self.W[i]}")
            print(f"  Gradient dW: \n{dW[i]}")
            print(f"  Gradient db: \n{db[i]}")
            
            self.W[i] -= self.alpha * dW[i]
            self.b[i] -= self.alpha * db[i]
            
            print(f"  W sau cập nhật: \n{self.W[i]}")
        print("==============================================\n")
    
    def fit(self, X, y, epochs=100):
        for epoch in range(epochs):
            self.fit_partial(X, y, epoch)
            loss = self.calculate_loss(X, y)
            self.loss_history.append(loss)
            if epoch % 10 == 0:
                print(f"Epoch {epoch}, Loss: {loss}")
    
    def predict(self, X):
        for i in range(len(self.layers) - 1):
            X = sigmoid(np.dot(X, self.W[i]) + self.b[i].T)
        return X
    
    def calculate_loss(self, X, y):
        y_pred = self.predict(X)
        return -np.sum(y * np.log(y_pred) + (1 - y) * np.log(1 - y_pred))

np.random.seed(42)
X_train = np.random.rand(5, 2)
y_train = (X_train[:, 0] + X_train[:, 1] > 1).astype(int)

# Khởi tạo và train mạng neural
nn = NeuralNetwork([2, 2, 1], alpha=0.5)
nn.fit(X_train, y_train, epochs=5)  # Chạy ít epochs để dễ quan sát