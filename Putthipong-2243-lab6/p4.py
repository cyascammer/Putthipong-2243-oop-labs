'''
Putthipong Phukhansung
633040224-3
Problem 4
'''


import json

with open('hobbies.json', 'r') as read_file:
    data = json.load(read_file)
    print(''.join(data['firstName']), 'has hobbies as', ', '.join(data['hobbies']))
