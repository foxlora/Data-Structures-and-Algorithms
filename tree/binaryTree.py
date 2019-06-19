'''
实现一个二叉排序（搜索）树
ALL：
Time：2019-06-07
'''

class tree_node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


class binary_search_tree:
    def __init__(self):
        self.root = None


#实现 树深、结点个数查询
    def height(self):
        return self.__height(self.root)

    def __height(self, root):
        if not root:
            return -1
        left_height = self.__height(root.left)
        right_height = self.__height(root.right)
        # return 1+(left_height if left_height>right_height else right_height)#这种方式是自己写的，后面两种高大上的是网上偷学的^_^
        # return 1+[left_height,right_height][left_height<right_height]
        return 1 + (left_height > right_height and [left_height] or [right_height])[0]

    def count(self):
        '''elements in tree'''
        return self.__count(self.root)

    def __count(self, root):
        if not root:
            return 0
        return 1 + self.__count(root.left) + self.__count(root.right)





#前序遍历、中序遍历、后序遍历 实现
    def preorder(self):
        print('preorder: ',end='')
        self.__preorder(self.root)
        print('')

    def __preorder(self, root):
        if not root:
            return
        print(root.key,end=' ')
        self.__preorder(root.left)
        self.__preorder(root.right)

    def preorder_iter(self):
        s,res = [],[]
        root = self.root
        s.append(root)
        while s:
            u = s.pop()
            if u:
                res.append(u.key)
                s.append(u.right)
                s.append(u.left)
        return res



    def inorder(self):
        print('inorder: ',end='')
        self.__inorder(self.root)
        print('')

    def __inorder(self, root):
        if not root:
            return
        self.__inorder(root.left)
        print(root.key,end=' ')
        self.__inorder(root.right)





    def inorder_iter(self):
        root = self.root
        s,res = [],[]

        while root or s:
            if root:
                s.append(root)
                root = root.left
            else:
                root = s.pop()
                res.append(root.key)
                root = root.right
        return res





    def postorder(self):
        print('postorder: ',end='')
        self.__postorder(self.root)
        print('')


    def __postorder(self, root):
        if not root:
            return
        self.__postorder(root.left)
        self.__postorder(root.right)
        print(root.key,end=' ')



    def postorder_iter(self):
        root = self.root
        s,res = [],[]
        s.append(root)
        a = []
        while s:
            u = s.pop()
            res.append(u)
            if u.left:
                s.append(u.left)
            if u.right:
                s.append(u.right)
        while res:
            a.append(res.pop().key)

        return a

#实现插入操作
    def insert(self, key):
        '''recursion'''
        self.root = self.__insert(self.root, key)

    def __insert(self, root, key):
        if not root:
            root = tree_node(key)
        else:
            if key < root.key:
                root.left = self.__insert(root.left, key)
            elif key > root.key:
                root.right = self.__insert(root.right, key)
            else:
                print(key, 'is already in the tree')

        return root

    #non-recursion
    #    def insert(self, key):
    #        if not self.root:
    #            self.root = tree_node(key)
    #        else:
    #            cur = self.root
    #            while True:
    #                if key < cur.key:
    #                    if not cur.left:
    #                        cur.left = tree_node(key)
    #                        break
    #                    cur = cur.left
    #                elif key > cur.key:
    #                    if not cur.right:
    #                        cur.right = tree_node(key)
    #                        break
    #                    cur = cur.right
    #                else:
    #                    print(key, 'is already in tree')
    #                    break



#实现删除操作
    def delete(self, key):
        self.root = self.__delete(self.root, key)

    ##
    ##删除操作：
    ##首先找到删除的节点，
    ##1. 如果左右子树都不为空，则找到右子树中最小的节点min，用min.key代替删除节点的key，然后再到右子
    ##	 树中删除min节点,因为min没有左节点，所以删除它的话只需要用它的右节点代替它(如果有右节点)；
    ##2. 如果左子树或者右子树不为空，则直接代替掉
    ##3. 如果左右均空即叶子节点，直接删掉
    def __delete(self, root, key):
        if not root:
            print('not find key:%d'%key)
        elif key < root.key:
            root.left = self.__delete(root.left, key)
        elif key > root.key:
            root.right = self.__delete(root.right, key)
        elif root.left and root.right:  # found
            right_min = self.__find_min(self.root.right)
            root.key = right_min.key
            root.right = self.__delete(root.right, right_min.key)
        elif root.left:
            root = root.left
        elif root.right:
            root = root.right
        else:
            root = None  # python的GC会在没有引用指向对象的时候销毁对象

        return root


#实现查询操作
    def find(self, key):
        node = self.__find(self.root, key)
        if not node:
            print('not found')
        return node

    def __find(self, root, key):
        if not root:
            return None
        if key < root.key:
            return self.__find(root.left, key)
        elif key > root.key:
            return self.__find(root.right, key)
        else:
            return root



#实现 寻找最小值
    def find_min(self):
        return self.__find_min(self.root)

    def __find_min(self, root):
        if not root.left:
            return root
        return self.__find_min(root.left)



#实现寻找最大值
    def find_max(self):
        return self.__find_max(self.root)

    def __find_max(self, root):
        if not root.right:
            return root
        return self.__find_max(root.right)


def main():
    import random
    root = binary_search_tree()
    for i in random.sample([j for j in range(100)], 15):
        root.insert(i)
    # for j in range(20):
    #     root.insert(j)



    print(root.preorder_iter())
    print(root.inorder_iter())
    print(root.postorder_iter())
    root.preorder()
    root.inorder()
    root.postorder()

    print('height: ', root.height())
    print('count: ', root.count())
    print('min: ', root.find_min().key)
    print('max: ', root.find_max().key)




if __name__ == '__main__':
    main()

