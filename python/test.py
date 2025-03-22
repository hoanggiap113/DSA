import numpy as np

# Hàm sigmoid và đạo hàm
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Khởi tạo đầu vào
x1, x2 = 0.5, 0.6  # Giá trị giả định
X = np.array([[x1, x2]])

y_actual = np.array([[1]])  # Nhãn mong muốn

# Trọng số ban đầu
W1 = np.array([[0.11, 0.12], [0.21, 0.08]])  # Từ input đến hidden layer
W2 = np.array([[0.14], [0.15]])  # Từ hidden layer đến output

# Quá trình huấn luyện
alpha = 0.5  # Learning rate
epochs = 5

for epoch in range(epochs):
    # Forward propagation
    H = sigmoid(np.dot(X, W1))
    Y_est = sigmoid(np.dot(H, W2))
    
    # Tính loss
    loss = 0.5 * (y_actual - Y_est) ** 2
    print(f"Epoch {epoch}: Loss = {loss[0][0]}")
    
    # Backpropagation
    dE_dY = -(y_actual - Y_est)  # Gradient của hàm lỗi
    dY_dH = sigmoid_derivative(Y_est)
    dH_dW2 = H.T
    dE_dW2 = np.dot(dH_dW2, dE_dY * dY_dH)
    
    dH_dW1 = X.T
    dE_dH = np.dot(dE_dY * dY_dH, W2.T) * sigmoid_derivative(H)
    dE_dW1 = np.dot(dH_dW1, dE_dH)
    
    # Cập nhật trọng số
    W2 -= alpha * dE_dW2
    W1 -= alpha * dE_dW1
    
    print(f"  Updated W1: {W1}")
    print(f"  Updated W2: {W2}\n")
