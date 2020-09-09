def replace_text(file,old_word,new_word):
    file_data = ''
    with open(file)as f:
        for i in f:
            if old_word in i:
                i=i.replace(old_word,new_word)
            file_data+=i

    with open(file,'w',encoding='utf-8')as f:
        f.write(file_data)

replace_text('test_replace.txt','test2','archer')