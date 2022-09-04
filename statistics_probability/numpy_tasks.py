"""
scalars - numbers, e.g. volume, density, speed, energy, mass, and time.
vectors - a list of mathematical variables each of whose value is unknown, either because the value has not yet occurred or because there is imperfect knowledge of its value.
matrices - a rectangular array of numbers arranged into columns and rows (much like a spreadsheet)
tensors - multidimensional arrays

n-dimensional - no limits
"""
import numpy as np

#Task 1 (execrises) - Create np.ndarray containing numbers from 0 to 100.
# nr = np.arange(100)
# print(nr)
#
# #Create np.ndarray containing numbers from 0 to 1000
# # that are divisible by 11. Output numbers should be in descending order
# #1st option (mine):
# numbers = np.arange(11, 1000, 11)
# nrs = np.sort(numbers) [::-1]
# print(nrs)
#
# #2nd option (SDA):
# numbers = np.array([x for x in range(1000, 1, -1) if x % 11 == 0])
# print(numbers)
#
# #Create np.ndarray containing 70 evenly spaced numbers
# # in the range of -5 - 5
# evenly_spaced = np.linspace(-5, 5, 70)
# print(evenly_spaced)

#Task 2 (execrises) - Create matrices as below, then make some calculations with them.
# matrix1 = np.array([[1, 4, 7], [2, 5, 8], [3, 6, 9]])
# matrix2 = np.array([[3, 2, 3], [4, 3, 1], [7, 3, 1]])
# print(matrix1, '\n', '\n', matrix2)     # printing array
# print('\n', matrix1.shape, '\n', matrix2.shape) # printing shape
#
# matrix_sum = np.add(matrix1, matrix2)   # calculating sum
# print(matrix_sum)
# diff = np.diff(matrix1, axis=1)    # calculating difference, also axis=0 works
# print(diff)
# subtract_matrix = np.subtract(matrix1, matrix2)     # calculating difference
# print(subtract_matrix)
# transposition_matrix1 = matrix1.T       # transposing matrix1, also "np.transpose" works
# transposition_matrix2 = matrix2.T
# print(transposition_matrix1, '\n', transposition_matrix2)
# print(matrix1 * matrix2)    # multiplies
# mult = np.multiply(matrix1, matrix2)    # also multiplies
# print(mult)
# print(matrix1 ** matrix2)           # astendatud
# quotient_matrix = np.divide(matrix1, matrix2)   # calculation quotient
# print(quotient_matrix)
# matrix_product = np.matmul(matrix1, matrix2)    # calculation matrix product(multiplication)
# print(matrix_product)

#Task1 (slides):
# Create a numpy array with values from 1 to 9, display and
#then invert this array (first element becomes last, etc.)

# a = np.arange(1, 10)
# print(a)
# inverted = np.sort(a)[::-1]
# print(inverted)

#Task 2 (slides):
#Create the following numpy array: [1, 23, 4, 31, 1, 1, 4, 23, 4, 1]; and
#then list all the unique (non-repeating) elements.

# b = np.array([[1, 23, 4, 31, 1, 1, 4, 23, 4, 1]])
# print(b)
# unique_b = np.unique(b)
# print(unique_b)

#Task 3 (slides):
#Create a 3x3 matrix (using reshape) with values between 2 and 10.
# c = np.arange(2, 11).reshape((3, 3))
# print(c)

#Task 4 (slides):
#Create an array with six random values between 10 and 30.
# d = np.random.randint(10, 31, 6)
# print(d)

#Task 5 (slides):
#From the array of values: [23, 45, 112, 150, 43, 254, 95, 8] filter those
#that are greater than 100

# e = np.array([[23, 45, 112, 150, 43, 254, 95, 8]])
# print(e)
# greater_100 = np.where(e > 100)
# print(greater_100)
# print(e[greater_100])

#Task6 (slides):
#Create the 4x4 matrix below, then:
# 1. display item from second row and third column,
# 2. calculate its determinant,
# 3. calculate its trace (sum of elements on the main diagonal),
# 4. find the largest and smallest item

# f = np.array([[1, 15, 4, 13, 8, 21, 3, 12, 11, 13, 11, 5, 32, 13, 0, 2]]).reshape(4, 4)
# print(f)
#
# print(f[1, 2])   # display item from second row and third column (answer: 3)
#
# determinant_e = np.linalg.det(f)  # calculate determinant (-19963.99999999999)
# print(determinant_e)
#
# trace_f = np.diagonal(f).sum()  # calculate its trace (35) (sum of elements on the main diagonal)
# print(trace_f)
#
# largest_f = np.max(f)   # find the largest (32) and smallest item (0)
# print(largest_f)
# smallest_f = np.min(f)
# print(smallest_f)

#Task 7 (slides):
#Create any array of values and then calculate the mean and median.

# g = np.array([[1, 5, 8, 14, 3, 2, 0, 7, 6, 3, 8, 9, 22, 40, 3, 1, 7, 9, 6]])
# mean_g = np.mean(g)
# median_g = np.median(g)
# print(mean_g, '\n', median_g)

#Task 8 (slides):
#Create any array of values and then normalize them - i.e. from
#each element of the array subtract the mean and divide by the
#standard deviation.

# h = np.array([[1, 5, 8, 14, 3, 2, 0, 7, 6, 3, 8, 9, 22, 40, 3, 1, 7, 9, 6]])
# mean_h = np.mean(h)
# standard_deviation_h = np.std(h)
# print(mean_h)
# print(standard_deviation_h)
# normalized_h = (np.subtract(h, mean_h)) / standard_deviation_h
# print(normalized_h)

#Task 9 (slides):
#Create a function that takes two vectors (both with the same
#dimension) as a numpy array and returns the Euclidean distance
#between them.

#a = np.array((1, 2, 3))       #as just values
#b = np.array((1, 1, 1))
# distance = np.linalg.norm(a - b)
# print(distance)

# def distance(a, b):         #as a function
#     dist = np.linalg.norm(a - b)
#     return dist
# a = np.array((1, 2, 3))
# b = np.array((1, 1, 1))
# print(distance(a, b))



