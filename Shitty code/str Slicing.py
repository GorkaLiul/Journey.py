#string slicing: you can index[] or slice()
# [start : end : step]
#you can use [x:] without an y to take all starting from x
# to reverse a string [x:y:-1] or [::-1]

name = 'Gorka Liul'
first_name = name[0:5]
last_name = name[6:10]
funcky_name = name[0:10:2]
reverse_name = name[::-1]

print(first_name)
print(last_name)
print(funcky_name)
print(reverse_name)

#slicing part:

url2 = 'https//wix.com'
url = 'https//google.com'
slice = slice(7,-4)
print(url[slice])
print(url2[slice])


