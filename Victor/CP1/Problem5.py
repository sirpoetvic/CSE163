# area_codes

# https://cse163.github.io/book/module-2-data-structures-and-files/lesson-5-data-structures-tuple-set-dict/practice-area-codes.html

"""Returns a list containing the unique area
codes of a list of phone numbers"""


def area_codes(phone_list):
    return set([phone[:3] for phone in phone_list])


print(area_codes(["123-456-7890", "206-123-45676", "123-000-0000", "425-999-9999"]))
