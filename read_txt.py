import codecs

#test.txtをutf-8で読み込み
with codecs.open('test.txt','r', 'utf-8') as f:
    lines = f.readlines()
    for line in lines:
        print(line,end="")
