"""
9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
"""

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
count = {}
for line in handle:
    if line.startswith("From"):
        words = line.split(" ")
        key = words[1]
        count[key] = count.get(key, 0) + 1 # dict.get() return 0 if A value to return if the specified key does not exist

max_key = None
max_value = None 
for key in count:
    if max_value == None or max_value < count[key]:
        max_key = key
        max_value = count[key]
        
print(max_key, max_value)


# Solution 2:
# name = input("Enter file:")
# if len(name) < 1:
#     name = "mbox-short.txt"
# handle = open(name)
# count = {}
# for line in handle:
#     if line.startswith("From"):
#         words = line.split(" ")
#         key = words[1]
#         if key in count:
#             count[key] = count[key] + 1
#         else:
#             count[key] = 1
# max_key = None
# max_value = None 
# for key in count:
#     if max_value == None or max_value < count[key]:
#         max_key = key
#         max_value = count[key]
        
# print(max_key, max_value)

