l = [[1, 5],[-5, 3], [3, -1], [3, -1]]
l.sort()
print(l)
# result [[-5, 3], [1, 5], [3, -1], [3, -1]]
a = sorted(l, key=lambda x: x[1])
print(a)

# 结论 sorted 会返回一个新数组
# sorted key= 可以使用一个lambda function， function 里面对每一个元素做选择


a = [10, 9, 8, 7]
b = sorted(a[1:])

pass
