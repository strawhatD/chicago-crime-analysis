import sys
from Database import Database  

class MyDatabaseAppCLI:
    def __init__(self):
        # Initialize the database app
        self.db_app = Database() 

    def display_main_menu(self):
        print()
        print("=================================")
        print("         MAIN MENU    ")
        print("=================================")
        print("1. View/run Available Queries")
        print("2. View/run Available Commands")
        print("3. Exit")
        print("4. Help")
        print()

    def display_queries_menu(self):
        print("=================================")
        print("         AVAILABLE QUERIES      ")
        print("=================================")
        print("1.1 View")
        print("1.2 Search")
        print("1.3 Statistics")
        print("Enter the command number you wish to execute or type 'back' to return to the main menu.\n")
        print()
        

    def display_view_menu(self):
        print("=================================")
        print("           VIEW MENU            ")
        print("=================================")
        print("1. View Weapons")
        print("2. View Premises")
        print("3. View Crime Types")
        print("4. View Areas")
        print("4.1 View Crime History in Specific Area")
        print("5. View Statuses")
        print("Enter your choice or type 'back' to return.")
        print()

    def view_menu(self):
        while True:
            self.display_view_menu()
            choice = input("Please select an option or type 'back' to return: ").strip()
            if choice == "1":
                self.db_app.view_weapons()
            elif choice == "2":
                self.db_app.view_premises()
            elif choice == "3":
                self.db_app.view_crime_types()
            elif choice == "4":
                self.db_app.view_areas()
            elif choice == "4.1":
                area = input("Enter Area:")
                self.db_app.crime_history_in_area(area)
            
            elif choice == "5":
                self.db_app.view_status()
            elif choice.lower() == "back":
                break
            elif choice.lower() == "c-options":
                self.display_crime_commands_menu()
                print()
            elif choice.lower() == "q-options":
                self.display_queries_menu()
            else:
                print("Invalid option. Please try again.")

    def display_search_menu(self):
        print("=================================")
        print("          SEARCH MENU           ")
        print("=================================")
        print("1. Search by Area")
        print("2. Search by Premise")
        print("3. Search by Poverty Rate")
        print("4. Search by Population")
        print("5. Search by Status")
        print("6. Search by Crime Type")
        print("7. Search by Weapon")
        print("8. Search by Time Range")
        print("Enter your choice or type 'back' to return.")
        print()

    def search_menu(self):
        while True:
            self.display_search_menu()
            choice = input("Please select an option or type 'back' to return: ").strip()
            if choice == "1":
                print("Available Areas:")
                self.db_app.view_areacodes()
                area = input("Enter area: ")
                self.db_app.search_by_area(area)
            elif choice == "2":
                print("Available Premises:")
                self.db_app.view_premises()
                premise = input("Enter premise code: ")
                self.db_app.search_by_premise(premise)
            elif choice == "3":
                poverty_rate = float(input("Enter poverty rate: "))
                self.db_app.search_by_poverty_rate(poverty_rate)
            elif choice == "4":
                population_number = input("Enter population: ")
                self.db_app.search_by_demographics(population_number)
            elif choice == "5":
                print("Available Statuses:")
                self.db_app.view_status()
                status = input("Enter status code: ")
                self.db_app.search_by_status(status)
            elif choice == "6":
                print("Available Crime Types:")
                self.db_app.view_crime_types()
                crime_type = input("Enter crime type code: ")
                self.db_app.search_by_crime_type(crime_type)
            elif choice == "7":
                print("Available Weapons:")
                self.db_app.view_weapons()
                weapon = input("Enter weapon code: ")
                self.db_app.search_by_weapon(weapon)
            elif choice == "8":
                time_range = input("Enter time range(morning/afternoon/night): ")
                self.db_app.search_by_time_range(time_range)
            elif choice.lower() == "back":
                break
            elif choice.lower() == "c-options":
                self.display_crime_commands_menu()
                print()
            elif choice.lower() == "q-options":
                self.display_queries_menu()
            else:
                print("Invalid option. Please try again.")

    def display_statistics_menu(self):
        print("=================================")
        print("         STATISTICS MENU        ")
        print("=================================")
        print("1. Statistics by Crime Type")
        print("2. Statistics by Area")
        print("3. Statistics by Victim Type")
        print("4. Statistics by Status")
        print("5. Statistics by Weapon")
        print("6. Statistics by Time Range")
        print("7. Statistics by Poverty Rate")
        print("Enter your choice or type 'back' to return.")
        print()

    
    def display_statistics_crimetype_menu(self):
        print("=================================")
        print("      STATISTICS BY CRIME TYPE      ")
        print("=================================")
        print("1.1 Total Crimes")
        print("1.2 Total Crimes with Percentage")
        print("1.3 Crime Types by Status ")
        print("1.4 Crime Types by Area")
        print("Enter your choice or type 'back' to return.")
        print()

    def statistics_crimetype_menu(self):
        while True:
            self.display_statistics_crimetype_menu()
            choice = input("Please select an option or type 'back' to return: ").strip()
            if choice == "1.1":
                self.db_app.statistics_by_crime_type()
            elif choice == "1.2":
                self.db_app.percentage_crime_type()
            elif choice == "1.3":
                self.db_app.crime_type_status()
            elif choice == "1.4":
                self.db_app.crime_type_area()
            elif choice.lower() == "back":
                break
            elif choice.lower() == "c-options":
                self.display_crime_commands_menu()
                print()
            elif choice.lower() == "q-options":
                self.display_queries_menu()
            else:
                print("Invalid option. Please try again.")
    
    def display_statistics_area_menu(self):
        print("=================================")
        print("        STATISTICS BY AREA        ")
        print("=================================")
        print("2.1 Total Crimes by Area")
        print("2.2 Most Criminal Areas")
        print("2.3 Crimes by Area and Premise")
        print("2.4 Average Victim Age in Areas")
        print("2.5 Victim Age Distribution in Specific Area")
        print("2.6 Crimes in Homeowners Area")
        print("Enter your choice or type 'back' to return.")
        print()   
    
    def statistics_area_menu(self):
        while True:
            self.display_statistics_area_menu()
            choice = input("Please select an option or type 'back' to return: ").strip()
            if choice == "2.1":
                self.db_app.statistics_by_area()
            elif choice == "2.2":
                self.db_app.most_criminal_areas()
            elif choice == "2.3":
                self.db_app.crimes_by_area_premise()
            elif choice == "2.4":
                self.db_app.average_victim_age_by_area()
            elif choice == "2.5":
                print("Available Areas:")
                self.db_app.view_areacodes()
                area = input("Enter Area:")
                self.db_app.victim_age_in_area(area)
            elif choice == "2.6":
                self.db_app.crimes_in_homeowner_areas()
            elif choice.lower() == "back":
                break
            elif choice.lower() == "c-options":
                self.display_crime_commands_menu()
                print()
            elif choice.lower() == "q-options":
                self.display_queries_menu()
            else:
                print("Invalid option. Please try again.")
    
    def display_statistics_victim_menu(self):
        print("=================================")
        print("      STATISTICS BY VICTIM      ")
        print("=================================")
        print("3.1 Total Crimes by Gender")
        print("3.2 Total Crimes by Age")
        print("3.3 Top crimes reported by Females")
        print("3.4 Average Victim Age in Areas")
        print("3.5 Victim Age Distribution")
        print("3.6 Most Reported Crimes by Race")
        print("Enter your choice or type 'back' to return.")
        print()   

    def statistics_victim_menu(self):
        while True:
            self.display_statistics_victim_menu()
            choice = input("Please select an option or type 'back' to return: ").strip()
            if choice == "3.1":
                self.db_app.statistics_by_gender()
            elif choice == "3.2":
                self.db_app.crime_counts_by_age()
            elif choice == "3.3":
                self.db_app.top_crimes_reported_by_females()
            elif choice == "3.4":
                self.db_app.average_victim_age_by_area()
            elif choice == "3.5":
                self.db_app.victim_age_distribution()
            elif choice == "3.6":
                self.db_app.most_reported_crimes_by_race()
            elif choice.lower() == "back":
                break
            elif choice.lower() == "c-options":
                self.display_crime_commands_menu()
                print()
            elif choice.lower() == "q-options":
                self.display_queries_menu()
            else:
                print("Invalid option. Please try again.")
    def display_statistics_status_menu(self):
        print("=================================")
        print("         STATISTICS BY STATUS         ")
        print("=================================")
        print("4.1 Total Crimes for Each Status")
        print("4.2 Total Arrests and Open Invistigations by Area")
        print("Enter your choice or type 'back' to return.")
        print()

    def statistics_status_menu(self):
        while True:
            self.display_statistics_status_menu()
            choice = input("Please select an option or type 'back' to return: ").strip()
            if choice == "4.1":
                self.db_app.statistics_by_status()
            elif choice == "4.2":
                self.db_app.total_arrests_investigations()
            elif choice.lower() == "back":
                break
            elif choice.lower() == "c-options":
                self.display_crime_commands_menu()
                print()
            elif choice.lower() == "q-options":
                self.display_queries_menu()
            else:
                print("Invalid option. Please try again.")
    def display_statistics_weapon_menu(self):
        print("=================================")
        print("         STATISTICS BY WEAPON         ")
        print("=================================")
        print("5.1 Total Crimes for Each Weapon")
        print("5.2 Most Used Weapons")
        print("5.3 Total Crimes where Weapon was used/not used")
        print("5.4 Total Crimes with Arrest and Open Invistigations by Weapon")
        print("5.5 Most Used Weapon by Areas")
        print("Enter your choice or type 'back' to return.")
        print()
    
    def statistics_weapon_menu(self):
        while True:
            self.display_statistics_weapon_menu()
            choice = input("Please select an option or type 'back' to return: ").strip()
            if choice == "5.1":
                self.db_app.statistics_by_weapon()
            elif choice == "5.2":
                self.db_app.most_used_weapons()
            elif choice == "5.3":
                self.db_app.total_crimes_with_without_weapons()
            elif choice == "5.4":
                self.db_app.crimes_by_weapon_status()
            elif choice == "5.5":
                self.db_app.most_used_weapon_by_area()
            elif choice.lower() == "back":
                break
            elif choice.lower() == "c-options":
                self.display_crime_commands_menu()
                print()
            elif choice.lower() == "q-options":
                self.display_queries_menu()
            else:
                print("Invalid option. Please try again.")
        
    def statistics_menu(self): 
            while True:
                self.display_statistics_menu()
                choice = input("Please select an option or type 'back' to return: ").strip()
                if choice == "1":
                    self.statistics_crimetype_menu()
                elif choice == "2":
                    self.statistics_area_menu()
                elif choice == "3":
                    self.statistics_victim_menu()
                elif choice == "4":
                    self.statistics_status_menu()
                elif choice == "5":
                    self.statistics_weapon_menu()
                elif choice == "6":
                    self.db_app.time_range_statistics()
                elif choice == "7":
                    self.db_app.most_frequent_crimes_by_poverty_rate()
                elif choice.lower() == "back":
                    break
                elif choice.lower() == "c-options":
                    self.display_crime_commands_menu()
                    print()
                elif choice.lower() == "q-options":
                    self.display_queries_menu()
                else:
                    print("Invalid option. Please try again.")
    def display_commands_menu(self):
        print("=================================")
        print("         AVAILABLE COMMANDS     ")
        print("=================================")
        print("2.1 Weapon")
        print("2.2 Area")
        print("2.3 Premise")
        print("2.4 Crime")
        print()

    
    def display_weapon_commands_menu(self):
        print("=================================")
        print("          WEAPON COMMANDS         ")
        print("=================================")
        print("1. Add a new Weapon")
        print("2. Update an existing Weapon")
        print("3. Delete a Weapon")

    
    def weapon_commands_menu(self):
        while True:
            self.display_weapon_commands_menu()
            choice = input("Please select an option or type 'back' to return: ").strip()

            if choice == "1":
                print("Adding a new Weapon...")
                wcode = input("Enter Weapon Code: ")
                wdescription = input("Enter Weapon Description: ")
                if wcode.isdigit():
                    self.db_app.add_weapon(int(wcode), wdescription)
                else:
                    print("Invalid Weapon Code. It must be an integer.")

            elif choice == "2":
                print("Updating an existing Weapon...")
                wcode = input("Enter Weapon Code to update: ")
                new_description = input("Enter new Weapon Description: ")
                if wcode.isdigit():
                    self.db_app.update_weapon(int(wcode), new_description)
                else:
                    print("Invalid Weapon Code. It must be an integer.")

            elif choice == "3":
                print("Deleting a Weapon...")
                wcode = input("Enter Weapon Code to delete: ")
                if wcode.isdigit():
                    self.db_app.delete_weapon(int(wcode))
                else:
                    print("Invalid Weapon Code. It must be an integer.")

            elif choice.lower() == "back":
                break
            elif choice.lower() == "c-options":
                self.display_crime_commands_menu()
                print()
            elif choice.lower() == "q-options":
                self.display_queries_menu()
            else:
                print("Invalid option. Please try again.")

    def display_area_commands_menu(self):
        print("=================================")
        print("          AREA COMMANDS         ")
        print("=================================")
        print("1. Add a new Area")
        print("2. Update an existing Area")
        print("3. Delete an Area")
        print("Enter your choice or type 'back' to return.")
        print()

    def display_area_commands_menu(self):
        print("=================================")
        print("          AREA COMMANDS         ")
        print("=================================")
        print("1. Add a new Area")
        print("2. Update an existing Area")
        print("3. Delete an Area")
        print("Enter your choice or type 'back' to return.")
        print()

    def area_commands_menu(self):
        while True:
            self.display_area_commands_menu()
            choice = input("Please select an option or type 'back' to return: ").strip()

            if choice == "1":
                print("Adding a new Area...")
                area = input("Enter Area name: ").strip()
                try:
                    area_code = int(input("Enter Area Code (positive integer): ").strip())
                    population = int(input("Enter Population (non-negative integer): ").strip())
                    white_pop = int(input("Enter White Population (non-negative integer): ").strip())
                    black_pop = int(input("Enter Black Population (non-negative integer): ").strip())
                    indigenous_pop = int(input("Enter Indigenous Population (non-negative integer): ").strip())
                    asian_pop = int(input("Enter Asian Population (non-negative integer): ").strip())
                    hawaiian_pop = int(input("Enter Hawaiian Population (non-negative integer): ").strip())
                    other_pop = int(input("Enter Other Population (non-negative integer): ").strip())
                    multi_pop = int(input("Enter Multi-racial Population (non-negative integer): ").strip())
                    in_poverty = int(input("Enter Number in Poverty (non-negative integer): ").strip())
                    owner_occ = int(input("Enter Owner-occupied Households (non-negative integer): ").strip())
                    renter_occ = int(input("Enter Renter-occupied Households (non-negative integer): ").strip())
                    households_in_poverty = int(input("Enter Households in Poverty (non-negative integer): ").strip())
                    households_in_poverty_percent = float(input("Enter Households in Poverty Percent (non-negative float): ").strip())

                    # Check for positive area_code and non-negative values for others
                    if area_code <= 0 or any(x < 0 for x in [
                        population, white_pop, black_pop, indigenous_pop, asian_pop,
                        hawaiian_pop, other_pop, multi_pop, in_poverty, owner_occ,
                        renter_occ, households_in_poverty
                    ]) or households_in_poverty_percent < 0:
                        print("Error: All values must be non-negative, and Area Code must be positive.")
                    else:
                        self.db_app.add_area(
                            area, area_code, population, white_pop, black_pop,
                            indigenous_pop, asian_pop, hawaiian_pop, other_pop,
                            multi_pop, in_poverty, owner_occ, renter_occ,
                            households_in_poverty, households_in_poverty_percent
                        )
                except ValueError as e:
                    print(f"Error: Invalid input. {e}")

            elif choice == "2":
                print("Updating an existing Area...")
                area = input("Enter Area name to update: ").strip()

                try:
                    area_code = int(input("Enter Area Code (positive integer): ").strip())
                    population = int(input("Enter Population (non-negative integer): ").strip())
                    white_pop = int(input("Enter White Population (non-negative integer): ").strip())
                    black_pop = int(input("Enter Black Population (non-negative integer): ").strip())
                    indigenous_pop = int(input("Enter Indigenous Population (non-negative integer): ").strip())
                    asian_pop = int(input("Enter Asian Population (non-negative integer): ").strip())
                    hawaiian_pop = int(input("Enter Hawaiian Population (non-negative integer): ").strip())
                    other_pop = int(input("Enter Other Population (non-negative integer): ").strip())
                    multi_pop = int(input("Enter Multi-racial Population (non-negative integer): ").strip())
                    in_poverty = int(input("Enter Number in Poverty (non-negative integer): ").strip())
                    owner_occ = int(input("Enter Owner-occupied Households (non-negative integer): ").strip())
                    renter_occ = int(input("Enter Renter-occupied Households (non-negative integer): ").strip())
                    households_in_poverty = int(input("Enter Households in Poverty (non-negative integer): ").strip())
                    households_in_poverty_percent = float(input("Enter Households in Poverty Percent (non-negative float): ").strip())

                    # Check for positive area_code and non-negative values for others
                    if area_code <= 0 or any(x < 0 for x in [
                        population, white_pop, black_pop, indigenous_pop, asian_pop,
                        hawaiian_pop, other_pop, multi_pop, in_poverty, owner_occ,
                        renter_occ, households_in_poverty
                    ]) or households_in_poverty_percent < 0:
                        print("Error: All values must be non-negative, and Area Code must be positive.")
                    else:
                        self.db_app.update_area(
                            area, area_code, population, white_pop, black_pop,
                            indigenous_pop, asian_pop, hawaiian_pop, other_pop,
                            multi_pop, in_poverty, owner_occ, renter_occ,
                            households_in_poverty, households_in_poverty_percent
                        )
                except ValueError as e:
                    print(f"Error: Invalid input. {e}")

            elif choice == "3":
                print("Deleting an Area...")
                area = input("Enter Area name to delete: ").strip()
                self.db_app.delete_area(area)

            elif choice.lower() == "back":
                break
            elif choice.lower() == "c-options":
                self.display_crime_commands_menu()
                print()
            elif choice.lower() == "q-options":
                self.display_queries_menu()
            else:
                print("Invalid option. Please try again.")

    def display_premise_commands_menu(self):
        print("=================================")
        print("          PREMISE COMMANDS         ")
        print("=================================")
        print("1. Add a new Premise")
        print("2. Update an existing Premise")
        print("3. Delete a Premise")
        print("Enter your choice or type 'back' to return.")
        print()

    def premise_commands_menu(self):
        while True:
            self.display_premise_commands_menu()
            choice = input("Please select an option or type 'back' to return: ").strip()

            if choice == "1":
                print("Adding a new Premise...")
            elif choice == "2":
                print("Updating an existing Premise...")
            elif choice == "3":
                print("Deleting a Premise...")
            elif choice.lower() == "back":
                break
            elif choice.lower() == "c-options":
                self.display_crime_commands_menu()
                print()
            elif choice.lower() == "q-options":
                self.display_queries_menu()
            else:
                print("Invalid option. Please try again.")

    def display_crime_commands_menu(self):
        print("=================================")
        print("          CRIME COMMANDS         ")
        print("=================================")
        print("1. Add a new Crime")
        print("2. Add Crime type")
        print("3. Update weapon in existing Crime")
        print("4. Update status of existing Crime")
        print("5. Update date of existing Crime")
        print("6. Update time of existing Crime")
        print("7. Delete existing Crime")
        print("Enter your choice or type 'back' to return.")
        print()

    def crime_commands_menu(self):
        while True:
            self.display_crime_commands_menu()
            choice = input("Please select an option or type 'back' to return: ").strip()

            if choice == "1":
                print("Adding a new Crime...")
            elif choice == "2":
                print("Adding a new Crime Type...")
            elif choice == "3":
                print("Updating weapon in existing Crime...")
            elif choice == "4":
                print("Updating status of existing Crime...")
            elif choice == "5":
                print("Updating date of existing Crime...")
            elif choice == "6":
                print("Updating time of existing Crime...")
            elif choice == "7":
                print("Deleting existing Crime...")
            elif choice.lower() == "back":
                break
            elif choice.lower() == "c-options":
                self.display_crime_commands_menu()
                print()
            elif choice.lower() == "q-options":
                self.display_queries_menu()
            else:
                print("Invalid option. Please try again.")
    
    def display_help(self):
        print("=================================")
        print("         HELP MENU      ")
        print("=================================")
        print("1. About the Dataset")
        print("2. Navigation")
        print("3. View/Run Available Queries")
        print("4. View/Run Available Commands")
        print("5. Get Help")
        print("6. Back to Main Menu")
        print()
            
    def help_menu(self):
        self.display_help()
        while True:
            choice = input("Please select an option: ").strip()

            if choice == "1":
                print("=================================")
                print("         ABOUT THE APPLICATION   ")
                print("=================================")
                print("Welcome to the Database App!")
                print("The Los-Angeles Crime dataset contains detailed information on reported crimes in Los-Angeles.")
                print("It includes the following fields:")
                print("- Crime Type: The category of the crime (e.g., theft, assault, robbery).")
                print("- Location: The geographical area where the crime occurred.")
                print("- Date: The date and time the crime was reported.")
                print("- Description: Additional details about the crime.")
                print("- Arrests and Outcomes: Information on whether arrests were made.")
                print("- Demographics and Social Classes: Data about the population in the affected areas,\n including income levels, and demographic trends, which helps in understanding how crime correlates with societal factors.   ")
                print("Press Enter to return to Help Menu")
                input()
                self.display_help()
            elif choice == "2":
                print("=================================")
                print("      NAVIGATION INSTRUCTIONS    ")
                print("=================================")
                print("1. Use the numbered options to select menu items (e.g., type '1' to select the first option).")
                print("2. Type 'back' at any point to return to the previous menu.")
                print("3. Type 'exit' to quit the application.")
                print("\nQuick Commands:")
                print("- `q-options`: Quickly view available queries from the View/Run Available Queries menu.")
                print("- `c-options`: Quickly view available commands from the View/Run Available Commands menu.")
                print("\nAll user inputs are validated to ensure safety and avoid errors.")
                print("Press Enter to return to Help Menu")
                input()
                self.display_help()
            elif choice == "3":
                print("=================================")
                print("    VIEW/RUN AVAILABLE QUERIES   ")
                print("=================================")
                print("How to use:")
                print("1. Select a query category:")
                print("\n2. Follow the on-screen prompts to input parameters for specific queries.")
                print("3. Results will be displayed in a readable format.")
                print("\nYou can return to the Available Queries menu anytime by typing 'back'.")
                print("Available queries Description:")
                print("- 1.1 View: View data such as Weapons, Premises, Crime Types, or Areas.")
                print("View Weapons: Displays all weapons used in crimes, along with their descriptions.")
                print("View Premises: Shows all premises where crimes occurred, with brief descriptions.")
                print("View Crime Types: Lists all crime types with their descriptions.")
                print("View Areas: Displays all areas and their details")
                print("- 1.2 Search: Filter data by date range, area, premise, poverty rate, etc.")
                print("Search by Area: Find crime records for a specific area.")
                print("Search by Premise: Retrieve crimes occurring at a specific premise type.")
                print("Search by Poverty Rate: Filter crimes in areas with a specified poverty rate or higher.")
                print("Search by Population: Retrieve crimes based on population.")
                print("Search by Status: Find crimes based on their status")
                print("Search by Crime Type: Retrieve crimes based on a specific Crime type.")
                print("Search by Weapon: Filter crimes involving a specific weapon type.")
                print("Search by Time Range: Retrieve crimes that occurred in a specific time frame (e.g., morning, afternoon).")
                print("- 1.3 Statistics: View aggregated data like crime trends by year or area.")
                print("Statistics by Crime Type: Displays crime statistics by crime type.")
                print("Statistics by Area: Displays crime statistics by area.")
                print("Statistics by Gender: Displays crime statistics based on victim gender.")
                print("Statistics by Status: Displays statistics by crime status.")
                print("Statistics by Weapon: Displays statistics of weapons use in crimes.")
                print("Statistics by Time Range: Displays crime statistics by time ranges (e.g., morning, afternoon).")
                print("Statistics by Poverty Rate: Displays crime statistics based on poverty rates.")
                print("Press Enter to return to Help Menu")
                input()
                self.display_help()
            elif choice == "4":
                print("=================================")
                print("   VIEW/RUN AVAILABLE COMMANDS    ")
                print("=================================")
                print("How to use:")
                print("1. Commands allow you to safely update or add new data:")
                print("2. To execute a command:")
                print("   - Select a command by its number.")
                print("   - Enter required inputs (e.g., IDs, names, or descriptions).")
                print("   - Follow on-screen prompts to confirm changes.")
                print("\nImportant:")
                print("- Deleting data or resetting the database is restricted to prevent accidental data loss.")
                print("- Use descriptive names and ensure inputs are valid.")
                print("\nAvailable commands:")
                print("-2.1 Weapon")
                print("Add a New Weapon: Add a new weapon type to the database (e.g., firearm, knife).")
                print("Update an Existing Weapon: Modify the description of an existing weapon based on its weapon code.")
                print("Delete a Weapon: Remove a weapon type from the database using its code.")
                print("-2.2 Area")
                print("Add a New Area: Add a new area with its name, population, poverty rate, and demographics.")
                print("Update an Existing Area: Modify specific details of an area, such as population or poverty rate.")
                print("Delete an Area: Remove an area and its associated data from the database using its name.")
                print("-2.3 Premise")
                print("Add a New Premise: Add a new premise type to the database (e.g., school, park).")
                print("Update an Existing Premise: Modify the description of an existing premise based on its premise code.")
                print("Delete a Premise: Remove a premise from the database using its code.")
                print("-2.4 Crime")
                print("Add a New Crime: Add a new crime record with details like date, area, and type.")
                print("Add Crime Type: Add a new crime type (CR code and description) to the database.")
                print("Update Weapon in Existing Crime: Modify the weapon used in an existing crime.")
                print("Update Status of Existing Crime: Change the status of a crime ")
                print("Update Date of Existing Crime: Adjust the date a crime occurred.")
                print("Update Time of Existing Crime: Modify the time a crime occurred.")
                print("Delete Existing Crime: Remove a crime record from the database using its unique identifier.")
                print("Press Enter to return to Help Menu")
                input()
                self.display_help()
            elif choice == "5":
                print("=================================")
                print("             GET HELP          ")
                print("=================================")
                print("1. Invalid Input:")
                print("   - Error: Invalid option. Please try again.")
                print("   - Fix: Ensure you are entering a valid number or command (e.g., '1', 'back').")
                print("\n2. SQL Error:")
                print("   - Error: 'Database constraint violation' or 'Invalid query.'")
                print("   - Fix: Ensure inputs match the expected format (e.g., dates as YYYY-MM-DD).")
                print("\n3. No Results Found:")
                print("   - Cause: Query did not match any data.")
                print("   - Fix: Double-check your inputs (e.g., area name, date range).")
                print("Press Enter to return to Help Menu")
                input()
                self.display_help()
            elif choice == "6" or choice.lower() == "back":
                print("Thank you for using the Help Menu! Returning to the main menu...")
                break
            else:
                print("Invalid option. Please try again.")

    def view_run_available_queries(self):
        while True:
            self.display_queries_menu()
            choice = input("Please select a query to run or type 'back' to return: ").strip()

            if choice == "1.1":
                self.view_menu()
            elif choice == "1.2":
                self.search_menu()
            elif choice == "1.3":
                self.statistics_menu()
            elif choice.lower() == 'back':
                break
            else:
                print("Invalid option. Please try again.")

    


    def view_run_available_commands(self):
        while True:
            self.display_commands_menu()
            choice = input("Please select a command to run or type 'back' to return: ").strip()

            if choice == "2.1":
                self.weapon_commands_menu()
            elif choice == "2.2":
                self.area_commands_menu()
            elif choice == "2.3":
                self.premise_commands_menu()
            elif choice == "2.4":
                self.crime_commands_menu()
            elif choice.lower() == 'back':
                break
            else:
                print("Invalid option. Please try again.")

    def run(self):
        try:
            while True:
                print("Welcome to the Database App!")
                self.display_main_menu()
                choice = input("Please select an option: ").strip()

                if choice == "1":
                    self.view_run_available_queries()
                elif choice == "2":
                    self.view_run_available_commands()
                elif choice == "3":
                    print("Exiting the program.")
                    self.db_app.close()
                    break
                elif choice == "4":
                    self.help_menu()
                else:
                    print("Invalid option. Please try again.")
                    print()

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            # Ensure the database connection is closed when the program ends
            if hasattr(self.db_app, 'close'):
                try:
                    self.db_app.close()
                except Exception as e:
                    print(f"Error while closing the database: {e}")

if __name__ == "__main__":
    try:
        app_cli = MyDatabaseAppCLI()  # Correct class instantiation
        app_cli.run()
    except Exception as e:
        print(f"Failed to initialize the application: {e}")
