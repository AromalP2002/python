#filter()
# l=[1,2,3,4,5,6,7,8]
# print(list(filter(lambda x:x%2)))


# l=['hello','welcome','apple','kiwi']
# print(list(filter(lambda x:('a'),l)))


# map()
l=[1,2,3,4,5,6,7]
# print(list(map(lambda x:x+10,l)))

def num(x):
    return x*3
print(list(map(num,l)))