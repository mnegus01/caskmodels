'''
Created on Dec 2, 2016
@author: Mitch

Utilities to be used in transforming a file object into a modifiable form and back
'''

def splitfile(infile,delimiter=None):
    # Split a file object into an array
    listfile = [line.strip('\n').split(delimiter) for line in infile]
    return listfile

def joinfile(listfile,delimiter=''):
    # Join a 2D array into a single string for output as multiline text
    stringfile = '\n'.join([delimiter.join(line) for line in listfile])
    return stringfile