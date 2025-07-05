from datetime import datetime, timedelta

def display_current_datetime():

    current_datetime = datetime.now()
    print("Current Date and Time:", current_datetime.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    try:
        days_to_add = int(input("Enter the number of days to add:"))
        future_date = display_current_datetime + timedelta(days=days_to_add)
        print("Future Date:", future_date.strftime("%Y-%m-%d %H:%M:%S"))
    except ValueError:
        print("Invalid input. Please enter a valid number of days.")



