#%%
# pip3 install numpy
# import numpy as np
# print(np.__version__)

import numpy as np

movie_ratings = np.array([
    [5, 4, 4, 1, 3],
    [1, 4, 3, 1, 2],
    [4, 2, 5, 5, 1]
])

average_ratings = np.mean(movie_ratings, axis=1)
viewer_preferences = np.argmax(movie_ratings, axis=0) + 1

print("Average ratings:", average_ratings)
print("Viewer preferences:", viewer_preferences)
# %%
