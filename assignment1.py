def get_season(month):
    season_mapping = {
        1: 'Winter', 2: 'Winter', 3: 'Spring',
        4: 'Spring', 5: 'Spring', 6: 'Summer',
        7: 'Summer', 8: 'Summer', 9: 'Autumn',
        10: 'Autumn', 11: 'Autumn', 12: 'Winter'
    }

    if 1 <= month <= 12:
        return season_mapping[month]
    else:
        return "Invalid month"

def main():
    try:
        month = int(input("Enter the number of a month (1-12): "))
        season = get_season(month)
        print(f"The season corresponding to month {month} is {season}.")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
