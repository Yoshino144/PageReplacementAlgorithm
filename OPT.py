# coding=utf-8
import sys


class OPT:
    # 初始化函数
    def __init__(self, memorySize, pageArr):
        # 内存块数
        self.memorySize = memorySize
        # 页面数组
        self.pageArr = pageArr
        # 页面数组 长度
        self.pageArrLen = len(self.pageArr)
        # 结果列表 初始化二维数组值为-1 如：[ [-1,-1,-1,-1] , [-1,-1,-1,-1] , [-1,-1,-1,-1] ]
        self.list = [[-1 for i in range(0, self.pageArrLen)] for j in range(0, self.memorySize)]
        # 初始化 缺页次数
        self.pageMissSize = 0
        # 初始化 缺页率
        self.pageMissRate = 0
        # 调度队列 初始化一维数组为-1 如：[-1,-1,-1,-1]
        self.queue = []
        # 记录 页面数组 的坐标
        self.pos = 1
        # 缺页次数
        self.ci = 0
        # 执行opt算法
        self.opt()

    # 将 num 放入到list中，pos代表页面数组 的坐标，从第几列开始放，meNum代表放入内存那一块，第几行开始放
    def putIn_list(self, num, col, meNum):
        for i in range(col, self.pageArrLen):
            self.list[meNum][i] = num

    # 判断 第col个元素 是否包含在内存中
    def equation(self, col):
        # 循环0到self.memorySize ,self.memorySize为内存块数
        for i in range(0, self.memorySize):
            # 如果 self.pageArr[col]包含在内存中
            if self.pageArr[col] == self.list[i][col - 1]:
                # 返回 true
                return True
        # 返回 false
        return False

    # 求start到 下一个num的距离
    def juli(self, num, start):
        # 循环 从start 到 page的长度
        for i in range(start, self.pageArrLen):
            # 如果 num 等于 page中的值
            if num == self.pageArr[i]:
                # 返回 距离
                return i

        # 如果没有，返回最大值 类似无穷大
        return sys.maxsize

    # opt算法函数
    def opt(self):
        # 先将第一个页面值放入内存中  代表现在是第一个值
        self.putIn_list(self.pageArr[0], 0, 0)
        self.queue.append(self.pageArr[0])

        # 从第二个开始放，直到放满内存
        for i in range(1, self.pageArrLen):

            # 判断是否放慢内存，放慢结束循环 通过判断内存中最后一块是否是-1 ，如果不是表示内存已经放满
            if self.list[self.memorySize - 1][i - 1] != -1:
                break

            # 如果没放满 ，判断内存中是否有这个数
            if self.equation(i):
                continue
            else:
                # 没有将这个数放入到内存中self.pageArr[i]放入list的 第pos行 第i列
                self.putIn_list(self.pageArr[i], i, self.pos)
                self.queue.append(self.pageArr[i])
                self.pos += 1
                self.ci += 1

        # 循环从pos开始，接着上面放满之后的继续放，将每个页面数组内容放入内存
        for i in range(self.pos + 1, self.pageArrLen):
            # 判断第i个元素是否已经在内存中
            if self.equation(i):
                # 在的话，跳过这个元素
                continue
            else:
                # 不在的话
                # 记录最大值
                Max = 0
                # 记录最大值的坐标
                MaxPos = 0
                # 遍历内存块，获取内存中每一个元素
                for row in range(0, self.memorySize):
                    # 求每一个元素在之后页面的距离
                    temp = self.juli(self.list[row][i - 1], i)
                    # 判断这个元素是否是最远的
                    if temp > Max:
                        Max = temp
                        MaxPos = row
                # 将最远的元素替换到内存中相应位置
                self.putIn_list(self.pageArr[i], i, MaxPos)
                self.queue.append(self.pageArr[i])
                self.ci += 1

        # 输出结果---------------------------------------------------------------------------start
        self.res = ""
        self.res = self.res + "|---"
        for j in range(0, self.pageArrLen - 2):
            self.res = self.res + "+---"
        self.res = self.res + "+---|\n"

        for j in range(0, self.pageArrLen):
            self.res = self.res + "|%2d" % (self.pageArr[j]) + " "
        self.res = self.res + '|\n'
        self.res = self.res + "|---"
        for j in range(0, self.pageArrLen - 2):
            self.res = self.res + "+---"
        self.res = self.res + "+---|\n"
        for j in range(0, self.memorySize):
            for i in range(0, self.pageArrLen):
                if self.list[j][i] == -1:
                    self.res = self.res + "|%2c" % (32) + " "
                else:
                    self.res = self.res + "|%2d" % (self.list[j][i]) + " "
            self.res = self.res + "|\n"

        self.res = self.res + "|---"
        for j in range(0, self.pageArrLen - 2):
            self.res = self.res + "+---"
        self.res = self.res + "+---|\n"
        self.res = self.res + "队列：" + str(self.queue)
        # print(self.res)
        # 输出结果---------------------------------------------------------------------------end

    def get_res(self):
        return self.res

    def get_lv(self):
        return self.ci / self.pageArrLen

    def get_ci(self):
        return self.ci


# 主函数
if __name__ == "__main__":
    OPT(3, [1, 2, 3, 4, 1, 5, 2, 3, 1, 8, 9])
