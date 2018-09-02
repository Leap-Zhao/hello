# coding=utf-8

# 冒泡排序

def bubble_sort(alist):
    n = len(alist)
    for i in range(n-1,0,-1):
        for j in range(0,i):
            if alist[j] > alist[j+1]:
                alist[j],alist[j+1] = alist[j+1],alist[j]

# 选择排序
def select_sort(alist):
    n = len(alist)
    for i in range(0,n-1):
        min_index = i
        for j in range(i,n-1):
            if alist[min_index] > alist[j+1]:
                min_index = j+1
        alist[i],alist[min_index] = alist[min_index],alist[i] 

# 插入排序
def insert_sort(alist):
    n = len(alist)
    for i in range(1,n):
        for j in range(i,0,-1):
            if alist[j] < alist[j-1]:
                alist[j],alist[j-1] = alist[j-1],alist[j]
            else:
                break


# 希尔排序
def shell_sort(alist):
    n = len(alist)
    gap = n//2
    while gap >= 1:
        for i in range(gap,n):
            for j in range(i,0,-gap):
                if alist[j-gap] > alist[j]:
                    alist[j-gap],alist[j] = alist[j],alist[j-gap]
                else:
                    break
        gap = gap//2

# 快速排序
def quick_sort(alist,first,last):
    if first >= last:
        return
    low = first
    high = last
    middle_value = alist[low]
    while low < high:
        while low < high and middle_value <= alist[high]:
            high -= 1
        alist[low] = alist[high]

        while low < high and alist[low] < middle_value:
            low += 1
        alist[high] = alist[low]
    alist[low] = middle_value

    quick_sort(alist,first,low-1)
    quick_sort(alist,low+1,last)



# 树结点
class TreeNode(object):
    def __init__(self,data):
        # 树结点数据
        self.data = data
        # 左子结点
        self.lchild = None
        # 右子结点
        self.rchild = None

# 树结构 
class Tree(object):
    def __init__(self):
        # 根结点是自带的,不是传递过来的
        self.root = None

    # 添加一个树结点
    def add(self,data):
        node = TreeNode(data)
        # 如果树为空树,则root为None,直接接此结点设为root
        if self.root is None:
            self.root = node
            return

        # 如果树不为空树,则用一个列表来代表一个队列,模拟树结点的广度优先遍历
        queue = [self.root]
        while queue:
            # 从队列头中取出父结点
            cur_node = queue.pop(0)
            
            # 如果父结点左子树为空,则直接添加结点
            # 如果父结点左子树不为空,则直接将左子树从队尾进入队列(下一次循环用)
            if cur_node.lchild == None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)

            # 接下来判断父结点的右子树,与左子树判断基本一致
            if cur_node.rchild == None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)

    # 树的层次遍历/广度遍历 
    def breadth_travel(self):
        # 如果树为空,直接返回
        if self.root is None:
            return 
        # 树不为空时
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.data),
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)
        print("")

    # 树的深度优先遍历有3种: 先序,中序,后序
    # 这里的序是指根结点,比如先序是先遍历根结点,中序是根结点在中间,后序是根结点在最后,而左右子结点的顺序是左永远在右前
    
    # 深度优先遍历的先序遍历
    def preorder(self,treenode):
        # 先序遍历递归的结束条件:当根结点为None时,说明无子树
        if treenode is None:
            return
        # 先序遍历,先打印根结点
        print(treenode.data),
        # 之后再对左子结点进行先序遍历
        self.preorder(treenode.lchild)
        # 之后再对右子结点进行先序遍历
        self.preorder(treenode.rchild)

    # 深度优先遍历的中序遍历
    def inorder(self,treenode):
        if treenode is None:
            return 
        self.inorder(treenode.lchild)
        print(treenode.data),
        self.inorder(treenode.rchild)

    # 深度优先遍历的后序遍历
    def posorder(self,treenode):
        if treenode is None:
            return
        self.posorder(treenode.lchild)
        self.posorder(treenode.rchild)
        print(treenode.data),

if __name__ == "__main__":
    alist = [9,7,5,3,4,6,8]
    print(alist)
    # bubble_sort(alist)
    # select_sort(alist)
    # quick_sort(alist,0,len(alist)-1)
    shell_sort(alist)
    print(alist)

    tree = Tree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.add(10)

    # 对树进行广度遍历
    tree.breadth_travel()

    # 对树进行深度优先遍历:先序遍历 
    tree.preorder(tree.root)
    print("")

    # 对树进行深度优先遍历:中序遍历
    tree.inorder(tree.root)
    print("")

    # 对树进行深度优先遍历:后序遍历
    tree.posorder(tree.root)
    print("")