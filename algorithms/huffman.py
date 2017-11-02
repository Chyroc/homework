# 定义节点
class Node:
    def __init__(self, weight=0, left=None, right=None):
        # 权重
        self.weight = weight

        # 左右子树
        self.left = left
        self.right = right

        # 是否是原生数据
        self.is_original = True


# 按权值排序
def sort(list):
    # 根据权重对list排序
    # 因为哈夫曼树算法，要求的就是将两个权重最小的加起来
    return sorted(list, key=lambda node: node.weight)


# 构建哈夫曼树
def Huffman(list):
    while len(list) != 1:
        # 去除最小的两个点
        a, b = list[0], list[1]
        # 构造他们的父树，权重为他们之和
        new = Node()
        new.weight = a.weight + b.weight
        new.is_original = False
        new.left, new.right = a, b
        # 去掉已经计算过的a和b，加上这个父节点
        list.remove(a)
        list.remove(b)
        list.append(new)
        # 排序，保证前两个节点永远是最小的
        list = sort(list)

    # 当循环结束的时候，list就是哈夫曼树的根节点
    return list
    # 中序遍历


# 获得编码
# 先序遍历
# 在哈夫曼编码里，默认将左边路径设为0，右边的路径设为1
def get_encode(node, data):
    # 处理父节点
    if node is None:
        return

    # 遍历左子树，路径加 0
    if node.left is not None:
        encode_list.append('0')
        d = get_encode(node.left, data)
        # 只有找到数据的时候，返回的才不是Node
        # 所以如果不是None，就是找到数据了，那么直接返回吧
        if d is not None:
            return d

    # 找到数据，返回路径
    if node.weight == data and node.is_original:
        return ''.join(encode_list)

    # 如果左子树不为空，路径肯定加过 0 ，现在掉头，去掉这个0
    if node.left is not None:
        encode_list.pop()

    # 遍历右子树，路径加 1
    if node.right is not None:
        encode_list.append('1')
        d = get_encode(node.right, data)
        # 只有找到数据的时候，返回的才不是Node
        # 所以如果不是None，就是找到数据了，那么直接返回吧
        if d is not None:
            return d

    # 如果右子树不为空，路径肯定加过 1 ，现在掉头，去掉这个1
    if node.right is not None:
        encode_list.pop()


if __name__ == '__main__':
    # 构造数据和哈夫曼树
    list = []
    for i in range(1, 11):
        # 构造10个数据，组成list
        list.append(Node(i))

    # 将这10个数据构造成了哈夫曼树，head是根节点
    list = sort(list)
    head = Huffman(list)[0]

    # 计算各数据的编码
    for i in range(1, 11):
        # encode_list 记录的是前序遍历的路径，如果找到那个i了，那么encode_list就是哈夫曼编码
        encode_list = []
        print('{} \t的编码是 {}'.format(i, get_encode(head, i)))
