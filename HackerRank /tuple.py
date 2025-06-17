# Using python2
if __name__ == '__main__':
    n = int(raw_input())  # Read the number of integers (we won't use 'n' explicitly)
    integer_list = map(int, raw_input().split())  # Convert the input into a list of integers
    
    # Create a tuple from the list and calculate its hash
    print hash(tuple(integer_list))  # In Python 2, 'print' is a statement, not a function
