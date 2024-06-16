def only_odd_digits(n):
    ''' Define even the odds function '''

    # Check if n is a positive integer
    if n < 0 or type(n) is float:
        raise ValueError('Only positive integers are allowed')

    # Convert n to str
    n_str = str(n)

    # Loop through every digit
    for i in range(len(n_str)):
        digit = int(n_str[i]) # Extract i digit
        if digit % 2 == 0: # Check if digit is even
            verif = False # Assign False, even digit was found
            break # An even digit was found, cease evaluation
        else:
            verif = True # Assign True, only odd number

    return verif # Return result
