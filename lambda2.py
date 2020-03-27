List = {1,2,3,4,5,6}
Oddlist = list(filter(lambda a : (a%3 ==0),List) )
print(Oddlist)

List = {1,2,3,4,10,123,22}
new_list = list(map(lambda x:x*3,List)) # this will return the triple of each item of the list and add it to new_list
print(new_list)  