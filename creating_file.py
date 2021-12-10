s = '''
created ?
or
not ?
'''

print('file creating')
with open('test_file.spec', 'w') as fd:
    fd.write(s)
