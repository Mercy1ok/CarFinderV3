AllowedVehiclesList = [
  'Ford F-150',
  'Chevrolet Silverado',
  'Tesla CyberTruck',
  'Toyota Tundra',
  'Nissan Titan'
] 

Authorized_Cars = AllowedVehiclesList[0] + ', ' + AllowedVehiclesList[1] + ', ' + AllowedVehiclesList[3] + ', ' + AllowedVehiclesList[4]

UnAuthorized_Cars = AllowedVehiclesList[2]

while True:
    menu = """********************************
AutoCountry Vehicle Finder v0.2
********************************
Please Enter the following number below from the following menu:

1. PRINT all Authorized Vehicles
2. SEARCH for an Authorized Vehicle
3. ADD an Authorized Vehicle
4. Exit
********************************"""
    print(menu)
    option = int(input("Enter your choice: "))

    if option == 1:
        print("********************************")
        responce = ("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
        print(f"\033[1m{responce}\033[0m")
        for vehicle in AllowedVehiclesList:
            print(vehicle)

    elif option == 2:
      print('*******************************')
      selected_car = "Please Enter the full Vehicle name: "
      selected_caro = input(f"\033[1m{selected_car}\033[0m")


      if selected_caro in Authorized_Cars:
          print('                                      ')
          selecteddd = f"{selected_caro} is an authorized vehicle."
          print(f"\033[1m{selecteddd}\033[0m")
          print(menu)
      elif selected_caro in UnAuthorized_Cars:
          print('                                      ')
          unselected = f"{selected_caro} is not an authorized vehicle, if you received this in error please check the spelling and try again."
          print(f"\033[1m{unselected}\033[0m")
      else:
          print("Invalid car selection.")

    elif option == 3:
      print('*******************************')
      pink = ("Please Enter the full Vehicle name you would like to add: ")
      sales_rep_selection=input(f"\033[1m{pink}\033[0m")
      AllowedVehiclesList.append(sales_rep_selection)
      chosen = (f"You have added {sales_rep_selection} as an authorized vehicle.")
      print("                 ")
      print(f"\033[1m{chosen}\033[0m")

    elif option == 4:
        print("********************************")
        print("Thank you for using the AutoCountry Vehicle Finder, goodbye!")
        break

    else:
        print("Invalid option")
