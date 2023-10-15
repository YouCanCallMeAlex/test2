d = {'name1' : 'id1' ,'name2' : 'id2' , 'name3' : 'id3'}
a = {}
a = dict(zip(d.values(), d.keys()))
print(a)