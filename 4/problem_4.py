class Problem_4(object):

    def is_pal(self, num):
        list = []
        for i in str(num):
            list.append(i)
        list.reverse()
        string = ''.join(list)
        return num == int(string)

