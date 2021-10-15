import codecs

#sample.csvをshift_JISに変換
with codecs.open('sample.csv',encoding='utf-8') as f_in:
    with open('sample2.csv', 'w', encoding='cp932') as f_out:
        f_out.write(f_in.read())



