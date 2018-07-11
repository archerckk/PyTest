import csv

data=csv.reader(open('resources/test_account.csv','r'))

# for i in data:
#     print(i)

for mail in data:
    print(mail[1])