#coding=utf-8

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