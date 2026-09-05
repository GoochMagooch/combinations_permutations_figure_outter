import sys
# Find all numbers divisible by 11, with all combinations of 6 digits

# PROMPT USER FOR 6 DIGITS AND STORE IN LIST
user_digits = []
user_digits.append(int(input("Enter first digit (0 - 9): ")))
user_digits.append(int(input("Enter second digit (0 - 9): ")))
user_digits.append(int(input("Enter third digit (0 - 9): ")))
user_digits.append(int(input("Enter fourth digit (0 - 9): ")))
user_digits.append(int(input("Enter fifth digit (0 - 9): ")))
user_digits.append(int(input("Enter sixth digit (0 - 9): ")))

# CHECK FOR DIGITS > 9 OR < 0
for i in range(len(user_digits)):
    if user_digits[i] > 9 or user_digits[i] < 0:
        print("One of your digits is greater than 9 or less than 0!")
        sys.exit()

# NOTE: MAIN COMBO/PERMU FUNCTION
# FOR LOOP OR WHILE LOOP
# LOCK FIRST DIGIT IN PLACE
    # CHECK ALL PERMUTATIONS WITH FIRST 4 DIGITS LOCKED, THEN FIRST 3 AND SO ON...
# LOCK SECOND DIGIT IN PLACE
    # ...
# IF DIGIT IS 0 DO NOT PLACE AT START OF COMBINATION

# I can start by ordering all numbers from least to greates, leaving any 0s to trail
# Going to study DSA to see if it helps at some point
