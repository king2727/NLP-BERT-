import numpy as np

# 建立二进制映射
int2binary = {}
binary_dim = 8
largest_number = pow(2, binary_dim)
binary = np.unpackbits(
    np.array([range(largest_number)], dtype=np.uint8).T,
    axis=1
)

for i in range(largest_number):
    int2binary[i] = binary[i]

# 定义参数
alpha = 0.9
input_dim = 2
hidden_dim = 16
output_dim = 1

synapse_0 = (2 * np.random.random((input_dim, hidden_dim)) - 1) * 0.05
synapse_1 = (2 * np.random.random((hidden_dim, output_dim)) - 1) * 0.05
synapse_h = (2 * np.random.random((hidden_dim, hidden_dim)) - 1) * 0.05

synapse_0_update = np.zeros_like(synapse_0)
synapse_1_update = np.zeros_like(synapse_1)
synapse_h_update = np.zeros_like(synapse_h)

# 模型初始化
c = 1
d = np.zeroError = 0

layer_2_deltas = list()
layer_1_values = list()

layer_1_values.append(np.ones(hidden_dim)*0.1)

# 正向传播
for position in range(binary_dim):
    x = np.array([[a[binary_dim - position - 1], b[binary_dim - position - 1]]])
    y = np.array([[c[binary_dim - position - 1]]]).T

    layer_1 = sigmoid(np.dot(X, synapse_0) + np.dot(layer_1_values[-1], synapse_h))

    layer_2 = sigmoid(np.dot(layer_1, synapse_1))

    layer_2_error = y - layer_2
    layer_2_deltas.append((layer_2_error)*sigmoid_output_to_derivative(layer_2))

    overallError += np.abs(layer_2_error[0])

    d[binary_dim - position - 1] = np.round(layer_2[0][0])

    layer_1_values.append(copy.deepcopy(layer_1))
