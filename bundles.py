def nunua_bundles():
     current_balance = int(150)
     accept = int(1)
     decline = int(2)
	 print("\n Available data plans: ")
	 print("\n 1: 4GB 1000\n")
	 print("\n 2: Daily Bundles\n")
	 print("\n 3: Weekly Bundles\n")
	 print("\n 4: Monthly Bundles\n")
	 print("\n 5: Blaze Bundles\n")
	 print("\n 00: Back \n")

	 option = input(" Please select an option:")
	 # try:
	 # 	option = int()
	 # except ValueError:
	 # 	option = input("please enter a value")
	 # 	print("Invalid option")

     if (option == 1):
     	bundle_price = int(1000)
		print("Are you sure you want to buy 4gb at ksh{}".format(bundle_price))




nunua_bundles()