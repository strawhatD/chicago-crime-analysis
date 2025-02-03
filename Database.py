import sqlite3
import csv

class Database:
    def __init__(self):
        self.connection = sqlite3.connect(":memory:") 
        self.create_area_demographics_table()
        self.create_crimes_data_table()
        self.create_premise_table()
        self.create_status_table()
        self.create_weapon_table() 
        self.load_area_demographics_from_csv("AreaDemographics.csv")
        self.load_crimes_data_from_csv("crimesData.csv")
        self.load_premise_from_csv("Premise.csv")
        self.load_status_from_csv("Status.csv")
        self.load_weapon_from_csv("Weapon.csv") 

    def create_area_demographics_table(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE AreaDemographics (
                Area TEXT PRIMARY KEY,
                areaCode INTEGER,
                population INTEGER,
                white_pop INTEGER,
                black_pop INTEGER,
                indigenous_pop INTEGER,
                asian_pop INTEGER,
                hawaiian_pop INTEGER,
                other_pop INTEGER,
                multi_pop INTEGER,
                inPoverty INTEGER,
                owner_occ INTEGER,
                renter_occ INTEGER,
                HouseholdsInPoverty INTEGER,
                HouseholdsInPovertyPercent REAL
            )
        """)
        self.connection.commit()

    def create_crimes_data_table(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE CrimesData (
                DR TEXT PRIMARY KEY,
                dateReported TEXT,
                dateOccured TEXT,
                timeOccured TEXT,
                Area TEXT,
                CRcode INTEGER,
                CRdescription TEXT,
                victAge INTEGER,
                victGender TEXT,
                victRace TEXT,
                premisCode INTEGER,
                weaponCode TEXT,
                statusCode TEXT
            )
        """)
        self.connection.commit()

    def create_premise_table(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE Premise (
                Pcode INTEGER PRIMARY KEY,
                Pdescription TEXT
            )
        """)
        self.connection.commit()

    def create_status_table(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE Status (
                Cstatus TEXT PRIMARY KEY,
                CstatusDescr TEXT
            )
        """)
        self.connection.commit()

    def create_weapon_table(self): 
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE Weapon (
                Wcode INTEGER PRIMARY KEY,
                Wdescription TEXT
            )
        """)
        self.connection.commit()

    def load_area_demographics_from_csv(self, filename):
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip the header row
            with self.connection:
                for row in reader:
                    self.connection.execute("""
                        INSERT INTO AreaDemographics VALUES (
                            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
                        )
                    """, row)

    def load_crimes_data_from_csv(self, filename):
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip the header row

            with self.connection:
                for row in reader:
                    cleaned_row = [
                        self.clean_crime_value(value, i) for i, value in enumerate(row)
                    ]
                    self.connection.execute("""
                        INSERT INTO CrimesData VALUES (
                            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
                        )
                    """, cleaned_row)

    def load_premise_from_csv(self, filename):
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip the header row

            with self.connection:
                for row in reader:
                    self.connection.execute("""
                        INSERT INTO Premise VALUES (?, ?)
                    """, row)

    def load_status_from_csv(self, filename):
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip the header row

            with self.connection:
                for row in reader:
                    self.connection.execute("""
                        INSERT INTO Status VALUES (?, ?)
                    """, row)

    def load_weapon_from_csv(self, filename):  # New method to load Weapon data
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip the header row

            with self.connection:
                for row in reader:
                    self.connection.execute("""
                        INSERT INTO Weapon VALUES (?, ?)
                    """, row)

    def clean_crime_value(self, value, index):
        value = value.strip()
        if value == "":
            return None
        if index in [5, 7, 10]:  # CRcode, victAge, premisCode are integers
            return int(value)
        return value

    def print_table_results(self, title, headers, data, column_widths=None):
        if not data:
            print(f"{title}\nNo results found.")
            return

        column_widths = column_widths if column_widths else [15] * len(headers)
        print()
        print("=" * sum(column_widths))
        print(f"{title}")
        print("=" * sum(column_widths))
        print(" | ".join(f"{header:<{column_widths[i]}}" for i, header in enumerate(headers)))
        print("-" * sum(column_widths))

        for row in data:
            print(" | ".join(f"{str(cell):<{column_widths[i]}}" for i, cell in enumerate(row)))

        print("-" * sum(column_widths))
        input("Press Enter to return to the menu...")

    def print_table(self, table_name):
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        headers = [description[0] for description in cursor.description]

        # Calculate column widths
        col_widths = [max(len(str(row[i])) for row in [headers] + rows) for i in range(len(headers))]

        # Print the header
        header_row = " | ".join(f"{headers[i]:<{col_widths[i]}}" for i in range(len(headers)))
        print(header_row)
        print("-" * len(header_row))

        # Print each row
        for row in rows:
            row_str = " | ".join(f"{str(row[i]):<{col_widths[i]}}" for i in range(len(row)))
            print(row_str)

        print("\n")  # Blank line between tables


    def print_all(self):
        self.print_table("AreaDemographics")
        self.print_table("Premise")
        self.print_table("Status")
        self.print_table("Weapon")
        self.print_table("CrimesData")

    #### VIEW MENU ####

    def view_areacodes(self):
        try:
            cursor = self.connection.cursor()
            query = "SELECT areaCode, Area FROM AreaDemographics"
            cursor.execute(query)
            results = cursor.fetchall()

            print("=================================")
            print("          AREA CODES            ")
            print("=================================")
            print("Code | Area")
            print("------------------------------")
            for row in results:
                print(f"{row[0]:<5} | {row[1]}")
            print("------------------------------")
            input("Press Enter to continue...")
        except Exception as e:
            print(f"Error fetching area codes: {e}")

    def view_weapons(self):
        try:
            cursor = self.connection.cursor()
            query = "SELECT Wcode, Wdescription FROM Weapon"
            cursor.execute(query)
            results = cursor.fetchall()

            print("=================================")
            print("          WEAPON LIST            ")
            print("=================================")
            print("Code | Description")
            print("------------------------------")
            for row in results:
                print(f"{row[0]:<5} | {row[1]}")
            print("------------------------------")
            input("Press Enter to continue...")
        except Exception as e:
            print(f"Error fetching weapons: {e}")

    def view_premises(self):
        try:
            cursor = self.connection.cursor()
            query = "SELECT Pcode, Pdescription FROM Premise"
            cursor.execute(query)
            results = cursor.fetchall()

            print("=================================")
            print("         PREMISE LIST            ")
            print("=================================")
            print("Code | Description")
            print("------------------------------")
            for row in results:
                print(f"{row[0]:<5} | {row[1]}")
            print("------------------------------")
            input("Press Enter to continue...")
        except Exception as e:
            print(f"Error fetching premises: {e}")

    def view_crime_types(self):
        try:
            cursor = self.connection.cursor()
            query = "SELECT CRcode, CRdescription FROM crimesData GROUP BY CRcode, CRdescription"
            cursor.execute(query)
            results = cursor.fetchall()

            print("=================================")
            print("        CRIME TYPE LIST          ")
            print("=================================")
            print("Code | Description")
            print("------------------------------")
            for row in results:
                print(f"{row[0]:<5} | {row[1]}")
            print("------------------------------")
            input("Press Enter to continue...")
        except Exception as e:
            print(f"Error fetching crime types: {e}")

    def view_areas(self):
        try:
            cursor = self.connection.cursor()
            query = "SELECT Area, population, HouseholdsInPovertyPercent FROM AreaDemographics"
            cursor.execute(query)
            results = cursor.fetchall()

            print("=================================")
            print("          AREA LIST              ")
            print("=================================")
            print(f"{'Area':<20} | {'Population':<15} | {'Poverty Rate (%)':<10}")
            print("---------------------------------------------")
            for row in results:
                print(f"{row[0]:<20} | {row[1]:<15} | {row[2]:<10}")
            print("---------------------------------------------")
            input("Press Enter to continue...")
        except Exception as e:
            print(f"Error fetching areas: {e}")


    def view_status(self):
        try:
            cursor = self.connection.cursor()
            query = "SELECT Cstatus, CstatusDescr FROM Status"
            cursor.execute(query)
            results = cursor.fetchall()

            print("=================================")
            print("          STATUS LIST            ")
            print("=================================")
            print("Code | Description")
            print("------------------------------")
            for row in results:
                print(f"{row[0]:<5} | {row[1]}")
            print("------------------------------")
            input("Press Enter to continue...")
        except Exception as e:
            print(f"Error fetching status: {e}")

    #### STATISTICS MENU ####

    #### CRIME TYPE STATISTICS ####
    def statistics_by_crime_type(self):
        try:
            cursor = self.connection.cursor()
            query = """
                SELECT CRdescription, COUNT(*) as CrimeCount
                FROM crimesData
                GROUP BY CRdescription
                ORDER BY CrimeCount DESC
            """
            cursor.execute(query)
            results = cursor.fetchall()
            headers = ["Crime Type", "Number of Crimes"]
            column_widths = [60, 16]
            self.print_table_results(f"TOTAL CRIMES BY TYPE", headers, results, column_widths)
        except Exception as e:
            print(f"Error fetching statistics by crime type: {e}")

    def percentage_crime_type(self):
        try:
            cursor = self.connection.cursor()
            query = """
                SELECT CRdescription, COUNT(*) AS totalCrimes, ROUND((COUNT(*) * 100.0 / SUM(COUNT(*)) OVER()), 2) AS crimePercentage  
                FROM CrimesData  
                GROUP BY CRdescription  
                ORDER BY crimePercentage DESC;
            """
            cursor.execute(query)
            results = cursor.fetchall()
            headers = ["Crime Type", "Total Crimes", "Crime Percentage" ]
            column_widths = [60, 14, 18]
            self.print_table_results(f"TOTAL CRIMES BY TYPE PERCENTAGE", headers, results, column_widths)
        except Exception as e:
            print(f"Error fetching percentage distribution by crime type: {e}")

    def crime_type_status(self):
        try:
            cursor = self.connection.cursor()
            query = """
                SELECT 
                    CASE WHEN CRdescription IS NULL THEN 'Unknown Crime Type' ELSE CRdescription END AS crimeType, 
                    CASE WHEN statusCode IS NULL THEN 'Unknown' ELSE statusCode END AS statusCode, 
                    COUNT(*) AS caseCount
                FROM CrimesData
                GROUP BY CRdescription, statusCode
                ORDER BY crimeType, statusCode;
            """
            cursor.execute(query)
            results = cursor.fetchall()
            headers = ["Crime Type", "Status", "Case Count" ]
            column_widths = [60, 10, 12]
            self.print_table_results(f"CRIME TYPE STATISTICS BY STATUS", headers, results, column_widths)
        except Exception as e:
            print(f"Error fetching crime type statistics: {e}")


    def crime_type_area(self):
        try:
            cursor = self.connection.cursor()
            query = """
                SELECT Area, CRdescription, COUNT(*) AS crimeCount
                FROM CrimesData
                GROUP BY Area, CRdescription
                ORDER BY Area, crimeCount DESC
            """
            cursor.execute(query)
            results = cursor.fetchall()
            headers = ["Area", "Crime Type", "Case Count" ]
            column_widths = [15, 60, 12]
            self.print_table_results(f"CRIME TYPE STATISTICS BY AREA", headers, results, column_widths)
        except Exception as e:
            print(f"Error fetching crime type statistics by area: {e}")


    #### AREA STATISTICS ####
    def statistics_by_area(self):
        try:
            cursor = self.connection.cursor()
            query = """
                SELECT Area, COUNT(*) as crimeCount
                FROM CrimesData
                GROUP BY Area
                ORDER BY crimeCount DESC
            """
            cursor.execute(query)
            results = cursor.fetchall()
            headers = ["Area", "Number of Crimes" ]
            column_widths = [15, 18]
            self.print_table_results(f"CRIME STATISTICS BY AREA", headers, results, column_widths)
        except Exception as e:
            print(f"Error fetching statistics by area: {e}")

    def crimes_by_area_premise(self):
        try:
            cursor = self.connection.cursor()
            query = """
                SELECT AreaDemographics.Area, Premise.Pdescription, COUNT(CrimesData.DR) AS crimeCount
                FROM CrimesData
                JOIN Premise ON CrimesData.premisCode = Premise.Pcode
                JOIN AreaDemographics ON CrimesData.Area = AreaDemographics.Area
                GROUP BY AreaDemographics.Area, Premise.Pdescription
                ORDER BY crimeCount DESC;
            """
            cursor.execute(query)
            results = cursor.fetchall()
            headers = ["Area", "Premise Type", "Number of Crimes" ]
            column_widths = [15, 70, 18]
            self.print_table_results(f"CRIMES BY AREA AND PREMISE", headers, results, column_widths)
        except Exception as e:
            print(f"Error fetching crimes by area and premise: {e}")

    def most_criminal_areas(self):
        try:
            cursor = self.connection.cursor()
            query = """
                SELECT Area, COUNT(*) AS areaCount
                FROM CrimesData
                GROUP BY Area
                ORDER BY areaCount DESC
                LIMIT 10; 
            """
            cursor.execute(query)
            results = cursor.fetchall()
            headers = ["Area", "Number of Crimes" ]
            column_widths = [15, 18]
            self.print_table_results(f"MOST CRIMINAL AREAS", headers, results, column_widths)
        except Exception as e:
            print(f"Error fetching most criminal areas: {e}")

    def average_victim_age_by_area(self):
        try:
            cursor = self.connection.cursor()
            query = """
                SELECT Area, ROUND(AVG(victAge), 0) as averageVictimAge
                FROM CrimesData
                GROUP BY Area
                ORDER BY averageVictimAge ASC
            """
            cursor.execute(query)
            results = cursor.fetchall()
            headers = ["Area", "Average Victim Age" ]
            column_widths = [15, 19]
            self.print_table_results(f"AVERAGE VICTIM AGE BY AREA", headers, results, column_widths)
        except Exception as e:
            print(f"Error fetching average victim age by area: {e}")

    #### VICTIM STATISTICS ####
    def statistics_by_gender(self):
        try:
            cursor = self.connection.cursor()
            query = """
                SELECT victGender, COUNT(*) as crimeCount
                FROM CrimesData
                GROUP BY victGender
                ORDER BY crimeCount DESC
            """
            cursor.execute(query)
            results = cursor.fetchall()
            headers = ["Gender", "Number of Crimes" ]
            column_widths = [7, 19]
            self.print_table_results(f"CRIME STATISTICS BY GENDER", headers, results, column_widths)
        except Exception as e:
            print(f"Error fetching statistics by gender: {e}")

    def crime_counts_by_age(self):
        try:
            cursor = self.connection.cursor()
            query = """
                SELECT 
                    CASE 
                        WHEN victAge BETWEEN 0 AND 17 THEN '0-17'
                        WHEN victAge BETWEEN 18 AND 24 THEN '18-24'
                        WHEN victAge BETWEEN 25 AND 34 THEN '25-34'
                        WHEN victAge BETWEEN 35 AND 44 THEN '35-44'
                        WHEN victAge BETWEEN 45 AND 54 THEN '45-54'
                        WHEN victAge BETWEEN 55 AND 64 THEN '55-64'
                        ELSE '65+'
                    END AS AgeGroup,
                    COUNT(*) AS CrimeCount
                FROM CrimesData
                GROUP BY AgeGroup
            """
            cursor.execute(query)
            results = cursor.fetchall()
            headers = ["Age Group", "Number of Crimes" ]
            column_widths = [9, 19]
            self.print_table_results(f"CRIMES BY AGE GROUP", headers, results, column_widths)
        except Exception as e:
            print(f"Error fetching crime counts by age group: {e}")

    def top_crimes_reported_by_females(self):
        try:
            cursor = self.connection.cursor()
            query = """
                WITH CrimeCounts AS (
                SELECT AreaDemographics.Area, CrimesData.CRdescription AS CrimeType, COUNT(CrimesData.CRcode) AS CrimeCount, AreaDemographics.HouseholdsInPovertyPercent
                FROM CrimesData
                JOIN AreaDemographics ON CrimesData.Area = AreaDemographics.Area
                WHERE CrimesData.victGender = 'F'
                GROUP BY AreaDemographics.Area, CrimesData.CRdescription, AreaDemographics.HouseholdsInPovertyPercent
                ),
                TopCrimesByArea AS (
                    SELECT Area, MAX(CrimeCount) AS MaxCrimeCount
                    FROM CrimeCounts
                    GROUP BY Area
                )
                SELECT 
                    CrimeCounts.Area, 
                    CrimeCounts.CrimeType, 
                    CrimeCounts.CrimeCount, 
                    CrimeCounts.HouseholdsInPovertyPercent
                FROM CrimeCounts JOIN TopCrimesByArea ON CrimeCounts.Area = TopCrimesByArea.Area AND CrimeCounts.CrimeCount = TopCrimesByArea.MaxCrimeCount
                ORDER BY CrimeCounts.CrimeCount DESC;

            """
            cursor.execute(query)
            results = cursor.fetchall()
            headers = ["Area", "Crime Type", "Number of Crimes", "Poverty Rate" ]
            column_widths = [15, 60, 20, 15]
            self.print_table_results(f"TOP REPORTED CRIMES BY FEMALES", headers, results, column_widths)
        except Exception as e:
            print(f"Error fetching top crimes by females by crime type: {e}")

    def most_reported_crimes_by_race(self):
        try:
            cursor = self.connection.cursor()
            query = """
                WITH CrimeCounts AS (
                    SELECT victRace, CRdescription AS CrimeType, COUNT(*) AS crimeCount
                    FROM CrimesData
                    WHERE victRace IS NOT NULL
                    GROUP BY victRace, CRdescription
                ),
                MostReportedCrimes AS (
                    SELECT victRace, MAX(crimeCount) AS maxCrimeCount
                    FROM CrimeCounts
                    GROUP BY victRace
                )
                SELECT CrimeCounts.victRace, CrimeCounts.CrimeType, CrimeCounts.crimeCount
                FROM CrimeCounts
                JOIN MostReportedCrimes ON CrimeCounts.victRace = MostReportedCrimes.victRace AND CrimeCounts.crimeCount = MostReportedCrimes.maxCrimeCount
                ORDER BY CrimeCounts.victRace;
            """
            cursor.execute(query)
            results = cursor.fetchall()
            headers = ["Race", "Crime Type", "Number of Crimes" ]
            column_widths = [5, 60, 20]
            self.print_table_results(f"MOST REPORTED CRIMES BY RACE", headers, results, column_widths)
        except Exception as e:
            print(f"Error fetching most reported crimes by race: {e}")

    #### STATUS STATISTICS ####
    def statistics_by_status(self):
        try:
            cursor = self.connection.cursor()
            query = """
                SELECT statusCode, COUNT(*) as crimeCount
                FROM CrimesData
                GROUP BY statusCode
                ORDER BY crimeCount DESC
            """
            cursor.execute(query)
            results = cursor.fetchall()
            headers = ["Status", "Number of Crimes" ]
            column_widths = [7, 20]
            self.print_table_results(f"CRIME STATISTICS BY STATUS", headers, results, column_widths)
        except Exception as e:
            print(f"Error fetching statistics by status: {e}")

    def total_arrests_investigations(self):
        try:
            cursor = self.connection.cursor()
            query = """
                SELECT Area, 
                (SELECT COUNT(*) FROM CrimesData WHERE statusCode = 'AA' AND CrimesData.Area = Areas.Area) AS TotalArrests,
                (SELECT COUNT(*) FROM CrimesData WHERE statusCode = 'IC' AND CrimesData.Area = Areas.Area) AS OpenInvestigations
                FROM (SELECT DISTINCT Area FROM CrimesData) AS Areas
                ORDER BY Area;
            """
            cursor.execute(query)
            results = cursor.fetchall()
            headers = ["Area", "Total Arrests", "Open Investigations" ]
            column_widths = [15, 15, 20]
            self.print_table_results(f"TOTAL ARRESTS AND OPEN INVESTIGATIONS", headers, results, column_widths)
        except Exception as e:
            print(f"Error fetching total arrests and open investigations by area: {e}")

    #### WEAPON STATISTICS ####
    def statistics_by_weapon(self):
        try:
            cursor = self.connection.cursor()
            query = """
                SELECT Weapon.Wdescription, COUNT(*) as crimeCount
                FROM CrimesData
                JOIN Weapon ON crimesData.weaponCode = Weapon.Wcode
                GROUP BY Weapon.Wdescription
                ORDER BY crimeCount DESC
            """
            cursor.execute(query)
            results = cursor.fetchall()

            headers = ["Weapon", "Number of Crimes" ]
            column_widths = [50, 20]
            self.print_table_results(f"CRIME STATISTICS BY WEAPON", headers, results, column_widths)
        except Exception as e:
            print(f"Error fetching statistics by weapon: {e}")

    def most_used_weapons(self):
        try:
            cursor = self.connection.cursor()
            query = """
                SELECT Wdescription AS Weapon, COUNT(*) AS WCount
                FROM CrimesData 
                JOIN Weapon ON CrimesData.weaponCode = Weapon.Wcode
                GROUP BY Wdescription
                ORDER BY WCount DESC
                LIMIT 10;
            """
            cursor.execute(query)
            results = cursor.fetchall()
            headers = ["Weapon", "Usage Count" ]
            column_widths = [30, 15]
            self.print_table_results(f"MOST USED WEAPONS", headers, results, column_widths)
        except Exception as e:
            print(f"Error fetching most used weapons: {e}")

    def total_crimes_with_without_weapons(self):
        try:
            cursor = self.connection.cursor()
            query = """
                SELECT 'Used' AS WeaponUse, COUNT(*) AS crimeCount
                FROM CrimesData
                WHERE weaponCode IS NOT NULL
                UNION ALL
                SELECT 'Not Used' AS WeaponUse, COUNT(*) AS crimeCount
                FROM CrimesData
                WHERE weaponCode IS NULL;
            """
            cursor.execute(query)
            results = cursor.fetchall()
            headers = ["Weapon", "Number Of Crimes" ]
            column_widths = [10, 20]
            self.print_table_results(f"TOTAL CRIMES WITH OR WITHOUT WEAPONS", headers, results, column_widths)
        except Exception as e:
            print(f"Error fetching total crimes by weapon usage: {e}")

    def crimes_by_weapon_status(self):
        try:
            cursor = self.connection.cursor()
            query = """
                SELECT Weapon.Wdescription AS Weapon,
                    (SELECT COUNT(*) FROM CrimesData WHERE statusCode = 'AA' AND CrimesData.weaponCode = Weapon.Wcode) AS TotalArrests,
                    (SELECT COUNT(*) FROM CrimesData WHERE statusCode = 'IC' AND CrimesData.weaponCode = Weapon.Wcode) AS OpenInvestigations
                FROM (SELECT DISTINCT weaponCode FROM CrimesData) AS Weapons
                LEFT JOIN Weapon ON Weapons.weaponCode = Weapon.Wcode
                ORDER BY Weapon.Wdescription;
            """
            cursor.execute(query)
            results = cursor.fetchall()
            headers = ["Weapon", "Total Arrests", "Open Investigations" ]
            column_widths = [50, 20, 20]
            self.print_table_results(f"CRIMES BY WEAPON (ARRESTS & INVESTIGATIONS)", headers, results, column_widths)
        except Exception as e:
            print(f"Error fetching crimes by weapon status: {e}")

    def most_used_weapon_by_area(self):
        try:
            cursor = self.connection.cursor()
            query = """
                WITH WeaponCounts AS (
                    SELECT Area, Weapon.Wdescription AS Weapon, COUNT(*) AS useCount
                    FROM CrimesData
                    JOIN Weapon ON CrimesData.weaponCode = Weapon.Wcode
                    GROUP BY Area, Weapon.Wdescription
                ),
                MostUsedWeaponByArea AS (
                    SELECT Area, Weapon, MAX(useCount) AS maxUse
                    FROM WeaponCounts
                    GROUP BY Area
                )
                SELECT WeaponCounts.Area, WeaponCounts.Weapon, WeaponCounts.useCount
                FROM WeaponCounts
                JOIN MostUsedWeaponByArea ON WeaponCounts.Area = MostUsedWeaponByArea.Area AND WeaponCounts.useCount = MostUsedWeaponByArea.maxUse
                ORDER BY WeaponCounts.Area;
            """
            cursor.execute(query)
            results = cursor.fetchall()
            headers = ["Area", "Weapon", "Usage Count" ]
            column_widths = [18, 50, 10]
            self.print_table_results(f"MOST USED WEAPON BY AREA", headers, results, column_widths)
        except Exception as e:
            print(f"Error fetching most used weapon by area: {e}")

    def most_used_weapons_by_poverty_rate(self):
        try:
            cursor = self.connection.cursor()
            query = """
                WITH weaponsCountPerArea AS (
                    SELECT Area, weaponCode, COUNT(weaponCode) AS weaponCount
                    FROM CrimesData
                    GROUP BY Area, weaponCode
                ),
                PopularWeaponsPerArea AS (
                    SELECT Area, Weapon.Wdescription, MAX(weaponCount) AS mostUsedWeaponPerArea
                    FROM weaponsCountPerArea
                    INNER JOIN Weapon ON weaponsCountPerArea.weaponCode = Weapon.Wcode
                    GROUP BY Area, Weapon.Wdescription
                )
                SELECT Area, Wdescription, mostUsedWeaponPerArea, HouseholdsInPovertyPercent
                FROM PopularWeaponsPerArea
                INNER JOIN AreaDemographics
                ON PopularWeaponsPerArea.Area = AreaDemographics.Area
                ORDER BY HouseholdsInPovertyPercent;
            """
            cursor.execute(query)
            results = cursor.fetchall()
            headers = ["Area", "Most Used Weapon", "Frequency", "Poverty Rate (%)" ]
            column_widths = [18, 50, 10, 20]
            self.print_table_results(f"MOST USED WEAPONS BY AREA AND POVERTY RATE", headers, results, column_widths)
        except Exception as e:
            print(f"Error fetching most used weapons by poverty rate: {e}")

    def most_frequent_crimes_by_poverty_rate(self):
        try:
            cursor = self.connection.cursor()
            query = """
                WITH 
                CrimeDescrCount AS (
                    SELECT CrimesData.Area, CRdescription, COUNT(CRdescription) AS crimeFrequency
                    FROM CrimesData
                    GROUP BY CrimesData.Area, CRdescription
                    ORDER BY crimeFrequency DESC
                ),
                MostFrequentCrime AS (
                    SELECT CrimeDescrCount.Area, CRdescription, MAX(crimeFrequency) AS maxFrequency
                    FROM CrimeDescrCount
                    GROUP BY CrimeDescrCount.Area, CRdescription
                )
                SELECT MostFrequentCrime.Area, CRdescription, maxFrequency, HouseholdsInPovertyPercent
                FROM MostFrequentCrime
                LEFT JOIN AreaDemographics ON MostFrequentCrime.Area = AreaDemographics.Area
                ORDER BY HouseholdsInPovertyPercent DESC;
            """
            cursor.execute(query)
            results = cursor.fetchall()
            headers = ["Area", "Most Frequent Crime", "Frequency", "Poverty Rate (%)" ]
            column_widths = [18, 60, 20, 20]
            self.print_table_results(f"MOST FREQUENT CRIMES BY AREA AND POVERTY RATE", headers, results, column_widths)
        except Exception as e:
            print(f"Error fetching most frequent crimes by poverty rate: {e}")

    def time_range_statistics(self):
        try:
            cursor = self.connection.cursor()
            query = """
                SELECT Area, 'Morning' AS timeRange, COUNT(*) AS crimeCount
                FROM CrimesData
                WHERE timeOccured >= '0600' AND timeOccured < '1200'
                GROUP BY Area
                UNION ALL
                SELECT Area, 'Afternoon' AS timeRange, COUNT(*) AS crimeCount
                FROM CrimesData
                WHERE timeOccured >= '1200' AND timeOccured < '1800'
                GROUP BY Area
                UNION ALL
                SELECT Area, 'Night' AS timeRange, COUNT(*) AS crimeCount
                FROM CrimesData
                WHERE timeOccured >= '1800' AND timeOccured <= '2400'
                GROUP BY Area
                ORDER BY Area, timeRange;
            """
            cursor.execute(query)
            results = cursor.fetchall()
            headers = ["Area", "Time Range", "Number of Crimes"]
            column_widths = [20, 15, 20]
            self.print_table_results(f"TIME RANGE STATISTICS", headers, results, column_widths)
        except Exception as e:
            print(f"Error fetching most frequent crimes by poverty rate: {e}")
    
    def crimes_in_homeowner_areas(self):
        try:
            cursor = self.connection.cursor()
            query = """
                SELECT Area, CRdescription, HouseholdsInPovertyPercent
                FROM CrimesData
                NATURAL JOIN AreaDemographics
                WHERE Area IN (
                    SELECT Area
                    FROM AreaDemographics
                    WHERE owner_occ > renter_occ
                )
                GROUP BY Area
            """
            cursor.execute(query)
            results = cursor.fetchall()
            headers = ["Area", "Crime Type", "Poverty Rate (%)" ]
            column_widths = [18, 60, 20]
            self.print_table_results(f"CRIMES IN AREAS WITH MORE HOMEOWNERS THAN RENTERS", headers, results, column_widths)
        except Exception as e:
            print(f"Error fetching crimes in homeowner-dominated areas: {e}")
    

    def victim_age_distribution(self):
        try:
            cursor = self.connection.cursor()
            query = """
                SELECT Area, ROUND(AVG(victAge), 0) AS averageAge, ROUND(MIN(victAge), 0) AS youngestVictim, ROUND(MAX(victAge), 0) AS oldestVictim 
                FROM CrimesData  
                GROUP BY Area
                ORDER BY averageAge ASC;
            """
            cursor.execute(query)
            results = cursor.fetchall()

            headers = ["Area","Average Victim Age", "Youngest Victim Age", "Oldest Victim Age"]
            column_widths = [20, 20, 20, 20]
            self.print_table_results(f"VICTIM AGE DISTRIBUTION", headers, results, column_widths)
        except Exception as e:
            print(f"Error fetching victim age distribution: {e}")

    #### SEARCH MENU ####

    def search_by_area(self, area):
        try:
            cursor = self.connection.cursor()
            query = """
                SELECT DR, CRdescription, premisCode, weaponCode, dateOccured, dateReported, timeOccured, statusCode 
                FROM CrimesData
                WHERE Area = ?;
            """
            cursor.execute(query, (area,))
            results = cursor.fetchall()
            headers = ["Case Number","Crime Type", "Premise Code", "Weapon Code", "Date Occured", "Date Reported", "Time", "Status"]
            column_widths = [15, 60, 12, 12, 15, 15, 10, 10]
            self.print_table_results(f"Crimes in Area: {area}", headers, results, column_widths)
        except Exception as e:
            print(f"Error searching by area: {e}")

    def search_by_premise(self, premise_code):
        try:
            cursor = self.connection.cursor()
            query = """
                SELECT DR, CrimesData.Area, CRdescription, weaponCode, dateOccured, dateReported, timeOccured, statusCode
                FROM CrimesData
                WHERE premisCode = ?;
            """
            cursor.execute(query, (premise_code,))
            results = cursor.fetchall()

            headers = ["Case Number", "Area", "Crime Type", "Weapon Code", "Date Occured", "Date Reported", "Time", "Status"]
            column_widths = [15, 15, 60, 12, 15, 15, 10, 10]
            self.print_table_results(f"Crimes in Premise Code: {premise_code}", headers, results, column_widths)
            input("Press Enter to return to the Search Menu...")
        except Exception as e:
            print(f"Error searching by premise: {e}")

    def search_by_poverty_rate(self, poverty_rate):
        try:
            cursor = self.connection.cursor()
            query = """
                SELECT DR, CrimesData.Area, CRdescription, premisCode, weaponCode, dateOccured, dateReported, timeOccured, statusCode
                FROM CrimesData
                LEFT JOIN AreaDemographics ON CrimesData.Area = AreaDemographics.Area
                WHERE AreaDemographics.HouseholdsInPovertyPercent >= ?;
            """
            cursor.execute(query, (poverty_rate,))
            results = cursor.fetchall()

            headers = ["Case Number", "Area", "Crime Type", "Premise Code", "Weapon Code", "Date Occured", "Date Reported", "Time", "Status"]
            column_widths = [15, 15, 60, 12, 12, 15, 15, 10, 10]
            self.print_table_results(f"Crimes in areas with poverty rate >= {poverty_rate}%:", headers, results, column_widths)
        except Exception as e:
            print(f"Error searching by poverty rate: {e}")


    def search_by_demographics(self, population):
        try:
            cursor = self.connection.cursor()
            query = """
                SELECT DR, CrimesData.Area, CRdescription, premisCode, weaponCode, dateOccured, dateReported, timeOccured, statusCode
                FROM CrimesData
                LEFT JOIN AreaDemographics ON CrimesData.Area = AreaDemographics.Area
                WHERE AreaDemographics.population <= ?;
            """
            cursor.execute(query, (population,))
            results = cursor.fetchall()
            headers = ["Case Number", "Area", "Crime Type", "Premise Code", "Weapon Code", "Date Occured", "Date Reported", "Time", "Status"]
            column_widths = [15, 15, 60, 12, 12, 15, 15, 10, 10]
            self.print_table_results(f"Crimes for Demographics with Population: {population}", headers, results, column_widths)
        except Exception as e:
            print(f"Error searching by demographics: {e}")

    def search_by_status(self, status_code):
        try:
            cursor = self.connection.cursor()
            query = """
                SELECT DR, CrimesData.Area, CRdescription, premisCode, weaponCode, dateOccured, dateReported, timeOccured
                FROM CrimesData
                WHERE statusCode = ?;
            """
            cursor.execute(query, (status_code,))
            results = cursor.fetchall()

            headers = ["Case Number", "Area", "Crime Type", "Premise Code", "Weapon Code", "Date Occured", "Date Reported", "Time"]
            column_widths = [15, 15, 60, 12, 12, 15, 15, 10]
            self.print_table_results(f"Crimes with Status Code: {status_code}", headers, results, column_widths)
        except Exception as e:
            print(f"Error searching by status: {e}")

    def search_by_crime_type(self, crime_code):
        try:
            cursor = self.connection.cursor()
            query = """
                SELECT DR, CrimesData.Area, premisCode, weaponCode, dateOccured, dateReported, timeOccured, statusCode
                FROM CrimesData
                WHERE CRcode = ?;
            """
            cursor.execute(query, (crime_code,))
            results = cursor.fetchall()
            headers = ["Case Number", "Area", "Premise Code", "Weapon Code", "Date Occured", "Date Reported", "Time", "Status"]
            column_widths = [15, 15, 12, 12, 15, 15, 10, 10]
            self.print_table_results(f"Crimes with Crime Code: {crime_code}", headers, results, column_widths)
        except Exception as e:
            print(f"Error searching by crime type: {e}")

    def search_by_weapon(self, weapon_code):
        try:
            cursor = self.connection.cursor()
            query = """
                SELECT DR, Area, CRdescription, premisCode, dateOccured, dateReported, timeOccured, statusCode
                FROM CrimesData
                WHERE weaponCode = ?;
            """
            cursor.execute(query, (weapon_code,))
            results = cursor.fetchall()
            headers = ["Case Number", "Area", "Crime Type", "Premise Code", "Date Occured", "Date Reported", "Time", "Status"]
            column_widths = [15, 15, 60, 12, 15, 15, 10, 10]
            self.print_table_results(f"Crimes involving Weapon Code: {weapon_code}", headers, results, column_widths)
        except Exception as e:
            print(f"Error searching by weapon: {e}")

    def search_by_time_range(self, time_range):
        try:
            cursor = self.connection.cursor()
            query = """
                SELECT DR, Area, CRdescription, premisCode, weaponCode, dateOccured, dateReported, timeOccured, statusCode
                FROM CrimesData
                WHERE 
                (? = 'morning' AND timeOccured >= '0600' AND timeOccured < '1200') OR
                (? = 'afternoon' AND timeOccured >= '1200' AND timeOccured < '1800') OR
                (? = 'night' AND timeOccured >= '1800' AND timeOccured <= '2400');
            """
            cursor.execute(query, (time_range, time_range, time_range))
            results = cursor.fetchall()
            headers = ["Case Number", "Area", "Crime Type", "Premise Code", "Weapon Code", "Date Occured", "Date Reported", "Time", "Status"]
            column_widths = [15, 15, 60, 12, 12, 12, 15, 15, 10, 10]
            self.print_table_results(f"Crimes during Time Range: {time_range}", headers, results, column_widths)
        except Exception as e:
            print(f"Error searching by time range: {e}")


    def crime_history_in_area(self, area):
        try:
            cursor = self.connection.cursor()
            query = """
                SELECT CRdescription,  COUNT(*) AS crimeFrequency,  MAX(dateOccured) AS mostRecentIncident,  MIN(dateOccured) AS oldestIncident  
                FROM CrimesData  
                WHERE Area = ?  
                GROUP BY CRdescription  
                ORDER BY crimeFrequency DESC;
            """
            cursor.execute(query, (area,))
            results = cursor.fetchall()
            headers = ["Crime Type", "Frequency", "Most Recent Incident", "Oldest Incident"]
            column_widths = [60, 10, 20, 20]
            self.print_table_results(f"CRIME HISTORY IN AREA: {area}", headers, results, column_widths)
        except Exception as e:
            print(f"Error fetching crime history for area {area}: {e}")

    

    def victim_age_in_area(self, area):
        try:
            cursor = self.connection.cursor()
            query = """
                SELECT ROUND(AVG(victAge), 0) AS averageAge, 
                     ROUND(MIN(victAge), 0) AS youngestVictim, 
                     ROUND(MAX(victAge), 0) AS oldestVictim 
                FROM CrimesData  
                WHERE Area = ?;
            """
            cursor.execute(query, (area,))
            result = cursor.fetchone()
            headers = ["Average Victim Age", "Youngest Victim Age", "Oldest Victim Age"]
            column_widths = [20, 20, 20]
            self.print_table_results(f"VICTIM AGE DISTRIBUTION FOR AREA: {area}", headers, [result], column_widths)
        except Exception as e:
            print(f"Error fetching victim age distribution for area {area}: {e}")

    

# WEAPON COMMANDS 
    def add_weapon(self, wcode, wdescription):
        try:
            with self.connection:
                self.connection.execute("""
                    INSERT INTO Weapon (Wcode, Wdescription) VALUES (?, ?)
                """, (wcode, wdescription))
            print("Weapon added successfully.")

        except sqlite3.IntegrityError:
            print("Error: Weapon code already exists.")

    def update_weapon(self, wcode, new_description):
        cursor = self.connection.cursor()
        cursor.execute("""
            UPDATE Weapon SET Wdescription = ? WHERE Wcode = ?
        """, (new_description, wcode))
       
        if cursor.rowcount == 0:
            print("No weapon found with that code.")
        else:
            print("Weapon updated successfully.")

    def delete_weapon(self, wcode):
        cursor = self.connection.cursor()

        cursor.execute("""
            DELETE FROM Weapon WHERE Wcode = ?
        """, (wcode,))

        if cursor.rowcount == 0:
            print("No weapon found with that code.")
        else:
            print("Weapon deleted successfully.")

# AREA COMMANDS 
    def add_area(self, area, area_code, population, white_pop, black_pop, 
             indigenous_pop, asian_pop, hawaiian_pop, other_pop, multi_pop, 
             in_poverty, owner_occ, renter_occ, households_in_poverty, 
             households_in_poverty_percent):
        """Add a new area with demographics to the AreaDemographics table."""
        try:
            with self.connection:
                self.connection.execute("""
                    INSERT INTO AreaDemographics (
                        Area, areaCode, population, white_pop, black_pop, 
                        indigenous_pop, asian_pop, hawaiian_pop, other_pop, 
                        multi_pop, inPoverty, owner_occ, renter_occ, 
                        HouseholdsInPoverty, HouseholdsInPovertyPercent
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (area, area_code, population, white_pop, black_pop, indigenous_pop, 
                    asian_pop, hawaiian_pop, other_pop, multi_pop, in_poverty, 
                    owner_occ, renter_occ, households_in_poverty, households_in_poverty_percent))
            print("Area added successfully.")
        except sqlite3.IntegrityError:
            print("Error: Area or Area Code already exists.")

    def update_area(self, area, area_code, population, white_pop, black_pop, 
                indigenous_pop, asian_pop, hawaiian_pop, other_pop, multi_pop,
                in_poverty, owner_occ, renter_occ, households_in_poverty, 
                households_in_poverty_percent):
        """Update all attributes of an existing area except the name."""
        cursor = self.connection.cursor()

        cursor.execute("""
            UPDATE AreaDemographics 
            SET areaCode = ?, population = ?, white_pop = ?, black_pop = ?, 
                indigenous_pop = ?, asian_pop = ?, hawaiian_pop = ?, 
                other_pop = ?, multi_pop = ?, inPoverty = ?, owner_occ = ?, 
                renter_occ = ?, HouseholdsInPoverty = ?, 
                HouseholdsInPovertyPercent = ? 
            WHERE Area = ?
        """, (
            area_code, population, white_pop, black_pop, indigenous_pop,
            asian_pop, hawaiian_pop, other_pop, multi_pop, in_poverty, 
            owner_occ, renter_occ, households_in_poverty, 
            households_in_poverty_percent, area
        ))

        if cursor.rowcount == 0:
            print("No area found with that name.")
        else:
            print(f"Area '{area}' updated successfully.")

    def delete_area(self, area):
        cursor = self.connection.cursor()
        cursor.execute("""
            DELETE FROM AreaDemographics WHERE Area = ?
        """, (area,))

        if cursor.rowcount == 0:
            print("No area found with that name.")
        else:
            print("Area deleted successfully.")

    def close(self):
        self.connection.close()

if __name__ == "__main__":
    app = Database()
    app.print_all()  # Prints all tables: AreaDemographics, CrimesData, Premise, Status, Weapon
    app.close()
