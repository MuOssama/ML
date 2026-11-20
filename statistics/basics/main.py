from  calc import *

def read_data():
    """Ask the user for numbers separated by spaces or commas."""
    while True:
        raw = input("Enter numbers separated by spaces or commas: ").replace(",", " ")
        try:
            data = [float(x) for x in raw.split()]
            if not data:
                print("Please enter at least one number.")
                continue
            return data
        except ValueError:
            print("Invalid input. Numbers only, please.")


MENU = """
===== Statistics Menu =====
1. Mean
2. Median
3. Variance
4. Standard deviation
5. Z-score of a value
6. Standardize all data
7. Skewness
8. Show everything
9. Enter new data
0. Exit
"""

def main():
    stats = Statistics(read_data())

    while True:
        print(MENU)
        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                print(f"Mean: {stats.mean():.4f}")
            elif choice == "2":
                print(f"Median: {stats.median():.4f}")
            elif choice == "3":
                print(f"Variance: {stats.variance():.4f}")
            elif choice == "4":
                print(f"Standard deviation: {stats.deviation():.4f}")
            elif choice == "5":
                x = float(input("Enter the value X: "))
                print(f"Z-score of {x}: {stats.z(x):.4f}")
            elif choice == "6":
                print("Standardized data:")
                print([round(z, 4) for z in stats.standerdize()])
            elif choice == "7":
                print(f"Skewness: {stats.check_skewneess():.4f}")
            elif choice == "8":
                print(f"Data:               {stats._list}")
                print(f"Mean:               {stats.mean():.4f}")
                print(f"Median:             {stats.median():.4f}")
                print(f"Variance:           {stats.variance():.4f}")
                print(f"Standard deviation: {stats.deviation():.4f}")
                print(f"Skewness:           {stats.check_skewneess():.4f}")
            elif choice == "9":
                stats = Statistics(read_data())
            elif choice == "0":
                print("Goodbye!")
                break
            else:
                print("Invalid choice, try again.")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()