import re

emails = """zuck26@facebook.com
page33@google.com
jeff42@amazon.com"""
#pattern = r"\b\w+\d"
#result = re.findall(pattern,emails)
#print(result)
pattern = r"\b\w+@facebook.com"
result = re.findall(pattern,emails)
print(re.split(r'\W+', 'zuck26@facebook.com'))
print(re.split(r'\W+', 'page33@google.com'))
print(re.split(r'\W+', 'jeff42@amazon.com'))
