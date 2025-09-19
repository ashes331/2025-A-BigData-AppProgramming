
data = {
    'bgnde',
    'sj',
    'endde'
}

print(type(data))

#추가
data.add('title')
data.add('title')
print(data)

#삭제
data.remove('sj')
print(data)

if 'sj' in data:
    data.remove('sj')

data.discard('sj')
data.discard('sj')
data.discard('sj')
data.discard('sj')
data.discard('sj')