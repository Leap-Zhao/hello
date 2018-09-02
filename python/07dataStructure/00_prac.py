# coding=utf-8

# 树
# 树结点类(data,lchild,rchild)
# 树类(init,add,travel)

class TreeNode(object):
    def __init__(self,data):
        self.data = data 
        self.lchild = None
        self.rchild = None

class Tree(object):
    def __init__(self):
        self.root = None

    def add(self,data):
        new_tree_node = TreeNode(data)

        if self.root == None:
            self.root = new_tree_node
            return
        else:
            # 定义一个列表来表示存储树的队列
            queue = []
            queue.append(self.root)
            while queue:
                cur_node = queue.pop(0)
                if cur_node.lchild == None:
                    cur_node.lchild = new_tree_node
                    return
                elif cur_node.rchild == None:
                    cur_node.rchild = new_tree_node
                    return
                else:
                    queue.append(cur_node.lchild)
                    queue.append(cur_node.rchild)  

    def guangdu_travel(self,root):
        if root is None:
            return
        else:
            queue = []
            queue.append(root)
            while queue:
                cur_node = queue.pop(0)
                print(cur_node.data),
                if cur_node.lchild != None:
                    queue.append(cur_node.lchild)
                if cur_node.rchild != None:
                    queue.append(cur_node.rchild)

    def shendu_xianxu(self,root):
        if root is None:
            return
        else:
            print(root.data),
            self.shendu_xianxu(root.lchild)
            self.shendu_xianxu(root.rchild)

    def shendu_zhongxu(self,root):
        if root is None:
            return
        else:
            self.shendu_zhongxu(root.lchild)
            print(root.data),
            self.shendu_zhongxu(root.rchild)

    def shendu_houxu(self,root):
        if root is None:
            return 
        else:
            self.shendu_houxu(root.lchild)
            self.shendu_houxu(root.rchild)
            print(root.data),

def quick_sort(alist,first,last):
    # 结束递归的条件:
    if first >= last:
        return

    n = len(alist)
    low = first 
    high = last
    mid_value = alist[low]
    while low < high:
        while low < high and alist[high] >= mid_value:
            high -=1
        alist[low] = alist[high]
        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]
    alist[low] = mid_value

    # 递归调用
    quick_sort(alist, first, low-1)
    quick_sort(alist, low+1, last)

# 选择排序
def select_sort(alist):
    n = len(alist)
    for i in range(0,n-1):
        min_index = i
        for j in range(min_index+1,n):
            if alist[min_index] > alist[j]:
                min_index = j
        alist[i],alist[min_index] = alist[min_index],alist[i]

def exchange_element(alist,low,high):
    temp = alist[low]
    j = 2*low
    while j <= high:
        if j<high and alist[j] < alist[j+1]:
            j+=1
        if temp > alist[j]:
            break
        alist[low] = alist[j]
        low = j
        j = 2*j
    alist[low] = temp

def top_heap_sort(alist):
    n = len(alist)-1
    for i in range(n//2,0,-1):
        exchange_element(alist,i,n)

    for j in range(n,1,-1):
        alist[1],alist[j] = alist[j],alist[1]
        exchange_element(alist,1,j-1)

def bubble_sort(alist):
    n = len(alist)
    for i in range(n-1,0,-1):
        # j= n-1,n-2,...1
        count = 0
        for j in range(0,i):
            if alist[j] > alist[j+1]:
                alist[j],alist[j+1] = alist[j+1],alist[j]
                count += 1
        if count == 0:
            return

def select_sort(alist):
    n = len(alist)
    for i in range(0,n):
        min_index = i
        for j in range(min_index,n):
            if alist[j] < alist[min_index]:
                min_index = j
        alist[min_index],alist[i] = alist[i],alist[min_index]

def insert_sort(alist):
    n = len(alist)
    for i in range(1,n):
        # j=1,2,3...n-1
        for j in range(i,0,-1):
            if alist[j-1] > alist[j]:
                alist[j-1],alist[j] = alist[j],alist[j-1]
            else:
                break

def shell_sort(alist):
    n = len(alist)
    gap = n//2
    while gap > 0:
        for i in range(gap,n):
            j = i
            while j>=gap and alist[j-gap] > alist[j]:
                alist[j-gap],alist[j] = alist[j],alist[j-gap]
                j -= gap
        gap = gap//2


if __name__ == "__main__":
    # tree = Tree()
    # tree.add(0)
    # tree.add(1)
    # tree.add(2)
    # tree.add(3)
    # tree.add(4)
    # tree.add(5)
    # tree.add(6)
    # tree.add(7)
    # tree.add(8)
    # tree.add(9)

    # tree.guangdu_travel(tree.root)
    # print("")
    # tree.shendu_xianxu(tree.root)
    # print("")
    # tree.shendu_zhongxu(tree.root)
    # print("")
    # tree.shendu_houxu(tree.root)
    # print("")

    # heap_alist = [-1,7,6,9,5,8,4,3,2,1]
    # print(heap_alist)
    # top_heap_sort(heap_alist)
    # print(heap_alist)

    alist = [7,2,3,5,8,9]
    print(alist)
    shell_sort(alist)
    print(alist)
    # quick_sort(alist,0,len(alist)-1)
    # print(alist)
