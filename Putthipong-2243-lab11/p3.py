#Putthipong Phukhansung 633040224-3
"""
Write a program to prompt for the text and the pattern. If the pattern is found in the text, display the message that “Found <pattern> in <text> at <position>”.  If the pattern is not found in the text, display the message that “Cannot find <pattern> in <text>”
"""
import re 

text = input("Enter text: ")
pattern = input("Enter pattern: ")
search = re.search(pattern, text)

if pattern in text:
    position = re.search(pattern, text).start()
    print(f"Found",search.group() , f"in {text} at {position}")
else:
    print(f"Cannot find {pattern} in {text}")
    