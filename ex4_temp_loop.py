'''
Coding Exercise 4
Section 4, Lecture 39
Consider the following list:

temperatures=[10,-20,-289,100]

Then, iterate over the temperature converter function that you created in execise 3
and print out the following output.

50.0
-4.0
That temperature doesn't make sense!
212.0
'''

def cel_to_fah(celsius):
    if celsius >= -273.15:
        f = celsius*1.8 + 32
    else:
        f = "That temperature doesn't make sense!"
    return f

temperatures=[10,-20,-289,100]

for t in temperatures:
    print(cel_to_fah(t))
