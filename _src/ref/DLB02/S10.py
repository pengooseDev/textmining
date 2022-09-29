import re

print(re.findall("[abc]", "How are you, boy?"))
print(re.findall("[0123456789]", "3a7b5c9d"))
print(re.findall("[\w]", "3a 7b_ '.^&5c9d")) #*****모든 string, number
print(re.findall("[_]+", "a_b, c__d, e___f"))
print(re.findall("[\w]+", "How are you, boy?"))
print(re.findall("[o]{2,4}", "oh, hoow are yoooou, boooooooy?"))
