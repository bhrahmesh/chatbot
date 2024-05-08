import pandas as pd
import random

# Load employee data from Excel file
employee_data = pd.read_excel("employee_data.xlsx")

# Function to retrieve employee schedule
def get_schedule(employee_name, employee_data):
    schedule = employee_data.loc[employee_data['name'] == employee_name, 'schedule'].values
    if len(schedule) > 0:
        return schedule
    else:
        return "Sorry, I couldn't find the schedule for {}".format(employee_name)

# Function to retrieve leave balance
def get_leave_balance(employee_name, employee_data):
    leaves_taken = employee_data.loc[employee_data['name'] == employee_name, 'leaves_taken'].values
    if len(leaves_taken) > 0:
        total_leaves = 20  # Assuming total annual leaves allowed is 20
        leave_balance = total_leaves - leaves_taken[0]
        return leave_balance
    else:
        return "Sorry, I couldn't find the leave balance for {}".format(employee_name)


def generate_response(user_input):
    user_input = user_input.lower()
    
    # Extract employee name from user input
    employee_names = employee_data['name'].tolist()
    matching_names = [name for name in employee_names if name.lower() in user_input]
    
    if not matching_names:
        return "I'm sorry, I couldn't identify the employee. Please provide a valid employee name."
    
    # If multiple matching names are found, prioritize the longer name (to handle cases like 'xxx' and 'xxx2')
    employee_name = max(matching_names, key=len)
    
    if "schedule" in user_input:
        schedule = get_schedule(employee_name, employee_data)  # Pass employee_data to get_schedule
        return "{}'s schedule: {}".format(employee_name, schedule)
    elif "leave balance" in user_input or "holiday" in user_input:
      leave_balance = get_leave_balance(employee_name, employee_data)  # Pass employee_data to get_leave_balance
      return "{}'s leave balance is {} days.".format(employee_name, leave_balance)

    else:
        return "I'm sorry, I don't understand. Can you please rephrase your question?"



# Main function to handle user interaction
def main():
    print("Welcome to the Employee Chatbot!")
    print("How can I assist you today?")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        response = generate_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
