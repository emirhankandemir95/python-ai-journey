import math
import time
plates = []
hourly_rate = 50 # Parking fee per hour
parking_spots = 20
while True:
    print("\n--- SMART PARKING SYSTEM ---")
    print("1: Park a Car")
    print("2: Remove a Car")
    print("3: View Parked Cars")
    print("4: Exit")
    choice = input("Select an option: ")
    if choice == "1":
        if len(plates) < parking_spots:
            plate = input("Enter car plate number: ")
            if plate in plates:
                print("Error: This car is already parked.")
            else:
                plates.append(plate)
                print(f"Car with plate {plate} has been parked.")
        else:
            print("Error: Parking is full.")
    elif choice == "2":
        plate = input("Enter car plate number to remove: ")
        if plate in plates:
            plates.remove(plate)
            print(f"Car with plate {plate} has been removed from parking.")
        else:
            print("Error: This car is not found in the parking.")
    elif choice == "3":
        if plates:
            print("Parked Cars:")
            for p in plates:
                print(f"- {p}")
        else:
            print("No cars are currently parked.")
    elif choice == "4":
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid selection, please choose a valid option.")

    time.sleep(1)
    