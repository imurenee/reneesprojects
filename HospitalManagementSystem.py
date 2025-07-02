

# Initialize empty lists to store data
patient_data = []
room_data = []
physician_data = []
transaction_data = []

# Function of Patient Management
def patient_management():
    while True:
        print()
        print(" 1. Add patient.")
        print(" 2. Update patient info.")
        print(" 3. Display patient info.")
        print(" 4. Delete patient.")
        print(" 5. Exit.")
        print()

        choice= input(" Enter your choice: ")
        print()

        if choice=='1':
            add_patient_info()
        elif choice=='2':
            update_info()
        elif choice=='3':
            display_patient_data()
        elif choice=="4":
            delete_patient()
        elif choice=="5":
            print('You have successfully exited the patient management system.')
            break
        else:
            print("Invalid option.")

# Function to add patient information
def add_patient_info():
    # Input patient details
    patient_ic = input("Enter patient IC: ")
    patient_name = input("Enter patient name: ")
    formatted_name = patient_name.title()
    patient_age = int(input("Enter patient age: "))
    patient_contact = input("Enter patient contact: ")
    room_number = input("Enter patient room number: ")
    patient_status = input("Enter patient status: ")

    # Append patient information to the patient_data list
    patient_data.append({
        "IC": patient_ic,
        "Name": formatted_name,
        "Age": patient_age,
        "Contact": patient_contact,
        "Room Number": room_number,
        "Status": patient_status
    })

    print("Patient data added successfully.")

# Function to display patient information
def display_patient_data():
    if not patient_data:
        print("This is an empty list.")
    else:
        print("List of patient data: ")
        for patient in patient_data:
            print(f"IC:{patient['IC']}, Name: {patient['Name']}, Age: {patient['Age']}, "
                  f"Contact: {patient['Contact']}, Room Number:{patient['Room Number']}, Status: {patient['Status']}")

# Function to update patient information
def update_info():
    index = int(input("Enter position: "))

    # Check if the index is valid
    if 1 <= index <= len(patient_data):
        patient = patient_data[index - 1]

        print('Edit Menu')
        print("1. Edit Name")
        print("2. Edit IC")
        print("3. Edit Age")
        print("4. Edit Contact")
        print("5. Edit Room Number")
        print("6. Edit Patient Status")
        print()

        # Get user's input
        choice = input("Enter your choice: ")

        if choice == '1':
            edited_name = input("Enter edited Name: ")
            patient["Name"] = edited_name.title()
        elif choice == '2':
            patient["IC"] = input("Enter edited IC: ")
        elif choice == '3':
            patient["Age"] = int(input("Enter edited Age: "))
        elif choice == '4':
            patient["Contact"] = input("Enter edited Contact: ")
        elif choice == '5':
            patient["Room Number"] = input("Enter edited Room Number: ")
        elif choice == '6':
            patient["Status"] = input("Enter edited Patient Status: ")
        else:
            print("Invalid choice")
            return

        print("Patient data updated successfully.")
    else:
        print('Invalid position.')

# Function to delete patient information
def delete_patient():
    index = int(input("Enter position: "))

    # Check if the index is valid
    if 1 <= index <= len(patient_data):
        # Remove patient information
        removed_patient = patient_data.pop(index - 1)
        print("Patient's data removed successfully.")
    else:
        print('Invalid position.')

# Function of Room Management
def room_management():
    while True:
        print()
        print(" 1. Add room info.")
        print(" 2. Update room status.")
        print(" 3. Display room info.")
        print(" 4. Delete room.")
        print(" 5. Exit.")
        print()

        choice= input(" Enter your choice: ")
        print()
        if choice=='1':
            add_room_info()
        elif choice=='2':
            update_room_status()
        elif choice=='3':
            display_room_data()
        elif choice=="4":
            delete_room()
        elif choice=="5":
            print('You have successfully exited the room management system.')
            break
        else:
            print("Invalid option.")

