'''
Coding Exercise 5
Section 5, Lecture 47
Here's a rather challenging exercise that integrates functions, loops,
conditionals, and file handling.

In exercise 4, you recursively printed out converted temperature in the
command line. For this exercise, please consider the same list of Celsius
values again as input:

temperatures=[10,-20,-289,100]

Try to make a script that converts Celsius to Fahrenheit and creates a
text file and stores the converted values inside the text file. Your text
file content should look like this:

50.0
-4.0
212.0

Please don't write any message in the text file when input is lower than
 -273.15.
'''

def c_to_f(cel):
    if cel >= -273.15:
        f = cel * 1.8 + 32
    else:
        f = ""
    return f

temperatures=[10,-20,-289,100]

def write_to_file():
    file = open("temp_conv.txt", "a+")
    file.seek(0)
    for t in temperatures:
        out = c_to_f(t)
        if len(str(out)) > 0:
            file.write(str(out) + "\n")
    file.close()

write_to_file()
