#%%
# Ask the user for their birthdate (specify the format, for example: DD/MM/YYYY).
# Display a little cake as seen below:
#        ___iiiii___
#       |:H:a:p:p:y:|
#     __|___________|__
#    |^^^^^^^^^^^^^^^^^|
#    |:B:i:r:t:h:d:a:y:|
#    |                 |
#    ~~~~~~~~~~~~~~~~~~~

# The number of candles on the cake should be the last number of the users age,
#  if they are 53, then add 3 candles.

# Bonus : If they were born on a leap year, display two cakes !


birth = input("Enter your birthdate (DD/MM/YYYY): ")
year = birth.split('/')[-1]
yeardate = int(year)

import datetime
today = datetime.date.today()
current_year = today.year

age = current_year - yeardate

num = str(age)
candles = int(num[-1])

print('         '+"i"*candles+'    ')
print("       -----------")
print("      |:H:a:p:p:y:|")
print("    __|___________|__")
print("   |^^^^^^^^^^^^^^^^^|")
print("   |:B:i:r:t:h:d:a:y:|")
print("   |                 |")
print("   ~~~~~~~~~~~~~~~~~~~")


# %%
