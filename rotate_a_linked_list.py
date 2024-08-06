class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self, current):
        # current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


    def reverse(self, curr):
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev

    def get_mid_node(self):
        fast = self.head
        slow = self.head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        if fast.next:
            slow = slow.next
        return slow
    

    def rotate_the_list(self, mid_point):
        left_curr = self.head
        right_curr = mid_point

        while right_curr.next:
            temp_left = left_curr.next
            temp_right = right_curr.next

            left_curr.next = right_curr
            right_curr.next = temp_left

            left_curr = temp_left
            right_curr = temp_right

        # Set the last node of the right side to None
        right_curr.next = None

        print("Rotated Linked List:")
        self.display(self.head)
        
    

# Example usage:
if __name__ == "__main__":
    linked_list = LinkedList()

    # Append elements to the linked list
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    # linked_list.append(5)
    # linked_list.append(6)
    # linked_list.append(7)

    mid_node = linked_list.get_mid_node()
    
    print(f"mid node: {mid_node.data}")
    reverse_head = linked_list.reverse(mid_node)

    print(f"Reversed head: {reverse_head.data}")


    print(f"Right Linked nodes")
    linked_list.display(reverse_head)
    
    print(f"Left Linked nodes")
    linked_list.display(linked_list.head)

    linked_list.rotate_the_list(mid_point=reverse_head)


