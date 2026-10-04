# Loop 1. Area Codes
phone = ['555-1234', '555-8945', '555-9632', '555-2587', '802-555-7532', '555-9512', '802-555-9173', '555-4562']

def add_area_code(phone_numbers, area_code):
    """Returns a list of phone numbers with the area code added.
    Given a list of phone numbers that are missing the area code,
    append the area code to the phone numbers in the list and return the result list.

    :param phone_numbers: (list) A list of phone numbers (strings) that do not have the area code
                                Example: ['555-1212']
    :param area_code: (str) The area code to add Example: '802'
    :return: (list) A list of phone numbers with the area code Example: ['802-555-1212']
    """
    full_phone_numbers = []
    for n in phone_numbers:
        full_phone_numbers.append(area_code + '-' + n)
    return full_phone_numbers

# example usage
phone_numbers = ['555-1212', '999-0738']
with_area_code = add_area_code(phone_numbers, '802')
print(with_area_code)