# Function to add room information
def add_room_info():
    # Input room details
    room_number = input("Enter room number: ")
    room_type = input("Enter room type: ")
    room_status = input("Enter room status: ")

    # Append room information to the room_data list
    room_data.append({"Room Number": room_number, "Type": room_type, "Status": room_status})
    print("Room data added successfully.")

# Function to update room status
def update_room_status():
    removed_room = input("Enter room number needed to update: ")

    for room in room_data:
        if room['Room Number'] == removed_room:
            room['Status'] = input("Enter new room status: ")
            print("Room data updated successfully.")
            return

    print('No result found.')

# Function to display room information
def display_room_data():
    if not room_data:
        print("This is an empty list.")
    else:
        print("List of room data: ")
        for room in room_data:
            print(f"Room Number:{room['Room Number']}, Type: {room['Type']}, Status: {room['Status']}")

# Function to delete room information
def delete_room():
    index = int(input("Enter position: "))

# Check if the index is valid
    if 1 <= index <= len(room_data):
# Remove room information
        removed_room = room_data.pop(index - 1)
        print("Room data removed successfully.")
    else:
        print('Invalid position.')

#A function for physician management
def physician_management():
    while True:
        print("\nPhysician Management")
        print("1. Add physician\n2. Update physician status\n3. Delete physician\n4. Exit")

#The user can input what they want to do with the physician info
        choice = input("Enter your choice: ")

        if choice == '1':
            add_physician(physician_data)
        elif choice == '2':
            manage_physician_status(physician_data)
        elif choice == '3':
            delete_physician(physician_data)
        elif choice == '4':
            print('Exiting Physician Management System.')
            break
        else:
            print("Invalid option.")

# Adds a physician to the list of physicians
def add_physician(physician_data):
# User can add physician name
    name = input("Enter physician's name: ")
# User can add physician specialization
    specialization = input("Enter physician's specialization: ")
# User can input physician ID
    physician_id = input("Enter your physician ID: ")

# A dictionary is created that stores the physician ID, name, and specializations as keys
    physician = {'id': physician_id, 'name': name, 'specialization': specialization}
# Appends the physician data to the physician list
    physician_data.append(physician)
# Prints the output
    print("Physician", name, "added with ID:", physician_id)

# Update the status of physicians
def manage_physician_status(physician_data):
# Checks if there are any physicians in the system
    if not physician_data:
# Output if no physicians
        print("No physicians in the system.")
# Used to exit the function
        return

# User input for physician ID
    physician_id = input("Enter physician ID: ")

# Check if the entered physician_id is within the valid range of IDs in physician_data
    matching_physicians = [physician for physician in physician_data if physician['id'] == physician_id]

    if matching_physicians:
# Assume there is only one physician with the given ID
        selected_physician = matching_physicians[0]

# Ask the user to enter the updated information
        edited_name = input("Enter edited name: ")
        edited_id = input("Enter edited ID: ")
        edited_specialization = input("Enter edited specialization: ")
# Update the keys in the physician dictionary with the specified edit
        selected_physician['name'] = edited_name
        selected_physician['id'] = edited_id
        selected_physician['specialization'] = edited_specialization
# Print a message indicating that the physician's information has been updated
        print("Physician", selected_physician['name'], "with ID", selected_physician['id'], "information updated.")

    else:
# Print a message indicating that the entered physician ID is invalid
        print("Invalid physician ID.")

def delete_physician(physician_data):
    removed_physician_id = input("Enter the physician ID you want to remove: ")

# Check if the entered physician ID exists in the physician_data list
    matching_physicians = [physician for physician in physician_data if physician['id'] == removed_physician_id]

    if matching_physicians:
# Assuming there is only one physician with the given ID
        removed_physician = matching_physicians[0]
        # Remove the physician from the physician_data list
        physician_data.remove(removed_physician)
        print("Physician", removed_physician['name'], "with ID", removed_physician_id, "removed successfully.")

    else:
        print("Physician ID not found. No physician removed.")

