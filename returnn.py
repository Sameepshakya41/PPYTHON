import datetime

def return_leased_land(land_list, land_id, customer, filename='return_receipts.txt'):
    """
    Returns a rented land and also updates
    """
    # Iterating over the land list
    for land in land_list:
        # Check to see if the land is rented
        if land['id'] == land_id and land['availability'] == 'Not Available':
            # Updating the lands availability to 'Available'
            land['availability'] = 'Available'
            # Acquire the current date and time
            return_date = datetime.datetime.now()
            # Open in append mode
            with open(filename, 'a') as file:
                # Write the return receipt to the file
                file.write(f"Land ID: {land['id']}\n")
                file.write(f"Location: {land['location']}\n")
                file.write(f"Facing: {land['facing']}\n")
                file.write(f"Size: {land['size']} annas\n")
                file.write(f"Customer: {customer}\n")
                file.write(f"Return Date: {return_date}\n")
                file.write(f"{'-'*40}\n")
                # print the cussess message
            print(f"Land returned successfully! Receipt appended to {filename}")
            # return form the function
            return
        # If the land is not found or it is not rented, print an error message
    print("Land not leased or invalid land ID!")
