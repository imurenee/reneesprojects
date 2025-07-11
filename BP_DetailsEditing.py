

#Question 2
def main():
#An empty list to store all the blood pressure entered
    bloodpressure = []

#The menu in which the hospital admin can choose which action they want
    while True:
        print()
        print("1. Add a patient's blood pressure.")
        print("2. Remove a patient's pressure, given its position.")
        print("3. Remove a patient's pressure, given its value.")
        print("4. Display all blood pressure readings.")
        print("5. Display the sum and average of all blood pressure readings.")
        print("6. Display all blood pressure readings in ascending order.")
        print("7. Display all blood pressure readings which has a value more than 120.")
        print("8. Quit the program.")
        print()

#The user can enter the action they want
        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            repeat = 'yes'
            while repeat.lower() == 'yes':
#allow the user to enter blood pressure
                ques1 = input("Add a patient's blood pressure: ")
##to add every input in 'ques1' to list 'bloodpressure'
                bloodpressure.append(ques1)
                print("Here is the list of bloodpressure:", bloodpressure)
#ask if they want to add more, if yes, it will loop
                repeat = input("Do you want to add another blood pressure? (Yes/No): ").lower()

        elif choice == '2':
#'int' to make sure they only enter a whole number because decimals does not exist in positions
            position = int(input("Choose the position of blood pressure you want to remove: "))
#to check whether the provided position is valid, if it is a non-negative integer
            if 1 <= position < len(bloodpressure):
#if position is valid, this line deletes the patient name at the specified position
              del bloodpressure[position - 1]
              print("Here's the updated list:", bloodpressure)
            else:
#outcome if the position is invalid
              print("Invalid position. Blood pressure not found in the list.")

        elif choice == '3':
#The user input which name to remove
            removed = input("Choose the blood pressure you want to remove: ")
#checks if the name is inside the 'bloodpressure' list
            if removed in bloodpressure:
              bloodpressure.remove(removed)
              print("Here's the updated list:", bloodpressure)
#outcome if the name is not in the list
            else:
              print("Blood pressure not found in the list.")

        elif choice == '4':
#checks if the length of the bloodpressure is more than 0 in the list
            if len(bloodpressure) > 0:
              print("All patients' blood pressure:", bloodpressure)
            else:
#outcome if the list is empty
              print("There are no blood pressure to be found.")

        elif choice == '5':
#checks if there are readings, this ensures that calculations are performed only when there are readings
            if len(bloodpressure) > 0:
#converts all elements in the bloodpressure list to integers and assigns the result to the bloodpressureint list
              bloodpressureint = [int(bp) for bp in bloodpressure]
#calculates the sum of all blood pressure readings
              sumofbp = sum(bloodpressureint)
#calculates the average of all blood pressure readings by dividing the sum by the number of readings
              average = sumofbp / len(bloodpressureint)
              print("The sum of all the blood pressure is: ", sumofbp)
              print("The average of all blood pressure is: ", average)
            else:
#prints this message if there are no names in the list
              print("There are no blood pressure readings to calculate the sum and average.")

#This will sort the patient names into ascending order
        elif choice == '6':
            sortedbp = sorted(bloodpressure)
            print("The ascending order is:", sortedbp)

        elif choice == '7':
#creates a new list and converts all the blood pressure entered into integers and includes it in the new list only if its value is greater than 120
            exceeded = [int(bp) for bp in bloodpressure if int(bp) > 120]
            if exceeded:
                print("The blood pressure that exceeds the value 120 is: ", exceeded)
            else:
#If all the values are lesser then 120, this message will be printed
                print("There are no values that exceed 120.")

#The loop will break and terminates the program if the user chooses this
        elif choice == '8':
            print("Thank you for using the program!")
            break

main()

