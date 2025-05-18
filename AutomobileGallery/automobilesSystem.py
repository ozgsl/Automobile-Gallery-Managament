import os

# Function to load car records from a file
def load_automobiles(file_path):
    automobiles = [] # Initialize an empty list to store load results
    if os.path.exists(file_path):
        # Open file
        with open(file_path, 'r') as file: # Meaning of r is read mode
            for line in file:
                line = line.strip() # Remove extra spaces and new line chars
                
                if line.strip(): # If it's empty, skip the line
                    try:
                        make, model, year, price, fuel_type, mileage = line.strip().split(',')
                        
                        # Add the car information to the list
                        automobiles.append({
                            'Make': make,
                            'Model': model,
                            'Year': int(year),
                            'Price': float(price),
                            'Fuel Type': fuel_type,
                            'Mileage': int(mileage)
                        })
                    except ValueError: # If the line has an error, handle it
                        print(f"Skipping invalid record: {line}") # Skip the incorrect line
    # Return the car records
    return automobiles

# Save automobile records to the file
def save_automobiles(file_path, automobiles):
    if not automobiles: # Check if the list of automobiles is empty
        print("There is no data to save.")
        return
    # TRY-CATCH structure
    try:
        # Open the file
        with open(file_path, 'w') as file: # Meaning of w is write mode to save data
            for automobile in automobiles:
                # Create a formatted record string in CSV format
                record = f"{automobile['Make']},{automobile['Model']},{automobile['Year']},{automobile['Price']},{automobile['Fuel Type']},{automobile['Mileage']}\n"
                file.write(record) 
        print(f"Data saved successfully!")
    
    except FileNotFoundError: # Handle the case where the file path is invalid
        print("Error: File not found.")
   
    except Exception as e: # Handle any other errors during saving
        print(f"Error while saving data: {e}")

# Add a new automobile record
def add_automobile(automobiles):
    try:
        # Prompt the user to enter car details and remove any extra spaces
        make = input("Enter Make: ").strip()
        model = input("Enter Model: ").strip()
        year = int(input("Enter Year: ")) # Convert to integer type
        price = float(input("Enter Price (TRY): ")) # Convert to float type
        fuel_type = input("Enter Fuel Type (Petrol/Diesel/Electric): ").strip()
        mileage = int(input("Enter Mileage (km): ")) # Convert to integer type

        # Add the new car details to the list
        automobiles.append({
            'Make': make,
            'Model': model,
            'Year': year,
            'Price': price,
            'Fuel Type': fuel_type,
            'Mileage': mileage
        })
        print("Automobile added successfully!")
    
    except ValueError: # Handle errors when invalid input is provided
        print("Error: Invalid input.")

# List all automobile records
def list_automobiles(automobiles): # Check if the list is empty
    if not automobiles:
        print("No automobiles in the system.") # If there are no records, print the information.
    else:
        print("\nAutomobile List:") # Print list of header
        print("****************")
        # Loop through each automobile and display its details with an index
        for idx, automobile in enumerate(automobiles, start=1):
            print(f"{idx}. {automobile['Make']} {automobile['Model']} ({automobile['Year']}) - "
                  f"{automobile['Price']} TRY - {automobile['Fuel Type']} - {automobile['Mileage']} km")

# Update an existing record
def update_automobile(automobiles):
    list_automobiles(automobiles) # Call function to show users all cars
    try:
        # Ask users to select the car to update
        index = int(input("Enter the number of the automobile to update: ")) - 1
        
        if 0 <= index < len(automobiles): # Check if the selected number is valid
            automobile = automobiles[index]
            print("Leave fields blank to keep current values. (for leave blank please click on Enter)")

            # Update each field or keep it the same
            automobile['Make'] = input(f"Enter Make ({automobile['Make']}): ") or automobile['Make']
            automobile['Model'] = input(f"Enter Model ({automobile['Model']}): ") or automobile['Model']
            automobile['Year'] = int(input(f"Enter Year ({automobile['Year']}): ") or automobile['Year'])
            automobile['Price'] = float(input(f"Enter Price ({automobile['Price']}): ") or automobile['Price'])
            automobile['Fuel Type'] = input(f"Enter Fuel Type ({automobile['Fuel Type']}): ") or automobile['Fuel Type']
            automobile['Mileage'] = int(input(f"Enter Mileage ({automobile['Mileage']}): ") or automobile['Mileage'])
            print("Automobile updated successfully!")
        else:
            print("Error: Invalid selection.") # If the number is invalid, print the information
    
    except ValueError: # Handle errors when invalid input is provided
        print("Error: Invalid input.")

