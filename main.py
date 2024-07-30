# importing all the necessary modules
from operation import read_land_data, write_land_data, show_land_list
from rent import lease_land
from returnn import return_leased_land

"""
Main Function to manage the land data 
"""
def main():
    """
    It reads the land data from the file and also stores it in a list
    """
    land_list = read_land_data('land_records.txt')

    # To continuous it prompts user for input an infinite loop is created
    while True:
        #Displaying the menu options
        print("\n1. Show Land data")
        print("2. Rent Land")
        print("3. Return Land")
        print("4. Exit")

        # Getting users choice
        choice = input("Enter your choice: ")

        # Handling users choice
        if choice == '1':
            # Showing the land list
            show_land_list(land_list)
        elif choice == '2':
            """
            Renting the land to customer
            """
            land_id = input("Enter land ID: ")
            customer = input("Enter customer name: ")
            duration = int(input("Enter lease duration (months): "))

            # Rent land and update land list
            lease_land(land_list, land_id, customer, duration)
            write_land_data('land_records.txt', land_list)
        elif choice == '3':
            """
            Return rented land
            """
            land_id = input("Enter land ID: ")
            customer = input("Enter customer name: ")
            return_leased_land(land_list, land_id, customer)
            write_land_data('land_records.txt', land_list)
        elif choice == '4':
            # Exit the program
            break
        else:
            # Handling invalid choice
            print("Invalid choice! Please try again.")
"""
Entry point of the program
"""
if __name__ == "__main__":
    main()
