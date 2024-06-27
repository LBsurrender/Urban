print('1)Работа со словарями:')
my_dict = {'Ruslan':1986,'Madina':1987,'Damir':2013,'Danik':2016}
print('Dict:',my_dict)
print('Existing value:',my_dict['Ruslan'])
print('Not existing value:',my_dict.get('Saadu'))
my_dict.update({'Muslim':1987,'Saadu':1986})
print('Deleted value:',my_dict['Saadu'])
del my_dict['Saadu']
print('Modified dictionary:',my_dict)

print('2)Работа с множествами:')
my_set = {1,2,3,1,2,2,5,'Руслан','Руслан','Мадина',3.14,3.14}
print('Set:',my_set)
my_set.add(345)
my_set.add((1,2,3))
my_set.discard(2)
print('Modified set',my_set)