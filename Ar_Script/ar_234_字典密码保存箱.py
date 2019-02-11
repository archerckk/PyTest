import sys,pyperclip

passwords={
    'qq':'123456789',
    'weibo':'sfsfsdfsdfsdfhf',
    '163':'324324dfgdgddcxv',
}
if len(sys.argv)<2:
    print('usage: py pw.py[account]- copy account password')

account=sys.argv[1]


if account in passwords.keys():
    pyperclip.copy(passwords[account])
    print('password has copied to the clipboard')
else:
    print('There is no %s info in passwords'%account)
