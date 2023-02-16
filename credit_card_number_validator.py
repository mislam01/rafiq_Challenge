'''
Python version: 3.7
Purpose: Providing function to check valid credit numbers for Visa, MasterCard and Discover.
Author: Rafiq Islam, NJ, USA.
Development Date: 11-Feb-2023
'''

import sys
import re

PATTERN='^([456][0-9]{3})-?([0-9]{4})-?([0-9]{4})-?([0-9]{4})$'

# Functions
def check_card_validity(card_number):
    '''
    Determines if the card_number is a valid credit card number based on the following.

    A valid credit card number
    1. must contain exactly 16 digits,
    2. must start with a 4, 5 or 6 
    3. must only consist of digits (0-9) or hyphens '-',
    4. may have digits in groups of 4, separated by one hyphen "-". 
    5. must NOT use any other separator like ' ' , '_',
    6. must NOT have 4 or more consecutive repeated digits.
    '''

    matched = re.match(PATTERN,card_number)  # `matched` fulfills conditions 1-5

    if matched is None:
        return 'Invalid'

    # To fulfill condition #6
    all_digits = re.sub('\D', '', card_number)
    for i in range(13):
        four_consecutive_digits = all_digits[i:i+4]
        # print(f'{i}-{i+3}: {four_consecutive_digits}')
        if all_digits[i]*4 == four_consecutive_digits:
            return 'Invalid'

    # The card number is valid if not retured from above
    return 'Valid'
# End Functions

number_of_cards = input('How many credit card numbers to check (1-99)? ')
if not(number_of_cards) or int(number_of_cards) < 1 or int(number_of_cards) > 99:
    sys.exit('Number of cards to be between 1 and 99')


for m in range(int(number_of_cards)):
    n = m+1
    prompt = f'Enter card number {n} of {number_of_cards}: '
    card_num = input(prompt)
    print(check_card_validity(card_num))
####End of Script #####
