# Import necessary modules
import matplotlib.pyplot as plt
import sys

# Define a function to display the menu
def display_menu():
    print("Welcome to the Sitka Temperature Program!")
    print("Please select an option from the menu:")
    print("1. Highs: Display the high temperatures for the given dates.")
    print("2. Lows: Display the low temperatures for the given dates.")
    print("3. Exit: Exit the program.")

# Define a function to get the user's choice
def get_user_choice():
    while True:
        choice = input("Enter your choice (1, 2, or 3): ")
        if choice in ['1', '2', '3']:
            return choice
        else:
            print("Invalid choice. Please try again.")

# Define a function to display the high temperatures
def display_highs(highs, dates):
    plt.figure(figsize=(10, 6))
    plt.plot(dates, highs, c='red')
    plt.title('Daily High Temperatures')
    plt.xlabel('Date')
    plt.ylabel('Temperature (F)')
    plt.show()

# Define a function to display the low temperatures
def display_lows(lows, dates):
    plt.figure(figsize=(10, 6))
    plt.plot(dates, lows, c='blue')
    plt.title('Daily Low Temperatures')
    plt.xlabel('Date')
    plt.ylabel('Temperature (F)')
    plt.show()

# Define the main function
def main():
    # Define the high and low temperatures for the given dates
    highs = [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80]
    lows = [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]
    dates = ['Jan 1', 'Jan 2', 'Jan 3', 'Jan 4', 'Jan 5', 'Jan 6', 'Jan 7', 'Jan 8', 'Jan 9', 'Jan 10', 'Jan 11', 'Jan 12', 'Jan 13', 'Jan 14', 'Jan 15', 'Jan 16']

    while True:
        display_menu()
        choice = get_user_choice()
        if choice == '1':
            display_highs(highs, dates)
        elif choice == '2':
            display_lows(lows, dates)
        elif choice == '3':
            print("Thank you for using the Sitka Temperature Program. Goodbye!")
            sys.exit(0)

# Call the main function
if __name__ == "__main__":
    main()