# Remove an automobile record
def remove_automobile(automobiles):
    list_automobiles(automobiles) # Call function to show users all cars as before
    try:
        # Ask the user to select the automobile to remove 
        index = int(input("Enter the number of the automobile to remove: ")) - 1
        if 0 <= index < len(automobiles):
            removed = automobiles.pop(index) # Remove the selected automobile from the list
            print(f"Removed automobile: {removed['Make']} {removed['Model']}")
        else:
            print("Error: Invalid selection.") # Print the error to user
    
    except ValueError: # Handle cases where the input is not a valid integer
        print("Error: Invalid input.")

# Search for automobiles
def search_automobiles(automobiles):
    # Print search options
    print("Search by: 1. Make  2. Model  3. Year Range  4. Price Range  5. Fuel Type")
    try:
        # Ask the user to select a search option
        choice = int(input("Enter your choice: "))
        results = [] # Initialize an empty list to store search results
        # Use if-elif structure and search by chosen integer numbers
        if choice == 1:
            make = input("Enter Make to search: ").strip()
            results = [a for a in automobiles if a['Make'].lower() == make.lower()] 
        elif choice == 2:                                # lower function is more flexible for interface
            model = input("Enter Model to search: ").strip()
            results = [a for a in automobiles if a['Model'].lower() == model.lower()]
        elif choice == 3:
            start_year = int(input("Enter start year: "))
            end_year = int(input("Enter end year: "))
            results = [a for a in automobiles if start_year <= a['Year'] <= end_year]
        elif choice == 4:
            min_price = float(input("Enter minimum price: "))
            max_price = float(input("Enter maximum price: "))
            results = [a for a in automobiles if min_price <= a['Price'] <= max_price]
        elif choice == 5:
            fuel_type = input("Enter Fuel Type to search: ").strip()
            results = [a for a in automobiles if a['Fuel Type'].lower() == fuel_type.lower()]
        else:
            print("Error: Invalid choice.") # Handle invalid search choice
            return

        if results:
            print("\nSearch Results:") # List of header
            print("****************")
            for automobile in results: # If results matched, print to users
                print(f"{automobile['Make']} {automobile['Model']} ({automobile['Year']}) - "
                      f"{automobile['Price']} TRY - {automobile['Fuel Type']} - {automobile['Mileage']} km")
        else:
            print("There is no matching automobiles found.")
    
    except ValueError: # Handle cases where the input is not valid
        print("Error: Please try again.")


# Main function
def main():
    file_path = 'automobiles.txt' # Define the file path for storing automobile data
    automobiles = load_automobiles(file_path) # Load existing automobile records from the file

    while True:
        # Print the menu options to users
        print("\nAutomobile Gallery Management")
        print("1. Add Automobile")
        print("2. Update Automobile")
        print("3. Remove Automobile")
        print("4. List Automobiles")
        print("5. Search Automobiles")
        print("6. Exit")
        try: # Ask the user to select a menu option, all options functions are here
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_automobile(automobiles)
            elif choice == 2:
                update_automobile(automobiles)
            elif choice == 3:
                remove_automobile(automobiles)
            elif choice == 4:
                list_automobiles(automobiles)
            elif choice == 5:
                search_automobiles(automobiles)
            elif choice == 6:
                save_automobiles(file_path, automobiles)
                print("Changes saved.\n")
                print("Exiting...Have a good day! ")
                break
            else:
                print("Error: Please select from the menu.") # Handle invalid menu choice
        except ValueError: # Handle cases where the input is not valid
            print("Error: Please enter a valid number.")

if __name__ == "__main__":
    main() # Start the program by calling the main
