import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

#试卷头部信息写入
for i in range(5):
    paper_file=open('paper_%s.txt'%(i+1),'w')
    answer_file=open('paper_answer_%s.txt'%(i+1),'w')
    paper_file.write('Name:\n\n')
    paper_file.write('Date:\n\n')
    paper_file.write('Period:\n\n')
    paper_file.write('\t\t\t\tState Capitals Quiz (Form %d)\n\n'%(i+1))

    #获取所有的州，并且打乱
    states=list(capitals.keys())
    # print(len(states))
    random.shuffle(states)
    for q_num in range(50):
        answer=capitals[states[q_num]]
        wrong_answer=list(capitals.values())
        del wrong_answer[wrong_answer.index(answer)]
        wrong_answers=random.sample(wrong_answer,3)

        answer_options=[answer]+wrong_answers
        random.shuffle(answer_options)
        paper_file.write("%s. What is the capital of %s?\n"%(q_num+1,states[q_num]))
        for i in range(4):
            paper_file.write('\t%s. %s'%('ABCD'[i],answer_options[i]))
            paper_file.write('\n')
        paper_file.write('\n')

        answer_file.write('%s. %s\n'%(q_num+1,'ABCD'[answer_options.index(answer)]))

    paper_file.close()
    answer_file.close()