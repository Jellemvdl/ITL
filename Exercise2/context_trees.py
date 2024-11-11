def findLeftChild(t: int, i: int) -> int:
    if i >= len(t):
        return -1 # no left child
    if t[i] == '0':
        return -1 # no child since it is a leaf node
    
    position = i + 1

    return position

def findRightChild(t: int, i: int) -> int:
    if i >= len(t):
        return -1 # no right child
    if t[i] == '0':
        return -1 # leaf node
    left_position = i + 1
    if t[left_position] == '0':
        right_position = left_position + 1
        return right_position
    
    else: 
        count = 1
        right_position = left_position + 1
        while right_position < len(t) and count >= 0:
            if t[right_position] == '1':
                count += 1
            else: 
                count -= 1
            right_position += 1

        
        return right_position  
        

# print(findRightChild('11100100100', 0))

def printTree(t: str):
    def printSubTree(t: str, i: int, depth: int, child_type: str):
        if i == -1 or i >= len(t):
            return
        # Assign label based on child type
        if child_type == 'root':
            label = 'r'
        elif child_type == 'left':
            label = 'a'
        elif child_type == 'right':
            label = 'b'

        print('  ' * depth + label)
        # Find left and right children
        left_child = findLeftChild(t, i)
        right_child = findRightChild(t, i)

        # process left and right children
        printSubTree(t, left_child, depth + 1, 'left')
        printSubTree(t, right_child, depth + 1, 'right')
        # print(right_child)
    # Start with the root node
    printSubTree(t, 0, 0, 'root')

printTree('11000')