class TmpChange:
    def __new__(cls,c):
        cls.hua=c*1.8+32
        return cls.hua


print(TmpChange(32))
# print(TmpChange(32))