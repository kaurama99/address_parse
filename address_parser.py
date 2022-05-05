import re
# Using regEX to get only the values 
regex = re.compile("^(?P<unit_number>[0-9]{1,5}-)?(?P<street_number>[0-9]{2,4})_?(?P<street_name>[a-zA-Z]+_[a-zA-Z]+_?[a-zA-Z]+?)_(?P<city>[a-zA-Z]+)_(?P<state>[a-zA-Z]{2})_(?P<postal_code>[a-zA-Z0-9]{6})$")

def run(address_string):
    address_info = {}
    match = regex.match(address_string)
    if match:
        try:
            # Using a try catch for the unit number as the unit number may not always be included
            address_info["unit_number"] = match.group("unit_number").replace("-", "")
        except KeyError:
            print("No unit number")
            pass
        # The captured groups are named to identify them easily, these groups are then saved into the dictionary with corresponding key  
        address_info["street_number"] = match.group("street_number")
        # Replacing the underscore with whitespace
        address_info["street_name"] = match.group("street_name").replace("_", " ")
        address_info["city"] = match.group("city")
        address_info["state"] = match.group("state")
        address_info["postal_code"] = match.group("postal_code")
    
    # Prints Dictionary 
    print(address_info)

#Driver code
address = input("Enter Address")
run(address)