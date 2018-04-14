orgin=(0,0)
legal_x=[-100,100]
legal_y=[-100,100]


def create(pos_x=0,pos_y=0):

    def moving(dir,step):
        nonlocal pos_x,pos_y
        n_pos_x=pos_x+dir[0]*step
        n_pos_y=pos_y+dir[1]*step

        if n_pos_x<legal_x[0]:
            pos_x=legal_x[0]-(n_pos_x-legal_x[0])
        elif n_pos_x>legal_x[1]:
            pos_x= legal_x[1] - (n_pos_x - legal_x[1])
        else:
            pos_x=n_pos_x

        if n_pos_y<legal_y[0]:
            pos_y=legal_y[0]-(n_pos_y-legal_y[0])
        elif n_pos_y>legal_y[1]:
            pos_y= legal_y[1] - (n_pos_y - legal_y[1])
        else:
            pos_y=n_pos_y

        return [pos_x,pos_y]
    return moving

move=create()

print('向上移10步的坐标为：',move(([-1,0]),10))