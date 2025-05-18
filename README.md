# Priority Queue Implementation using BST and MaxHeap

This project implements a **Priority Queue** by combining two fundamental data structures: a **Binary Search Tree (BST)** and a **Max Heap**. Each request (or task) is stored with an **ID**, **Name**, and **Priority**. The system allows users to insert, delete, search, and process requests efficiently while maintaining two synchronized views of the data.

## 📁 Files

- `Bst.py` – Implements a Binary Search Tree for storing and searching tasks by **Name** and **ID**.
- `Maxheap.py` – Implements a Max Heap to manage tasks based on **Priority**.
- `PriorityQueue.py` – Synchronizes operations between the BST and Max Heap.
- `Menu.py` – Provides a CLI menu interface to interact with the system and perform available operations.


## 🧠 How it Works

Each request has:
- `ID` (unique identifier)
- `Name` (description or name of the task/request)
- `Priority` (a numeric value representing urgency or importance)

### Data Structures Used:
- **BST**: Efficiently stores and searches by **Name** and **ID**.
- **Max Heap**: Efficiently retrieves and updates requests based on **Priority**.

The two structures are kept synchronized to ensure that every request is consistently represented in both data structures.

## ✅ Features

You can perform the following operations through the menu:

- 🔍 **Search** for a request by ID or Name  
- ➕ **Insert** a new task with Name, ID, and Priority  
- ❌ **Delete** a request by ID  
- 📋 **Display** all tasks in BST or Heap format  
- ⚙️ **Process** the request with the highest priority  
- ⬆️ **Increase** the priority of an existing task  
- 🌳 **Traverse** the BST in preorder  
- 📈 **Visualize** the trees using Graphviz

## 🖥️ Usage

Run the program using:

```bash
python Menu.py
```

Follow the interactive menu to perform operations on the priority queue.

## 📦 Requirements

- Python 3.x
- `graphviz` (optional, for tree visualization)

Install Graphviz via pip if needed:

```bash
pip install graphviz
```

To generate images, Graphviz software must be installed on your system (e.g., `brew install graphviz` or from https://graphviz.org/).

## 🧪 Example Use Cases

- Add new tasks with different priority levels
- Process high-priority tasks first
- View task structure visually
- Adjust priorities dynamically

## 📌 Notes

- Ensure unique IDs for each task.
- All operations maintain consistency between BST and MaxHeap.
- Visualization files are converted to images using Graphviz tools.

## 🧑‍💻 Author

This project was developed as part of the Algorithm Design course for a better understanding of data structures and priority-based scheduling.
