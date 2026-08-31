from node import Node

def length(node, count=0):
    if node is None:
        return count
    else:
        value = node.get_value()
        next = node.get_next()
        rest = length(next)

def sum (a_node):
    total = 0
    while not (a_node == None):
        total += a_node.get_value ()
        a_node = a_node.get_next ()
    return total

def main():
    series = Node(3, Node (2, (Node(1))))
    print(series)

    print (length (series))
    print (sum (series))

main()

'''
5
5,8
8
8,3
3
3,1
'''