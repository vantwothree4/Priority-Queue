from PriorityQueue import PriorityQueue

queue = PriorityQueue()

def selectOption():
    menuItems = '''how can I help you?\n
1) View all requests\n  
2) Insert request\n  
3) Increase priority\n  
4) Process request\n  
5) Search request\n
6) Delete request\n 
7) Print BST (Preorder)\n
8) Visualize tree\n
9)exit '''
    print(menuItems)
    while 1:
        choice = input("\nEnter your choice (1-9): ")
        if choice.isdigit() and 1 <= int(choice) <= 9:
            return int(choice)
        else:
            print("Invalid, try again.")

def getValue(mode):
    while 1:
        try:
            value = int(input(f"Enter {mode} (as a number): "))
            break
        except ValueError:
            print(f"\nInvalid input. Please enter a numeric value for {mode}.")
    return value
    
    
def viewRequests():
    if queue.BST.isEmpty():
        print("There are no requests in the queue.")
    else:
        print("Here are all the requests in the queue:\n")
        queue.showRequests()
        
def insertRequest():
    while 1:
        name = input("Enter request name: ")
        pid = getValue("request ID")
        priority = getValue("priority")
        queue.newRequest(pid, name, priority)
        print("\nRequest inserted.")
        exit = input("\npress [R] to return or press [Enter] to insert another request: ").lower()
        if exit == 'r':
            return


    
def increasePriority():
    while 1:
        pid = getValue("request ID")
        priority = getValue("priority")
        if queue.increasePriority(pid,priority):
            print(f"\npriority of request {pid} increased to {priority}.")
        else:
            print(f"\nRequest with ID {pid} was not found, or the new priority was less than the old priority.")
        exit = input("\nPress [R] to return or press [Enter] to increase the priority of another request: ").lower()
        if exit =='r':
            return

def processRequest():
    while 1:
        request = queue.process()
        if request:
            print(f"Processed request: {request.name}")
        else:
            print("No requests to process.")
        exit = input("\nPress [R] to return or press [Enter] to process another request: ").lower()
        if exit =='r':
            return

        


def searchRequest():
    while 1:
        pid = getValue("request ID")
        request = queue.searchRequestByID(pid)
        if request:
            print(f"\nRequest found: {request.name}")
        else:
            print("\nRequest with that ID was not found.")
        exit = input("\nPress [R] to return or press [Enter] to search for another request: ").lower() 
        if exit =='r':
            return

            
def deleteRequest():
    while 1:
        pid = getValue("request ID")
        request = queue.deleteRequestByID(pid)
        if request:
            print(f"\nRequest with ID {pid} deleted successfully.")
        else:
            print("\nRequest with that ID was not found.")
        exit = input("\nPress [R] to return or press [Enter] to delete another request: ").lower() 
        if exit =='r':
            return

def BSTPreorder():
    if queue.BST.isEmpty():
        print("The BST is empty.")
    else:
        print("BST Preorder Traversal:")
        queue.BST.printBST()  

def visualize():
    print("Which data structure do you want to visualize?\n1) BST \n2) Heap \n3) Both")

    while True:
        choice = input("\nEnter your choice (1-3): ")
        if choice == '1':
            queue.visualizeTrees('BST')
            break
        elif choice == '2':
            queue.visualizeTrees('heap')
            break
        elif choice == '3':
            queue.visualizeTrees()
            break
        else:
            print("\nInvalid input. Please enter 1, 2, or 3.")



while True:
    print()
    choice = selectOption()
    print()
    if choice == 1:
        viewRequests()
    elif choice == 2:
        insertRequest()
    elif choice == 3:
        increasePriority()
    elif choice == 4:
        processRequest()
    elif choice == 5:
        searchRequest()
    elif choice == 6:
        deleteRequest()
    elif choice == 7:
        BSTPreorder()
    elif choice == 8:
        visualize()
    else:
        print("Goodbye!")
        break
    input("\npress [Enter] to continue.")



        
    
   
    
