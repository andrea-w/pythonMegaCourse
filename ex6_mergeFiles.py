'''
Coding Exercise 6: Merging Text Files
Section 6, Lecture 53
Here is a tricky exercise.

Please download the ZIP file in the Resources and unzip it in a folder.

Then create a script that merges the three text files into a new text file
containing the text of all three files. The filename of the merged text file
should contain the current timestamp down to the millisecond level.
E.g. "2016-06-01-13-57-39-170965.txt".
'''

import glob2
import os
import datetime

# get list of filenames within Sample-Files dir
filesList = []
for file in glob2.glob('./Sample-Files/*.txt'):
    filesList.append(file)

# copy contents of each file into string
superString = ""
for file in filesList:
    with open(file, 'r') as myfile:
        superString += myfile.read()
        superString += '\n'

# write string to new file titled with current timestamp
now = datetime.datetime.now()
with open(now.strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt", "w") as text_file:
    text_file.write(superString)
