import re
test_str='The ADJECTIVE panda walked to the NOUN and the VERB.'


adj_reg=re.compile(r'ADJECTIVE',re.I)
noun_reg=re.compile(r'NOUN',re.I)
verb_reg=re.compile(r'VERB',re.I)

adj_replace=input('请输入替换ADJECTIVE的内容：\n')
adj_str=adj_reg.search(test_str).group()
test_str=test_str.replace(adj_str,adj_replace)

noun_replace=input('请输入替换NOUN的内容：\n')
noun_str=noun_reg.search(test_str).group()
test_str=test_str.replace(noun_str,noun_replace)

verb_replace=input('请输入替换VERB的内容：\n')
verb_str=verb_reg.search(test_str).group()
test_str=test_str.replace(verb_str,verb_replace)

print(test_str)

with open('test.txt','w')as f:
    f.write(test_str)
