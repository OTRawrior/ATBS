#! python3
# Reads a user-specified file, allows the user to overwrite any string
# NOUN, ADVERB, VERB or ADJECTIVE. Saves output as a user-specified file.
# Usage: py madlib.py <input file> <output file>

import sys
import os

inputFileContent = ''
outputFileContent = ''


def read_input_file(inputFileName):
    # Open up inputFile and write it to content, then close inputFile.
    inputFile = open(inputFileName, 'r')
    inputFileContent = inputFile.read()
    inputFile.close()
    return inputFileContent


def write_output_file(input):
    # Lets user overwrite the strings and writes to the output file.
    return outputFileContent


def check_arguement_validity():
    # Checks if given arguements are OK, otherwise exits.
    if len(sys.argv) != 3:
        # Checks if arguments are correct and prematurely exits if not.
        print("Please specify an input and output file name.")
        exit()

    if os.path.isfile(sys.argv[1]) is False:
        # Checks if arg. 1 exists and prematurely exits if not.
        print("Invalid file name.")
        exit()


# Main Block:
if __name__ == '__main__':
    check_arguement_validity()
    inputFileContent = read_input_file(sys.argv[1])
    outputFileContent = write_output_file(inputFileContent)
    print(outputFileContent)