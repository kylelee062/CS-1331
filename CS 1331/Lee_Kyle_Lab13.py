import numpy as np

array = np.zeros((4, 6))

print("Shape of the array:", array.shape)
print("Size of the array:", array.size)

array[2] = 7
print("\nArray after step-3:\n", array)

array = np.insert(array, 0, 2, axis=1)
print("\nArray after step-4:\n", array)

array.sort(axis=1)
print("\nArray after step-5:\n", array)

array = np.resize(array, (7, 5))
print("\nArray after step-6:\n", array)

flattened_array = array.flatten(order='F')
print("\nArray after step-7:", flattened_array)

ones_array = np.ones(35)
result = flattened_array + ones_array
print("\nAfter step-8:", result)
