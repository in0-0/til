from onnx import TensorProto
from onnx.checker import check_model
from onnx.helper import make_graph, make_model, make_node, make_tensor_value_info

# inputs
# X: name, TensorProto.FLOAT: type, [None, None]: shape
# None은 모든 크기를 말함
X = make_tensor_value_info("X", TensorProto.FLOAT, [None, None])
A = make_tensor_value_info("A", TensorProto.FLOAT, [None, None])
B = make_tensor_value_info("B", TensorProto.FLOAT, [None, None])

# output
Y = make_tensor_value_info("Y", TensorProto.FLOAT, [None])

# node
node1 = make_node("MatMul", ["X", "A"], ["XA"])
node2 = make_node("Add", ["XA", "B"], ["Y"])

graph = make_graph([node1, node2], "lr", [X, A, B], [Y])

onnx_model = make_model(graph)
check_model(onnx_model)

# Serialization
# The serialization
with open("linear_regression.onnx", "wb") as f:
    f.write(onnx_model.SerializeToString())


print(onnx_model)
