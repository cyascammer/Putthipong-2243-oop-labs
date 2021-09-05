'''
Putthipong Phukhansung
633040224-3
Problem 3
'''


def main() -> None:
    fread = input("Enter a filename:")
    with open(fread, 'r') as f:
        read_data = f.read()
    print(read_data)

if __name__ == '__main__':
    main()
    
#


import json
filename = "hobbies.json"
with open(filename, 'w') as file_obj:
    data = { "firstName": "Jane", "lastName": "Doe",
          "hobbies": ["running", "sky diving", "singing"]}
    json.dump(data,file_obj)
