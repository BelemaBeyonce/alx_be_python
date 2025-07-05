def display_menu():
    print("Shopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"{item} has been added to.")

        elif choice == "2":
            remove_item = input("Enter the item to remove from list: ")
            if remove_item in shopping_list:
                shopping_list.remove(remove_item)
                print(f"{remove_item} has been removed from the list.")
            else:
                print(f"{remove_item} is not in the list.")
        
        elif choice == "3":
            if shopping_list:
                print("Shopping List:")
                for item in shopping_list:
                    print(f"- {item}")
            else:
                print("Your shopping list is empty.")

        elif choice == "4":
            print("Exiting the Shopping List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")  

if __name__ == "__main__":
    main()

