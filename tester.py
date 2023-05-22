import math
import random
from AVLTree import AVLTree, AVLNode

def test_successor_predecessor():
    n03 = AVLNode(3,0)
    n05 = AVLNode(5,0)
    n08 = AVLNode(8,0)
    n10 = AVLNode(10,0)
    n17 = AVLNode(17,0)
    n20 = AVLNode(20,0)
    n10.right = n20
    n10.left = n05
    n05.left = n03
    n05.right = n08
    n20.left = n17
    n03.parent=n05
    n08.parent=n05
    n05.parent=n10
    n17.parent=n20
    n20.parent=n10

    n03.left=AVLNode(None,0)
    n03.right=AVLNode(None,0)
    n17.left=AVLNode(None,0)
    n17.right=AVLNode(None,0)
    n08.right=AVLNode(None,0)
    n08.left=AVLNode(None,0)
    n20.right=AVLNode(None,0)
    tree = AVLTree()
    tree.root = n10
    assert tree.successor(n03) == n05
    assert tree.successor(n05) == n08
    assert tree.successor(n08) == n10
    assert tree.successor(n10) == n17
    assert tree.successor(n17) == n20
    assert tree.successor(n20) is None
    # assert tree.predecessor(n03) is None
    # assert tree.predecessor(n05) == n03
    # assert tree.predecessor(n08) == n05
    # assert tree.predecessor(n10) == n08
    # assert tree.predecessor(n17) == n10
    # assert tree.predecessor(n20) == n17

# test_successor_predecessor()

def test_rotation():
    n03 = AVLNode(3,0)
    n05 = AVLNode(5,0)
    n08 = AVLNode(8,0)
    n10 = AVLNode(10,0)
    n17 = AVLNode(17,0)
    n20 = AVLNode(20,0)
    n10.right = n20
    n10.left = n05
    n05.left = n03
    n05.right = n08
    n20.left = n17
    n03.parent=n05
    n08.parent=n05
    n05.parent=n10
    n17.parent=n20
    n20.parent=n10

    n03.left=AVLNode(None,0)
    n03.right=AVLNode(None,0)
    n17.left=AVLNode(None,0)
    n17.right=AVLNode(None,0)
    n08.right=AVLNode(None,0)
    n08.left=AVLNode(None,0)
    n20.right=AVLNode(None,0)
    tree = AVLTree()
    tree.root = n10

    
    


# def inserttest():
#     tree=AVLTree()
#     tree.insert(10, 10)
#     tree.insert(5, 5)
#     tree.insert(3, 3)
#     tree.insert(8, 8)
#     tree.insert(20, 20)
#     tree.insert(17,17)
#     tree.insert(18, 18)
#     tree.insert(-2, -2)
#     tree.insert(-4, -4)
#     tree.insert(-6, -6)

#     tree.printTree(tree.get_root())
    
#     print('____________________________')
    
#     print(tree.get_root().get_left().get_left().get_left().get_left().get_key())
#     print(tree.get_root().get_left().get_left().get_left().get_key())
#     print(tree.get_root().get_left().get_left().get_key())
#     print(tree.get_root().get_left().get_key())
#     print(tree.get_root().get_left().get_right().get_key())
#     print(tree.get_root().get_key())
#     print(tree.get_root().get_right().get_left().get_key())
#     print(tree.get_root().get_right().get_key())
# inserttest()

# def test_rotation():
#     tree=AVLTree()
#     tree.insert(0,0)
#     tree.insert(0,0)
#     tree.insert(1, 1)
#     tree.insert(2, 2)
#     tree.insert(3,3)
#     tree.insert(4,4)
#     tree.insert(5,5)
#     # tree.insert(0, 0)
#     # tree.insert(0,0)
#     # tree.insert(0,1)
#     # tree.insert(1,2)
#     # tree.insert(1,3)
#     # tree.insert(2,4)

#     # tree.insert(0,2)
#     # tree.insert(2,3)
#     # tree.insert(0,4)
#     # tree.insert(2,5)
#     # tree.insert(4,6)
#     # tree.insert(5,7)

#     # tree.insert(0, 2)
#     # tree.insert(0, 3)
#     # tree.insert(0, 4)
#     # tree.insert(0, 5)
#     # x=tree.insert(0, 6)

