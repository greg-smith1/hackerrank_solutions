"""In this challenge, the task is to debug the existing code to successfully execute all provided test files.
Debug the given function print_from_stream
"""

raw_input = input     # Locked code apparently copied from python 2 

def print_from_stream(n, stream=None):
    if stream == None:
        stream = EvenStream()
    for _ in range(n):
        print(stream.get_next())
