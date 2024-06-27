immutable_var_ = 1,2,3,4,5,'a','b','c','d'
print('Immutable tuple:',immutable_var_)
mutable_list = [1,2,3,4,5,'a','b','c','d']
mutable_list.append('Modified')
print('Mutable list:',mutable_list)
immutable_var_[5] = 6 #кортеж не поддерживает обращение по элементам, это неизменный список
print('New immutable tuple:',immutable_var_)