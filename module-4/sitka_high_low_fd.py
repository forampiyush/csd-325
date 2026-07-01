"""
Name: Your Name
Course: CSD-325
Module: 4

Program: sitka_high_low_fd.py

Description:
This program allows the user to view either the daily high
or daily low temperatures from the Sitka weather data.
The program continues to display a menu until the user
chooses to exit.
"""

import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt

filename = "sitka_weather_2018_simple.csv"

# Read weather data
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates = []
    highs = []
    lows = []

    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        dates.append(current_date)

        highs.append(int(row[5]))
        lows.append(int(row[6]))


def show_highs():
    """Display high temperatures."""
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c="red")

    plt.title("Daily High Temperatures - 2018", fontsize=24)
    plt.xlabel("", fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis="both", which="major", labelsize=16)

    plt.show()


def show_lows():
    """Display low temperatures."""
    fig, ax = plt.subplots()
    ax.plot(dates, lows, c="blue")

    plt.title("Daily Low Temperatures - 2018", fontsize=24)
    plt.xlabel("", fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis="both", which="major", labelsize=16)

    plt.show()


def main():
    """Display the menu until the user chooses to exit."""
    while True:
        print("\n===== Sitka Weather Menu =====")
        print("1. High Temperatures")
        print("2. Low Temperatures")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            show_highs()

        elif choice == "2":
            show_lows()

        elif choice == "3":
            print("\nThank you for using the Sitka Weather program. Goodbye!")
            sys.exit()

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


main()