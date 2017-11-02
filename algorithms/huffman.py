# 定义节点
class Node:
    def __init__(self, weight=0, left=None, right=None):
        self.weight = weight
        self.left = left
        self.right = right
        self.is_original = True


# 按权值排序
def sort(list):
    return sorted(list, key=lambda node: node.weight)


# 构建哈夫曼树
def Huffman(list):
    while len(list) != 1:
        a, b = list[0], list[1]
        new = Node()
        new.weight = a.weight + b.weight
        new.is_original = False
        new.left, new.right = a, b
        list.remove(a)
        list.remove(b)
        list.append(new)
        list = sort(list)
    return list
    # 中序遍历


def traval(First):
    if First == None:
        return
    traval(First.left)
    print(First.weight)
    traval(First.right)


# 获得树的长度
def get_height(node):
    if node.left == None and node.right == None:
        print(node.weight, node.is_original)
        return 1
    return get_height(node.left) + get_height(node.right)


# 获得编码
def get_encode(node, data):
    if node is None:
        return

    if node.left is not None:
        encode_list.append('0')
        d = get_encode(node.left, data)
        if d is not None:
            return d

    if node.weight == data and node.is_original:
        return ''.join(encode_list)

    if node.left is not None:
        encode_list.pop()

    if node.right is not None:
        encode_list.append('1')
        d = get_encode(node.right, data)
        if d is not None:
            return d

    if node.right is not None:
        encode_list.pop()


if __name__ == '__main__':
    # 构造数据和哈夫曼树
    list = []
    for i in range(1, 11):
        list.append(Node(i))

    list = sort(list)
    head = Huffman(list)[0]

    # 计算各数据的编码
    for i in range(1, 11):
        encode_list = []
        print('{} \t的编码是 {}'.format(i, get_encode(head, i)))
