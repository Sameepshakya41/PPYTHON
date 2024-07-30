"""
This is a module for reading, writing , and displaying land data
"""
def read_land_data(filename):
    """
    It reads land data from a file and also returns a list of land dictionaries
    """

# Initialize an empty list to store the land data
    land_list = []

    # Opening the file in read mode
    with open(filename, 'r') as file:
        # each line in the file is iterated
        for line in file:
            #removing the leading/trailing whitespace and split the line
            data = line.strip().split(', ')

            # creating a land dictionary
            land = {
                'id': data[0],
                'location': data[1],
                'facing': data[2],
                'size': data[3],
                'cost': int(data[4]),
                'availability': data[5]
            }

            # Adding the land dictionary to the list
            land_list.append(land)

            # Returning the list of the land dictionaries
    return land_list

def write_land_data(filename, land_list):
    """
    Writes the land data to the file
    """
    # Opening the file in write mode
    with open(filename, 'w') as file:
        # Iterating through the land list
        for land in land_list:
            # Writing the land data to the file
            line = f"{land['id']}, {land['location']}, {land['facing']}, {land['size']}, {land['cost']}, {land['availability']}\n"
            
            # Write the string to the file
            file.write(line)

def show_land_list(land_list):
    """
    Displays the list of land dictionaries
    """

    # Iterating over each land dictionary on the list
    for land in land_list:
        # Printing the land data
        print(f"ID: {land['id']}, Location: {land['location']}, Facing: {land['facing']}, Size: {land['size']} annas, Cost: {land['cost']} NPR, Availability: {land['availability']}")
