def age_calculation():
    current_year = input("Please Enter Current Year:")
    current_year = int(current_year)
    current_month = input("Please Enter Current Month:")
    current_month = int(current_month)
    birth_year = input("Please Enter Your Birth Year:")
    birth_year = int(birth_year)
    birth_month = input("Please Enter Your Birth Month:")
    birth_month = int(birth_month)

    print("Current Year:", current_year)
    print("Current Month:", current_month)
    print("Birth Year:", birth_year)
    print("Birth Month:", birth_month)

    months = (current_year - birth_year) * 12 + (current_month - birth_month)
    print("Your age in months: ", months)

def main():
    age_calculation()
    age_calculation()
    age_calculation()

main()