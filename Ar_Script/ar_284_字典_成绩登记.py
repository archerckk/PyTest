dictLiming={'姓名':"李明",'年龄':'25','语文':80,'数学':75,'英语':85}
dictZhangqiang={'姓名':"张强",'年龄':'23','语文':75,'数学':82,'英语':78}

dictLiming['python']=60
dictZhangqiang['python']=80

dictZhangqiang['数学']=89

del dictLiming['年龄']

scoreList=[dictZhangqiang['语文'],dictZhangqiang['数学'],dictZhangqiang['英语'],dictZhangqiang['python']]

print(sorted(scoreList))

print(dictLiming.get('城市','beijing'))