#Write a NumPy program to convert a list of numeric value into a one-dimensional NumPy array.
import numpy as np
list=[1,2,3,4,5]
arr=np.array(list)
print(arr)

#Write a NumPy program to create a 3X3 matrix with values from 2 to 10
arr=[[1,2,3],[4,5,6],[7,8,9]]
matrix=np.array(arr)
print(matrix)

#Write a NumPy program to create a null vector of size 10 and update the sixth value to 11.
import numpy as np

my_vector=np.zeros(10)
my_vector[5]=11
print(my_vector)

#Write a NumPy program to create an array with values ranging from 12 to 38.
import numpy as np

arr=np.arange(12,39)
print(arr)

#Write a NumPy program to reverse an array (first element becomes last).
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print("Original array:", arr)

rev_arr = arr[::-1]
print("Reversed array:", rev_arr)

#Write a NumPy program to convert an array to a float type.
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print("Original array:", arr)
float_arr = arr.astype(float)
print("Float Array:", float_arr)

#Write a NumPy program to create an 8X8 matrix and fill it with a checkerboard pattern.
import numpy as np

matrix = np.zeros((8, 8))
matrix[1::2, ::2] = 1
matrix[::2, 1::2] = 1
print(matrix)

#Write a NumPy program to convert a list and tuple into arrays.
import numpy as np
list1 = [1, 2, 3, 4, 5]
arr1 = np.array(list1)
print("List converted to array:", arr1)
tuple1 = (6, 7, 8, 9, 10)
arr2 = np.array(tuple1)
print("Tuple converted to array:", arr2)

#Write a NumPy program to convert the values of Centigrade degrees into Fahrenheit degrees and vice versa. Values are stored in to a NumPy array
import numpy as np

# Create a NumPy array of Celsius temperatures
celsius_temps = np.array([0, 10, 20, 30, 40, 50])
fahrenheit_temps = (celsius_temps * 9/5) + 32
print("Celsius temperatures:", celsius_temps)
print("Fahrenheit temperatures:", fahrenheit_temps)
fahrenheit_temps=np.array([32, 50, 68, 86, 104])
celsius_temps = (fahrenheit_temps - 32) * 5/9
print("Fahrenheit temperatures:", fahrenheit_temps)
print("Celsius temperatures:", celsius_temps)
