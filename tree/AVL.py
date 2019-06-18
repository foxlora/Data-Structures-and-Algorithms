'''
实现平衡二叉树
用途：适用于大量查询操作
Time:2019-06-10
Arthur:Foxlora
'''

class tree_node(object):
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class avl_tree(object):
    def __init__(self):
        self.root = None


#实现查询操作
    def find(self,key):
        node = self.__find(key,self.root)
        if not node:
            print("not found")
        return node

    def __find(self,key,root):
        if not root:
            return None
        if key < root.value:
            return self.__find(key, root.left)
        elif key > root.value:
            return self.__find(key, root.right)
        else:
            return root

    def find_min(self):
        return self.__find_min(self.root)

    def __find_min(self, root):
        if not root.left:
            return root.value
        return self.__find_min(root.left)

    def find_max(self):
        return self.__find_max(self.root)

    def __find_max(self, root):
        if not root.right:
            return root.value
        return self.__find_max(root.right)


    def height(self):
        return self.__height(self.root)

    def __height(self,root):
        if not root:
            return -1
        return 1 + max(self.__height(root.left),self.__height(root.right))

    def count_node(self):
        return self.__count_node(self.root)

    def __count_node(self,root):
        if not root:
            return 0
        return 1 + self.__count_node(root.left) + self.__count_node(root.right)

#前序遍历、中序遍历、后序遍历 实现
    def preorder(self):
        print('preorder: ',end='')
        self.__preorder(self.root)
        print('')
    def __preorder(self, root):
        if not root:
            return
        print(root.value,end=' ')
        self.__preorder(root.left)
        self.__preorder(root.right)

    def inorder(self):
        print('inorder: ',end='')
        self.__inorder(self.root)
        print('')
    def __inorder(self, root):
        if not root:
            return
        self.__inorder(root.left)
        print(root.value,end=' ')
        self.__inorder(root.right)

    def postorder(self):
        print('postorder: ',end='')
        self.__postorder(self.root)
        print('')
    def __postorder(self, root):
        if not root:
            return
        self.__postorder(root.left)
        self.__postorder(root.right)
        print(root.value,end=' ')


#插入操作
    def insert(self,key):
        self.root = self.__insert(key,self.root)
        #这里犯错了！！！！
        #return self.__insert(key,self.root)

    def __insert(self,key,root):
        if not root:
            root = tree_node(value=key)
        else:
            if key < root.value:
                root.left = self.__insert(key,root.left)
                if (self.__height(root.left) - self.__height(root.right)) == 2:
                    if key < root.left.value:
                        root = self.__single_left_rotate(root)
                    else:
                        root = self.__double_left_rotate(root)

            elif key > root.value:
                root.right = self.__insert(key,root.right)
                if (self.__height(root.right) - self.__height(root.left)) == 2:
                    if key < root.right.value:
                        root = self.__double_right_rotate(root)
                    else:
                        root = self.__single_right_rotate(root)

            else:
                print(key, 'is already in the tree')
        return root

    '''
    不平衡有四种情况：
    1.对K的左儿子的左子树进行一次插入，左单旋转
    2.对K的左儿子的右子树进行一次插入，左双旋转
    3.对K的右儿子的左子树进行一次插入，右双旋转
    4.对K的右儿子的右子树进行一次插入，右单旋转
    '''

    def __single_left_rotate(self, node):  # 左单旋转
        k1=node.left
        node.left=k1.right
        k1.right=node
        return k1

    def __single_right_rotate(self, node):  #右单旋转
        k1 = node.right
        node.right = k1.left
        k1.left = node
        #node.right,k1.left = k1.left,node
        return k1

    def __double_right_rotate(self,node):   #右双旋转
        node.right = self.__single_left_rotate(node.right)
        return self.__single_right_rotate(node)

    def __double_left_rotate(self,node):    #左双旋转
        node.left = self.__single_right_rotate(node.left)
        return self.__single_left_rotate(node)




# 删除操作
    '''
    1.当前节点为要删除的节点且是树叶（无子树），直接删除，当前节点（为None）的平衡不受影响。
    2.当前节点为要删除的节点且只有一个左儿子或右儿子，用左儿子或右儿子代替当前节点，当前节点的平衡不受影响。
    3.当前节点为要删除的节点且有左子树右子树:
        如果右子树高度较高，则从右子树选取最小节点，将其值赋予当前节点，然后删除右子树的最小节点。
        如果左子树高度较高，则从左子树选取最大节点，将其值赋予当前节点，然后删除左子树的最大节点。
        这样操作当前节点的平衡不会被破坏。
    4.当前节点不是要删除的节点，则对其左子树或者右子树进行递归操作。当前节点的平衡条件可能会被破坏，需要进行平衡操作。
    '''

    def delete(self,key):
        self.root = self.__delete(key,self.root)

    def __delete(self,key,root):
        if not root:
            print('not find key',key)
        elif key < root.value:
            root.left = self.__delete(key,root.left)
        elif key > root.value:
            root.right = self.__delete(key,root.right)
        elif root.left and root.right:  #情况3
            if self.__height(root.right) > self.__height(root.left):
                right_min = self.__find_min(root.right)
                root.value = right_min
                root.right = self.__delete(right_min,root.right)
            else:
                left_max = self.__find_max(root.left)
                root.value = left_max
                root.left = self.__delete(left_max,root.left)

        elif root.left:
            root = root.left
        elif root.right:
            root = root.right
        else:
            root = None

        return root
        






def main():
    import random
    root = avl_tree()
    # for i in random.sample([j for j in range(100)], 15):
    #     root.insert(i)
    for j in range(30):
        root.insert(j)
    root.insert(72)

    root.delete(24)

    root.preorder()
    root.inorder()
    root.postorder()



    print('height: ', root.height())
    print('count: ', root.count_node())
    print('min: ', root.find_min())
    print('max: ', root.find_max())




if __name__ == '__main__':
    main()