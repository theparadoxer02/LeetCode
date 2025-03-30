

dictionary = {}

for i in range(5):
    dictionary[i] = i * 2

print(dictionary)

operations = True

# while operations:
#     for key in abc.keys():
#         abc.pop(key)
#         print(key)

#     operations = False


sample_set = set([1, 34, 4, 5, 5])
while operations:
    for key in sample_set:
        sample_set.remove(key)
        print(key)

    operations = False
