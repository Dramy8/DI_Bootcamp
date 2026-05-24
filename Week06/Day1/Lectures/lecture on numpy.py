#lecture on numpy


# import sys
# !{sys.executable} -m pip install numpy

# %%
import numpy as np
print(np.__version__)

# %%
import numpy as np
# 1. Create arrays
array_1d = np.arange(1, 6)
array_2d = np.arange(1, 7).reshape(2, 3)

print("1D array:")
print(array_1d)
print("Shape:", array_1d.shape)
print("Size:", array_1d.size)
print("Data type:", array_1d.dtype)

print("\n2D array:")
print(array_2d)
print("Shape:", array_2d.shape)
print("Size:", array_2d.size)
print("Data type:", array_2d.dtype)

# 3. Play with data types
float_array = np.arange(1, 4, dtype=float)

print("\nFloat array:")
print(float_array)
print("Data type:", float_array.dtype)

# %%
# --- Additional Arrays ---

# 1D array with temperatures from this week (Sun-Sat)
temperatures = np.array([28, 30, 32, 31, 29, 27, 26])
print("\n--- Weekly Temperatures ---")
print("Temperatures:", temperatures)

# 2D array of shape (2, 5) with values from 1 to 10
array_2x5 = np.array([[3, 7, 1, 9, 5],
                       [2, 8, 4, 10, 6]])
print("\n--- 2D Array (2x5) ---")
print(array_2x5)

# 3D array with valid pixel values (RGB) for a 3x3 image (9 pixels)
# Shape: (3, 3, 3) -> 3 rows, 3 columns, 3 color channels (R, G, B), values 0-255
pixels = np.array([[[255, 0, 0], [0, 255, 0], [0, 0, 255]],
                   [[128, 128, 0], [0, 128, 128], [128, 0, 128]],
                   [[255, 255, 255], [0, 0, 0], [64, 224, 208]]], dtype=np.uint8)
print("\n--- 3D Pixel Array (3x3 image) ---")
print(pixels)
print("Shape:", pixels.shape)
# %%
import numpy as np


# 1. Basic Indexing
array = np.arange(1, 11)

print("Array:")
print(array)

fifth_element = array[4]

print("\n5th element:")
print(fifth_element)


# 2. Basic Slicing
slice_array = array[2:8]

print("\nSlice from 3rd to 8th elements:")
print(slice_array)


# 3. Boolean Indexing
random_array = np.random.randint(10, 51, size=6)

print("\nRandom array:")
print(random_array)

greater_than_30 = random_array[random_array > 30]

print("\nElements greater than 30:")
print(greater_than_30)


# 4. Fancy Indexing
selected_elements = random_array[[1, 3, 5]]

print("\n2nd, 4th, and 6th elements:")
print(selected_elements)

# %%
