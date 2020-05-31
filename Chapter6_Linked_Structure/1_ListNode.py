class ListNode(object):
	def __init__(self,data):
		self.data = data
		self.next = None

def traverse(head):
	current_node = head
	while current_node != None:
		print(current_node.data)
		current_node = current_node.next

def unsorted_search(head, target):
	current_node = head
	while current_node != None and current_node.data != target:
		current_node = current_node.next
	return current_node != None
	
def remove(head, target):
	pred_node = None
	current_node = head
	
	while current_node != None and current_node.data != 	target:
		pred_node = current_node
		current_node = current_node.next
		
	if current_node != None:
		if current_node == head:
			head = current_node.next
		else:
			pred_node.next = current_node.next
	return head
		
	
def main():
	node1 = ListNode(1)
	node2 = ListNode(12)
	node3 = ListNode(144)
	node4 = ListNode(123)
	node5 = ListNode(5)
	
	node1.next = node2
	node2.next = node3
	node3.next = node4
	node4.next = node5
	
	node2 = None
	node3 = None
	node4 = None
	node5 = None
	
	print("the linked list: ")
	traverse(node1)
	
	print()
	
	print("search 2,1 and 5: ")
	print(unsorted_search(node1, 2))
	print(unsorted_search(node1, 1))
	print(unsorted_search(node1, 5))
	
	print()
	
	print("remove 1")
	node1 = remove(node1, 1)
	traverse(node1)
	
	print()
	
	print("remove 144")
	node1 = remove(node1, 144)
	traverse(node1)
	
	
	
if __name__ == "__main__":
	main()