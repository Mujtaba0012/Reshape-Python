import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

reshaped = arr.reshape(3,4)
print("Reshaped array:\n", reshaped)

second_row = reshaped[1,:]
print("\nSecond Row :", second_row)

third_column = reshaped[:,2]
print("\nthird Row :", third_column)

greater_than_5 = reshaped[reshaped > 5]

print("\nGreater than 5 :", greater_than_5)