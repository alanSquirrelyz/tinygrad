from tinygrad.tensor import Tensor
a = Tensor([[1,2], [2,2], [1,2], [1,2], [1,2], [1,2], [1,2], [1,2], [1,2], [1,2], [1,2], [1,2], [1,2]])
b = Tensor([3,4])
res = a.dot(b).numpy()
# print(res) # 11

print(a.associative_scan("add").numpy()) 