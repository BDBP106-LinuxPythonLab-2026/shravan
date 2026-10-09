#!/usr/bin/python3
#25 sep, 2026
#question4
"""Given a dictionary with a values list, extract the key whose value has the most unique values.
Input: test_dict= {"Gfg":[5,7,7,7,7], "is":[6,7,7,7], "Best":[9,9,6,5,5]}
Output:"Best"
Explanation:3 (max) unique elements, 9,6,5 of "Best" """

test_dict= {"Gfg":[5,7,7,7,7], "is":[6,7,7,7], "Best":[9,9,6,5,5]}
#test_dict = {"Gfg":, "is":, "Best":}

max_unique_count = -1
result_key = None
for key, value_list in test_dict.items():
    unique_values = set(value_list)
    unique_count = len(unique_values)

    if unique_count > max_unique_count:
        max_unique_count = unique_count
        result_key = key

print(test_dict.get(result_key),result_key)
