# Foram Dholariya
# 8 June 2026
# Module 1.2 - Bottles on the Wall
# Purpose: Print the bottles on the wall song using a loop.

# This program displays the bottles on the wall countdown.

def countdown(bottles):
    while bottles > 1:
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        bottles -= 1

        if bottles == 1:
            print(f"Take one down and pass it around, {bottles} bottle of beer on the wall.\n")
        else:
            print(f"Take one down and pass it around, {bottles} bottles of beer on the wall.\n")

    print("1 bottle of beer on the wall, 1 bottle of beer.")
    print("Take one down and pass it around, no more bottles of beer on the wall.\n")


def main():
    bottles = int(input("How many bottles of beer are on the wall? "))
    countdown(bottles)
    print("Time to buy more beer!")


main()