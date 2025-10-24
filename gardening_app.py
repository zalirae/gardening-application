"""Gardening App

A simple, text-based terminal app where users can view plants, water the garden, fertilise the soil, plant seeds, and save or load their garden using garden_data.json.

Persistence:
    - Garden data is stored locally in a JSON file named `garden_data.json`.

Key dependencies (runtime):
    - colorama: coloured terminal output for clearer feedback.
    - questionary: interactive command-line prompts and menus.
"""
import json
from colorama import init, Fore
import questionary

# Initialise Colorama so terminal colours reset automatically after each print.
init(autoreset=True)

# File path used to persist the garden between runs.
GARDEN_FILE = "garden_data.json"

def get_yes_no(prompt):
    """Prompt repeatedly for a yes/no answer and return 'yes' or 'no' (lowercase).
    """
    while True:
        response = input(prompt + " (yes/no): ").strip().lower()
        if response in ["yes", "no"]:
            return response
        else: print(Fore.RED + "Please enter 'yes' or 'no'. ")


class Garden:
    """Model for the user’s garden (list of plant names)."""
    def __init__(self, plants=None):
        """Create a garden with an optional starting list of plants."""
        self.plants = plants if plants else ["tomatoes", "snow peas", "marigolds",
                                             "nasturtiums", "tulips"]
    def display_plants(self):
        """Show all plants currently in the garden."""
        print(Fore.GREEN + "\nYour garden has the following plants:")
        for plant in self.plants:
            print(f"- {plant}")

    def save_garden(self):
        """Save the current garden to garden_data.json, replacing any existing file."""
        try:
            with open(GARDEN_FILE, 'w', encoding="utf-8") as f:
                json.dump({"plants": self.plants}, f)
        except Exception as e:
            print(Fore.RED + f"Error saving your garden: {e}")

    def load_garden(self):
        """Load the garden from garden_data.json if it exists; otherwise start a new garden."""
        try:
            with open(GARDEN_FILE, 'r', encoding="utf-8") as f:
                data = json.load(f)
                self.plants = data.get("plants", [])
                print(Fore.CYAN + "Garden loaded successfully!")
        except FileNotFoundError:
            print(Fore.YELLOW + "No saved garden found, starting a new garden.")
  

class GardenActions:
    """User actions that operate on a Garden instance.

    Keeps the “data” (Garden) separate from the “interaction” (prompts/prints),
    which makes responsibilities clearer and easier to extend later.
    """
    def __init__(self, garden: Garden):
        self.garden = garden

    def water(self):
        """Offer to water the garden and print a simple outcome message."""
        if get_yes_no("Water your garden?") == "yes":
            print(Fore.BLUE + "Your plants are growing!")
        else:
            print(Fore.YELLOW + "The sun is out, your plants need water!")

    def fertilize(self):
        """Offer to fertilise the soil and print the outcome.

        Note:
            The line “Your plants are ready to be picked!” is flavour text only.
            There’s no dedicated “harvest/pick” mechanic implemented yet.
        """
        if get_yes_no("Fertilize the soil?") == "yes":
            print(Fore.MAGENTA + "Your plants are ready to be picked!")
        else:
            print(Fore.YELLOW + "Your plants need fertilizer soon!")

    def plant_seeds(self):
        """Ask to plant seeds; allow only 'orange tree' or 'pumpkin' for simplicity.

        Includes a follow-up prompt to water the seeds for a bit of feedback/flow.
        """
        if get_yes_no("Plant seeds?") == "yes":
            seed_type = input("Plant 'orange tree' or 'pumpkin'? ").strip().lower()
            if seed_type in ["orange tree", "pumpkin"]:
                self.garden.plants.append(seed_type)
                if get_yes_no("Water your seeds?") == "yes":
                    print(Fore.GREEN + "Your seeds are sprouting!")
                else:
                    print(Fore.RED + "Your seeds need water!")
            else:
                print(Fore.RED + "Invalid seed type.")
        else:
            print(Fore.RED + "Maybe later then.")


# Main Game Function
def main():
    """Create objects, attempt to load saved state, then run the main menu loop."""
    garden = Garden()
    actions = GardenActions(garden)

    garden.load_garden()

    # Map menu labels (exactly as displayed) to the corresponding callables.
    function_map = {
            "Show Garden": garden.display_plants,
            "Water Garden": actions.water,
            "Fertilize Soil": actions.fertilize,
            "Plant Seeds": actions.plant_seeds,
            "Save Garden": garden.save_garden,
        }

    while True:
        # questionary provides a simple, accessible menu with arrow-key navigation.
        question = questionary.select(
            "What would you like to do?",
            choices=list(function_map.keys()) + ["Exit"]
        ).ask()

        if question == "Exit":
            print(Fore.CYAN + "Thanks for gardening, goodbye!")
            break

        if question:
            function_map[question]()

# Run program
if __name__ == "__main__":
    main()

# Helpers primarily for tests
def calculate_growth(days):
    return days * 2

def is_valid_seed(seed_type):
    return seed_type in ["orange tree", "pumpkin"]
