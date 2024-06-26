from .Operations.build_bst import build_bst
from .Operations.in_order import in_order_traversal
from .Operations.pre_order import pre_order_traversal
from .Operations.post_order import post_order_traversal
from .Operations.remove import remove
from .Operations.deleteall import delete
from .Operations.rebalance import rebalance
from .Operations.minmax import find_min, find_max
from .Operations.export import export
import re

def main_func_bst():
    root = None

    print("BST Tree Selected\nWaiting for input...\n> ", end='')
    tab = input()
    
    numbers = [int(x) for x in re.split(r'[\s,]+', tab)]
    root = build_bst(numbers)
    
    while True:
        print("Enter number of your choice: | 1. Print | 2. Remove | 3. Delte | 4. Export | 5. Rebalance | 6. Find min & max | 7. Exit |\n> ", end='')
        choice = input()

        if choice == "1" or choice == "1.":
                print("Option Print selected")
                    
                print("\nIn-order traversal: ", end='')
                in_order_traversal(root)
                print("\nPre-order traversal: ", end='')
                pre_order_traversal(root)
                print("\nPost-order traversal: ", end='')
                post_order_traversal(root)

                print("\n")

        elif choice == "2" or choice == "2.":
            print("Option Remove selected\nWaiting for input...\n> ", end='')
            tab = input()

            elements = [int(x) for x in re.split(r'[\s,]+', tab) if x]
            root = remove(root, elements)

        elif choice == "3" or choice == "3.":
            print("Option Delete selected")
            root = delete(root)

        elif choice == "4" or choice == "4.":
            print("Option Export selected")
            print(export(root))

        elif choice == "5" or choice == "5.":
            print("Option Rebalance selected")
            root = rebalance(root)

        elif choice == "6" or choice == "6.":
            print("Option min & max selected")
            print("Minimum value: ", find_min(root))
            print("Maximum value: ", find_max(root))
        
        elif choice == "7" or choice == "7.":
            print("Option Exit selected", end='')
            return False
        
        elif choice == "66" or choice == "66.":
            print("Execute order 66!\nComing soon...")

        else:
            print("Invalid choice")