# coding=utf-8
class page:
    def __init__(self, num, time):
        self.num = num
        self.time = time


class main:
    def __init__(self, a, size):
        self.lv = 0
        self.ci = 0
        self.M = size
        self.N = len(a)
        self.arr_int = a
        self.res = ""
        self.b = [page(-1, self.M - i - 1) for i in range(0, self.M)]
        self.c = [[-1 for i in range(0, self.N)] for j in range(0, self.M)]
        self.queue = []
        self.k = -1
        self.flag = -1
        self.process()

    def print_string(self):
        print("|---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|")

    def print_string2(self):
        print("|---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|")

    def get_max(self, b):
        max = -1
        flag = 0
        for i in range(0, self.M):
            if b[i].time > max:
                max = b[i].time
                flag = i
        return flag

    def equation(self, fold, b):
        for i in range(0, self.M):
            if fold == b[i].num:
                return i
        return -1

    def fifo(self, fold, b):
        val = self.equation(fold, b)
        if val >= 0:
            pass
        else:
            self.queue.append(fold)
            self.k += 1
            self.flag += 1
            self.flag %= self.M
            self.b[self.flag].num = fold

    def Myprint(self, a):
        self.res = self.res + "|---"
        for j in range(0, self.N - 2):
            self.res = self.res + "+---"
        self.res = self.res + "+---|\n"
        for j in range(0, self.N):
            self.res = self.res + "|%2d" % (a[j]) + " "
        self.res = self.res + '|\n'
        self.res = self.res + "|---"
        for j in range(0, self.N - 2):
            self.res = self.res + "+---"
        self.res = self.res + "+---|\n"
        for i in range(0, self.M):
            for j in range(0, self.N):
                if self.c[i][j] == -1:
                    self.res = self.res + "|%2c" % (32) + " "
                else:
                    self.res = self.res + "|%2d" % (self.c[i][j]) + " "
            self.res = self.res + "|\n"
        self.res = self.res + "|---"
        for j in range(0, self.N - 2):
            self.res = self.res + "+---"
        self.res = self.res + "+---|\n调入队列为"
        for i in range(0, self.k + 1):
            self.res = self.res + "%3d" % (self.queue[i])
        self.ci = self.k + 1
        self.lv = (float)((self.k + 1) / self.N)

    def process(self):
        a = self.arr_int
        for i in range(0, self.N):
            self.fifo(a[i], self.b)
            self.c[0][i] = a[i]
            for j in range(0, self.M):
                self.c[j][i] = self.b[j].num
        self.Myprint(a)

    def get_res(self):
        return self.res

    def get_lv(self):
        return self.lv

    def get_ci(self):
        return self.ci


if __name__ == "__main__":
    main([1, 2, 3, 2, 1, 2, 3, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 2, 1, 3, 2, 1, 4, 2, 3, 1, 2, 1, 2, 3, 2, 1, 4, 1, 2, 3, 2,
          1, 1, 2, 4, 1, 2, 3, 4, 1, 2, 5, 3, 1, 4, 7, 2, 5, 6, 4, 1, 2, 5, 2], 20)
