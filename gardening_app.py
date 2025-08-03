'''Import providing a function for coloured terminal text'''
import json
from colorama import init, Fore
import questionary

init (autoreset=True)


#File to save Garden State
GARDEN_FILE = "garden_data.json"


'''Helper function to get yes/no'''
def get_yes_no(prompt):
    while True:
        response = input(prompt + " (yes/no): ").strip().lower()
        if response in ["yes", "no"]:
            return response
        else: print(Fore.RED + "Please enter 'yes' or 'no'. ")



class Garden:
    '''Class representing the garden'''
     def __init__(self, plants=None):
        self.plants = plants if plants else ["tomatoes", "snow peas", "marigolds",
                                             "nasturtiums", "tulips"]
    def display_plants(self):
        print(Fore.GREEN + "\nYour garden has the following plants:")
        for plant in self.plants:
            print(f"- {plant}")

     def save_garden(self):
        try:
            with open(GARDEN_FILE, 'w', encoding="utf-8") as f:
                json.dump({"plants": self.plants}, f)
        except Exception as e:
            print(Fore.RED + f"Error saving your garden: {e}")

    def load_garden(self):
        try:
            with open(GARDEN_FILE, 'r', encoding="utf-8") as f:
                data = json.load(f)
                self.plants = data.get("plants", [])
                print(Fore.CYAN + "Garden loaded successfully!")
        except FileNotFoundError:
            print(Fore.YELLOW + "No saved garden found, starting a new garden.")
  

class GardenActions:
    '''Class representing the garden actions'''
   

# Main Game Function
def main():
  

# Run program
if __name__ == "__main__":
    main()

# Testing 
