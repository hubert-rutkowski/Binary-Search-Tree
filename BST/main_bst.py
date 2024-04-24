from Operations.build_bst import build_bst
from Operations.in_order import in_order_traversal
from Operations.pre_order import pre_order_traversal
from Operations.post_order import post_order_traversal

if __name__ == "__main__":
    print("Enter number of your choice: (1. Print, 2. Remove, 3. Delte, 4. Export, 5. Rebalance, 6. Exit)\n> ", end='')
    choice = input()

    if choice == "1" or choice == "1.":
        print("Option Print selected\nWaiting for input...\n> ", end='')
        tab = input()
        numbers = [int(x) for x in tab.split(",")]

        root = build_bst(numbers)

        print("\nPre-order traversal: ", end='')
        pre_order_traversal(root)
        print("\nIn-order traversal: ", end='')
        in_order_traversal(root)
        print("\nPost-order traversal: ", end='')
        post_order_traversal(root)

        print("\n")
        
    elif choice == "2" or choice == "2.":
        print("Option Remove selected")

    elif choice == "3" or choice == "3.":
        print("Option Delete selected")

    elif choice == "4" or choice == "4.":
        print("Option Export selected")

    elif choice == "5" or choice == "5.":
        print("Option Rebalance selected")

    elif choice == "6" or choice == "6.":
        print("Option Exit selected")

    else:
        print("Invalid choice")