#     print('____________________________')
#     print('____________________________')
#     print('____________________________')
#     print(tree.size)
#     print(tree.get_root())
#     print(tree.get_root().get_left())
#     print(tree.get_root().get_right())
#     print(tree.get_root().get_left().get_left())
#     print(tree.getRoot().get_left().getRight())
#     print("retrieve:")
#     print(tree.retrieve(2))
#     print("number of rotations")
#     #print(x)
#     tree.printTree(tree.getRoot())
#     print(tree.get_root().get_left().is_real_node())

# def random_insert_delete(n):
#     def _ins(index, v):
#         return tree.insert(index , v)

#     def _del(index):
#         return tree.delete(index)
#     rotations = 0
#     tree=AVLTreeList()
#     for i in range(0, n//2):
#         if(tree.getSize() == 0):
#             rotations += _ins(0, i)
#         index = random.randrange(tree.getSize())
#         rotations += _ins(index, i)

#     rotations_2 = 0
#     for i in range(n//4):
#         index1 = random.randrange(tree.getSize())
#         rotations_2 += _ins(index1, i)
#         index2 = random.randrange(tree.getSize())
#         rotations_2 += _del(index2)

#     return (rotations, rotations_2)

def test_delete():
    tree = AVLTree()
    tree.insert(10, 10)
    tree.insert(5, 5)
    tree.insert(3, 3)
    tree.insert(8, 8)
    tree.insert(20, 20)
    tree.insert(17,17)
    tree.insert(18, 18)
    tree.insert(-2, -2)
    tree.insert(-4, -4)
    tree.insert(-6, -6)

    tree.printTree(tree.get_root())

    tree.delete(tree.get_root().get_right())
    # tree.delete(tree.get_root())
    # tree.delete(tree.get_root().get_left().get_left())
    # tree.delete(tree.get_root().get_left().get_right())
    # tree.delete(tree.get_root().get_left())
    # tree.printTree(tree.get_root())
    # tree.delete(tree.get_root().get_left())
    tree.printTree(tree.get_root())

# test_delete()

def test_search():
    tree = AVLTree()
    tree.insert(10, 10)
    tree.insert(5, 5)
    tree.insert(3, 3)
    tree.insert(8, 8)
    tree.insert(20, 20)
    tree.insert(17,17)
    tree.insert(18, 18)
    tree.insert(-2, -2)
    tree.insert(-4, -4)
    tree.insert(-6, -6)
    tree.printTree(tree.get_root())

    print(tree.search(tree.get_root().get_key()).get_key())
    print(tree.search(tree.get_root().get_right().get_right().get_key()).get_key())
    print(tree.search(2))

# test_search()

def test_size():
    tree = AVLTree()
    tree.insert(10, 10)
    tree.insert(5, 5)
    tree.insert(3, 3)
    tree.insert(8, 8)
    tree.insert(20, 20)
    tree.insert(17,17)
    tree.insert(18, 18)
    tree.insert(-2, -2)
    tree.insert(-4, -4)
    tree.insert(-6, -6)

    print(tree.size())

def test_rank():
    tree = AVLTree()
    tree.insert(10, 10)
    tree.insert(5, 5)
    tree.insert(3, 3)
    tree.insert(8, 8)
    tree.insert(20, 20)
    tree.insert(17,17)
    tree.insert(18, 18)
    tree.insert(-2, -2)
    tree.insert(-4, -4)
    tree.insert(-6, -6)
    print(tree.rank(tree.get_root().get_left().get_left().get_left()))

def test_select():
    tree = AVLTree()
    tree.insert(10, 10)
    tree.printTree(tree.get_root())
    tree.insert(5, 5)
    tree.insert(3, 3)
    tree.insert(8, 8)
    tree.insert(20, 20)
    tree.insert(17,17)
    tree.insert(18, 18)
    tree.insert(-2, -2)
    tree.insert(-4, -4)
    tree.insert(-6, -6)

    print(tree.select(1).get_key())

# test_select()

def test_avl_to_array():
    tree = AVLTree()
    tree.insert(10, 10)
    # tree.printTree(tree.get_root())
    # tree.insert(5, 5)
    # tree.insert(3, 3)
    # tree.insert(8, 8)
    # tree.insert(20, 20)
    # tree.insert(17,17)
    # tree.insert(18, 18)
    # tree.insert(-2, -2)
    # tree.insert(-4, -4)
    # tree.insert(-6, -6)
    print(tree.avl_to_array())