def transaction_management():
    while True:
        print("\nTransaction Management")
        print("1. Add transaction.\n2. Update transaction.\n3. Delete transaction.\n4. Exit.")

        choice = input("Enter your choice: ")

        if choice == '1':
          add_transaction(patient_data, transaction_data)
        elif choice == '2':
          update_transaction(transaction_data)
        elif choice == '3':
          delete_transaction(transaction_data)
        elif choice == '4':
          print('Exiting Transaction Management System.')
          break
        else:
            print("Invalid option.")

# Adds the transaction records
def add_transaction(patient_data, transaction_data):
# Check if there are patients in the system
    if not patient_data:
        print("No patients in the system. Please add patients first.")
        return

# User input for patient IC
    patient_ic = input("Enter patient IC: ")
# Check if the entered patient IC exists in the patient_data list
    matching_patients = [patient for patient in patient_data if patient['IC'] == patient_ic]

    if matching_patients:
# The patient with the specified IC was found
        patient = matching_patients[0]  # Assuming there's only one matching patient
    else:
# The patient with the specified IC was not found
        print("Patient with IC", patient_ic, "not found.")
        return

# User input for transaction ID
    transaction_id = input("Enter transaction ID: ")

# Check if the transaction ID already exists
    if any(transaction['id'] == transaction_id for transaction in transaction_data):
        print("Transaction ID already exists. Please choose a unique ID.")
        return

# User input for transaction amount
    amount = float(input("Enter transaction amount: "))

# Create a transaction dictionary with patient data and transaction amount
    transaction = {'id': transaction_id, 'patient': patient, 'amount': amount}

# Append the transaction data to the transaction list
    transaction_data.append(transaction)

# Print a message indicating that the transaction record has been added
    print("Transaction", transaction_id, "added successfully.")


def update_transaction(transaction_data):
# Check if there are transactions in the system
    if not transaction_data:
        print("No transactions in the system.")
        return

# User input for transaction id
    transaction_id = input("Enter transaction id: ")
# Check if the entered transaction_id is within the valid range of IDs
    matching_transactions = [transaction for transaction in transaction_data if transaction['id'] == transaction_id]

    if matching_transactions:
# Assume there is only one transaction with the given ID
        selected_transaction = matching_transactions[0]
# User input for updated transaction amount
        updated_amount = float(input("Enter updated transaction amount: "))
# Update the 'amount' key in the transaction dictionary with the specified id
        selected_transaction['amount'] = updated_amount
# Print a message indicating that the transaction record has been updated
        print("Transaction ID", transaction_id, "updated.")

    else:
# Print a message indicating that the entered transaction id is invalid
        print("Invalid transaction id.")

def delete_transaction(transaction_data):
    removed_transaction = input("Enter the transaction ID you want to remove: ")

# Check if the entered transaction ID exists in the transaction_data list
    matching_transactions = [transaction for transaction in transaction_data if transaction['id'] == removed_transaction]

    if matching_transactions:
# Assuming there is only one transaction with the given ID
        removed_transaction = matching_transactions[0]
# Remove the transaction from the transaction_data list
        transaction_data.remove(removed_transaction)
        print("Transaction ID", removed_transaction['id'], "removed successfully.")

    else:
        print("Transaction ID not found. No transaction removed.")

# Main function to run the hospital management system
def main():
    while True:
        print()
        print("Hospital Management System")
        print(" 1. Patient Management.")
        print(" 2. Room Management.")
        print(" 3. Physician Management.")
        print(" 4. Transaction Management.")
        print(" Q. Quit the program.")
        print()

# Get user's choice
        choice = input(" Enter your choice (1-Q):")

        if choice == '1':
           patient_management()
        elif choice == '2':
            room_management()
        elif choice == '3':
            physician_management()
        elif choice == '4':
            transaction_management()
        elif choice.upper() == 'Q':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and Q.")

main()