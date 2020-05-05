def myRev(data):
    # 这里用 range 生成 data 的倒序索引
    # 注意，range 的结束位置是不包含的
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for i in myRev('FishC'):
    print(i,end='')


print()
def feibo(count):
    '输出指定位置的斐波那契数列字符'
    index=0
    a=0
    b=1
    while index<=count:
        if index==count:
            yield b
        c = b
        b=a+b
        a=c
        index+=1


for i in feibo(10):
    print(i)


#模拟多任务操作
def play_music(duration):
    time=0
    while time<duration:
        print('听音乐{}分钟'.format(time))
        time+=1
        yield None
    raise StopIteration

def coding(duration):
    time=0
    while time<duration:
        print('写代码{}分钟'.format(time))
        time+=1
        yield None
    raise StopIteration

def main():
    music_generator=play_music(10)
    coding_generator=coding(20)
    music_end=False
    coding_end=False

    while True:
        try:
            next(music_generator)
        except StopIteration:
            print('音乐已经听完了')
            music_end=True

        try:
            next(coding_generator)
        except StopIteration:
            print('代码已经写完了')
            coding_end=True

        if music_end and coding_end:
            break

if __name__ == '__main__':
    main()