# test_avl_to_array()
def test_join_split():
    tree1 = AVLTree()
    tree1.insert(10, 10)
    tree1.insert(5, 5)
    tree1.insert(3, 3)
    tree1.insert(8, 8)
    tree1.insert(17,17)
    tree1.insert(18, 18)
    tree1.insert(-2, -2)
    tree1.insert(-4, -4)
    tree1.insert(-6, -6)

    # tree1.printTree(tree1.get_root())

    tree2 = AVLTree()
    tree2.insert(21, 21)
    tree2.insert(30, 30)
    tree2.insert(25, 25)
    tree2.insert(26,26)
    tree2.insert(27, 27)

    # tree2.printTree(tree2.get_root())

    tree1.join(tree2, 20, 20)

    # tree1.printTree(tree1.get_root())

    tree1.printTree(tree1 .get_root())

    print(tree1.split(tree1.get_root().get_right()))

# test_join_split()

# def test_join_finger():
#     tree1 = AVLTree()
#     # case 1 the array is reverse sorted
#     # n = 1500 * 2^i
#     n = 48000
#     arr = [n+1 -i for i in range(1, n+1)]
#     for k in arr:
#         tree1.insertFinger(k, k)
#     print(tree1.counter)
#         # tree1.printTree(tree1.get_root())
#     print("------------------------------------------")
#     # case 2 the array is random
#     # tree2 = AVLTree()
#     # # random.shuffle(arr)
#     # count2 = 0
#     # for i in range (len(arr)):
#     #     for j in range(i+1, len(arr)):
#     #         if(arr[j] < arr[i]):
#     #             count2 += 1
#     # print(arr)
#     # print("counter2 :" + str(count2))
#     # for k in arr:
#     #     tree2.insertFinger(k, k)
#     # print(tree2.counter)
#     print("--------------------------------------------")
#     tree3 = AVLTree()
#     # case 3:
#     n = 48000
#     arr = []
#     for i in range(1, n+1, 300):
#         temp = [j for j in range(i,i+300)]
#         arr += temp[:: -1]
    
#     count2 = 0
#     for i in range (len(arr)):
#         for j in range(i+1, len(arr)):
#             if(arr[j] < arr[i]):
#                 count2 += 1
#     print("counter2 :" + str(count2))

#     for k in arr:
#         tree3.insertFinger(k, k)
#     print(tree3.counter)


    
    
# test_join_finger()




# def create_list_tree(n):
#     tree=AVLTree()
#     list = []
#     tree.insert(0, 0)
#     list.insert(0, 0)
#     for i in range(1, n):
#         index = random.randrange(len(list))
#         rand = random.randrange(2**10)
#         print('inserting ' + str(i) + ' at ' + str(index))
#         # list.insert(index, rand)
#         tree.insert(index, rand)
#     return tree

# create_list_tree(100)

# def test_insert_delete(_list, _tree, n):
#     def execute_assertions():
#         assert(len(list) == tree.get_size())
#         for i in range(1,len(list)):
#             node = tree.retrieve(i)
#             expected = list[i]
#             returned = node.value
#             assert (list[i] == tree.retrieve(i).value)
#             assert node.getBF() <= 1
#             assert (i == len(list) - 1 or tree.successor(node).value == list[i+1])
#             assert (i == 0 or tree.predecessor(node).value == list[i - 1] )
#             # assert(tree.search(returned) == i)
#             if(tree.get_Size() > 0):
#                 assert tree.last().value == list[-1]
#                 assert tree.first().value == list[0]
#             else: 
#               !!  assert tree.last() == None
#               !!  assert tree.first() == None
#             def print_err(i, e, r):
#                 print("ERROR!")
#                 print("index: " +str(i))
#                 print("expected: " +str(e))
#                 print("returned: " +str(r))
#     def _ins(index, v):
#         print('inserting ' + str(v) + ' at ' + str(index))
#         list.insert(index, v)
#         tree.insert(index , v)
#     def _del(index):
#         print('deleting ' + ' at ' + str(index))
#         list.pop(index)
#         tree.delete(index)

