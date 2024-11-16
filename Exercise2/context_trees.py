MAXINTERNALNODES = 10
MAXTOTALNODES = 2 * MAXINTERNALNODES + 1

def findLeftChild(t: str, i: int) -> int:
    # Reverse t to process bits from the least significant bit at the end of the sequence
    t_reversed = t[::-1]
    if i < 0 or i >= len(t_reversed):
        return -1  # No left child
    if t_reversed[i] == '0':
        return -1  
    left_child = i + 1
    if left_child >= len(t_reversed):
        return -1  # No left child
    return left_child # Output position, looking at the reversed sequence (pos 0 is the least significant bit)

def findRightChild(t: str, i: int) -> int:
    t_reversed = t[::-1] # Reverse t
    if i < 0 or i >= len(t_reversed):
        return -1  # No right child
    if t_reversed[i] == '0':
        return -1  
    count = 1
    rightchild_pos = i + 1
    while count != 0:
        if rightchild_pos >= len(t_reversed):
            return -1  # No right child
        if t_reversed[rightchild_pos] == '1':
            count += 1
        else:
            count -= 1
        rightchild_pos += 1
    if rightchild_pos >= len(t_reversed):
        return -1  # No right child
    return rightchild_pos  # Position of the right child


t = '00000011111'
print("Find position of left child of 00000011111 at index 0: ", findLeftChild(t, 0)) 
print("Find position of right child of 00000011111 at index 0: ",  findRightChild(t, 0)) 

t = '000110011'
print("Find position of left child of 000110011 at index 0: ", findLeftChild(t, 0)) 
print("Find position of right child of 000110011 at index 0: ", findRightChild(t, 0)) 
print("Find position of right child of 000110011 at index 1: ", findRightChild(t, 1))
print("Find position of right child of 000110011 at index 4: ", findRightChild(t, 4))
print("Find position of right child of 000110011 at index 5: ", findRightChild(t, 5))



def printSubTree(t: str, i: int, depth: int, child_type: str):
    if i == -1 or i >= len(t):
        return
    
    # Assign label based on the type of child ( left is 'a' and right is 'b')
    if child_type == 'root':
        label = 'r'
    elif child_type == 'left':
        label = 'a'
    elif child_type == 'right':
        label = 'b'

    print('  ' * depth + label)
    left_child = findLeftChild(t, i)
    right_child = findRightChild(t, i)

    printSubTree(t, left_child, depth + 1, 'left')
    printSubTree(t, right_child, depth + 1, 'right')
        
def printTree(t: str):
    # Start with the root node at index 0
    printSubTree(t, 0, 0, 'root')

print("Printing tree 00011")
printTree('00011')
print("Printing tree 0000111")
printTree('0000111')
print("Printing tree 0010101")
printTree('0010101')

def isValidTree(t: int) -> bool:
    t_bin_original = bin(t)[2:]
    max_zeros_to_add = MAXINTERNALNODES

    # Reverse the original binary sequence
    t_bin_reversed = t_bin_original[::-1]

    # Try adding zeros at the end of t_bin_reversed, up to MAXINTERNALNODES times, check if it is a valid tree (C already has all the zeros)
    for zeros_to_add in range(max_zeros_to_add + 1):
        t_bin_reversed_padded = t_bin_reversed + '0' * zeros_to_add

        # If it exceeds the maximum number of total nodes, no valid tree can be formed
        if len(t_bin_reversed_padded) > MAXTOTALNODES:
            return False  

        internal_nodes = 0
        leaves = 0

        def check_tree(i):
            nonlocal internal_nodes, leaves
            if i >= len(t_bin_reversed_padded):
                return i  # Reached the end of the bit sequence
            if t_bin_reversed_padded[i] == '1':
                internal_nodes += 1
                if internal_nodes > MAXINTERNALNODES:
                    return -1  # Exceeds maximum internal nodes
                left_end = check_tree(i + 1)
                if left_end == -1:
                    return -1  # Invalid left subtree
                right_end = check_tree(left_end)
                if right_end == -1:
                    return -1  # Invalid right subtree
                return right_end
            elif t_bin_reversed_padded[i] == '0':
                leaves += 1
                return i + 1

        # Start from index 0
        end_index = check_tree(0)
        if end_index == -1:
            # Checking tree failed, add another zero and continue
            continue

        leaves_needed = internal_nodes + 1
        if leaves != leaves_needed:
            # Invalid number of leaves, try adding another zero (L = I + 1)
            continue

        # Check if all remaining bits after the tree representation are zeros, otherwise continue (while then there are still internal nodes to add)
        if any(bit != '0' for bit in t_bin_reversed_padded[end_index:]):
            continue
        
        # If we pass all checks we have a valid tree and we print it
        valid_tree = t_bin_reversed_padded[::-1]
        print(f"Valid tree found with sequence: {valid_tree}")
        printTree(valid_tree)
        return True

    # No valid tree found after adding the max number of zeros
    return False

numbers = [31, 51, 341, 1829, 4903]

for t in numbers:
    print(f"Test canonical representation for tree = {t}")
    print(isValidTree(t))