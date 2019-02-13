class Problem_4(object):

    def is_pal(self, num):
        list = []
        for i in str(num):
            list.append(i)
        list.reverse()
        string = ''.join(list)
        return num == int(string)

    def solver(self, num1, num2):
        pal = []
        n1 = 0
        n2 = 0
        while n1 <= num1:
            answer = n1 * n2
            if self.is_pal(answer) == True:
                if answer not in pal:
                    pal.append(answer)
            while n2 <= num2:
                answer = n1 * n2
                if self.is_pal(answer) == True:
                    if answer not in pal:
                        pal.append(answer)
                n2 += 1
            n1 += 1
            n2 = 1
        print(max(pal))
        return max(pal)