#     print('**********************************************************************************')
#     tree=AVLTree() if _tree is None else _tree
#     list = [] if _list is None else _list
#     print('______')
#     print('______')
#     print('final tree:')
#     tree.printTree(tree.root)
#     print('final List:')
#     print(list)
#     print('______')
#     print('______')

#     execute_assertions()

#     for i in range(0, n):
#         if(len(list) == 0):
#             _ins(0, i)
#         else:
#             coin = random.randrange(8)
#             if(coin <= 5):
#                 index = random.randrange(len(list))
#                 _ins(index, i)
#             else:
#                 index = random.randrange(len(list))
#                 _del(index)

#     print('______')
#     print('______')
#     print('final tree:')
#     tree.printTree(tree.root)
#     print('final List:')
#     print(list)
#     print('______')
#     print('______')


#     execute_assertions()
            
        
# def test_concat():
#     x=create_list_tree(5)
#     y=create_list_tree(1)
#     tree1=x[0]
#     list1=x[1]
#     tree2=y[0]
#     list2=y[1]
#     print("***************tree1******************")
#     tree1.printTree(tree1.root)
#     print(list1)
#     print(tree1.getSize())
#     print("***************tree2******************")
#     tree2.printTree(tree2.root)
#     print(list2)
#     print(tree2.getSize())
#     print("***************after concat******************")
#     tree1.concat(tree2)
#     tree1.printTree(tree1.root)
#     test_insert_delete(list1+list2,tree1,20)

# def test_concat2(n):
#     rand1 = random.randrange(1, n)
#     rand2 = random.randrange(1, n)

#     tree1, list1 = create_list_tree(rand1)
#     tree2, list2 = create_list_tree(rand2)
#     print('...............................................................')
#     print_tree(tree1.getRoot())
#     print('\n\n\n')
#     print_tree(tree2.getRoot())
#     print(list1)
#     print(list2)
#     print('...............................................................\n\n')
#     tree1.concat(tree2)
#     list = list1 + list2
#     test_insert_delete(list, tree1, 20)

    
# def test_arrayToList():
#     lst = list(range(0,100))
#     tree = atl(lst)
#     print_tree(tree.getRoot())
#     print(tree.retrieve(6).parent)

#     for i in range(0,len(lst)):
#         expected = lst[i]
#         returned = tree.retrieve(i).value
#         print(expected, returned)
#         assert (lst[i] == tree.retrieve(i).value), print_err(i, expected, returned)
#         def print_err(i, e, r):
#             print("ERROR!")
#             print("index: " +str(i))
#             print("expected: " +str(e))
#             print("returned: " +str(r))
#     test_insert_delete(lst, tree, 200)

# def test_listToArray():
#     tree, arr = create_list_tree(20)
#     _arr = tree.listToArray()
#     assert arr == _arr
    

# def test_permutations():
#     tree, arr = create_list_tree(20)
#     shuffled = tree.permutation()
#     print('Before: ')
#     print_tree(tree.getRoot())
#     print('After: ')
#     print_tree(shuffled.getRoot())
#     assert shuffled.getSize() == tree.getSize()
    
# def test_sorting():
#     tree, arr = create_list_tree(70)
#     sortedlist = tree.sort()
#     print('Before: ')
#     print_tree(tree.getRoot())
#     print('After: ')
#     print_tree(sortedlist.getRoot())
#     print(sortedlist.getRoot())
#     print(sorted(arr))
#     print(sortedlist.listToArray())
#     assert (sorted(arr) == sortedlist.listToArray())
#     assert sortedlist.getSize() == tree.getSize()





# # for i in range(100):
# #     for k in range(math.ceil(10 + 1000/(i+1))):
# #         test_insert_delete(None, None, i)

# for i in range(100):
#   test_concat2(40)

# for i in range(100):
#     for k in range(math.ceil(100 + 1000/(i+1))):
#         test_insert_delete(None, None, i)

def calcuRandRand2(i):
    tree = buildTree(1500*math.pow(2,int(i)))
    num1 = random.randint(1, 1500*math.pow(2,i))
    node = tree.search(num1)
    tree.split2(node)
    # print(tree.printTree(node))
    # print(num1)
    
		
		
		
def buildTree(i):
    newTree = AVLTree()
    values = list(range(1, int (i+1)))
    random.shuffle(values)
    for value in values:
        newTree.insert(value,value)
    return newTree


calcuRandRand2(1)
