import json
#print(json.__all__)
dict={'name':'leizi','age':'24','address':'北京'}
print(dict)
str1=json.dumps(dict)
print(str1)
str2=json.loads(str1)
print(str2)