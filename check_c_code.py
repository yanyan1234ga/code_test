import chardet

#test_txtの文字コード表示
with open('test.txt','rb') as f:
    b = f.read()
    print(b)
    c = chardet.detect(b)
    print(c)
    print('')

#code_test.pyの文字コード表示
with open('code_test.py','rb') as fp:
    bp = fp.read()
    print(bp)
    cp = chardet.detect(bp)
    print(cp)
    print('')

#sample.csvの文字コード表示
with open('sample.csv','rb') as fc:
    bc = fc.read()
    print(bc)
    cc = chardet.detect(bc)
    print(cc)
    print('')

#sample2.csvの文字コード表示
with open('sample2.csv','rb') as fe:
    be = fe.read()
    print(be)
    ce = chardet.detect(be)
    print(ce)
    print('')