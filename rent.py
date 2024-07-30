import datetime

def lease_land(land_list, land_id, customer, duration):
    """
    Rents a land to the customer and also generates a receipt
    """
    for land in land_list:
        """
        Checking if the land ID matches and also if the land is available or not
        """
        if land['id'] == land_id and land['availability'] == 'Available':
            land['availability'] = 'Not Available'
            lease_date = datetime.datetime.now()
            total_cost = land['cost'] * duration
            receipt = f"Lease_{land_id}_{customer}_{lease_date.strftime('%Y%m%d%H%M%S')}.txt"
            with open(receipt, 'w') as file:
                """
                Write the rent details to the receipt file.
                """
                file.write(f"Land ID: {land['id']}\n")
                file.write(f"Location: {land['location']}\n")
                file.write(f"Facing: {land['facing']}\n")
                file.write(f"Size: {land['size']} annas\n")
                file.write(f"Customer: {customer}\n")
                file.write(f"Lease Date: {lease_date}\n")
                file.write(f"Duration: {duration} months\n")
                file.write(f"Total Cost: {total_cost} NPR\n")
                # Print the success message
            print(f"Land leased successfully! Receipt generated: {receipt}")
            # Return to exit the function
            return
        # Print the error message if the land is not available
    print("Land not available or invalid land ID!")
