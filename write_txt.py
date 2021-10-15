import codecs

#test.txtをutf-8で書き込み
with codecs.open('test.txt','w', encoding = 'utf-8') as f:
    f.write('Hello\n')
    f.write('Goodbye\n')
