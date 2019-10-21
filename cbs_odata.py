import cbsodata

tablename = '03759ned'

info = cbsodata.get_info(tablename)

print(info.keys())
print(info['Title'])

for k,v in info.items():
    print('%-20s : %s' % (k,v))