## INTERNAL REVIEW

Before recieving feedback from others we conducted an internal review of the Gardening Application to go over any improvements necessary.

## Review 01

Original Code:

```python
def get_yes_no(prompt):
    """Prompt repeatedly for a yes/no answer and return 'yes' or 'no' (lowercase).
    """
    while True:
        response = input(prompt + " (yes/no): ").strip().lower()
        if response in ["yes", "no"]:
            return response
        else: print(Fore.RED + "Please enter 'yes' or 'no'. ")
```

Suggestions on improvement:

- UX: accept y/n as well as yes/no

```python
def get_yes_no(prompt):
    """Prompt repeatedly for yes/no; accept y/yes and n/no. Returns 'yes' or 'no'."""
    while True:
        response = input(f"{prompt} (y/n): ").strip().lower()
        if response in {"y", "yes"}:
            return "yes"
        if response in {"n", "no"}:
            return "no"
        print(Fore.RED + "Please enter y/yes or n/no.")
```

## Review 02

Original Code:

```python
# plant_seeds()
if seed_type in ["orange tree", "pumpkin"]:
    self.garden.plants.append(seed_type)
```

```python
# helper
def is_valid_seed(seed_type):
    return seed_type in ["orange tree", "pumpkin"]
```

Suggestions on improvement:

- Single source of truth for allowed seeds

```python
# module-level constant
ALLOWED_SEEDS = {"orange tree", "pumpkin"}

# use in plant_seeds()
if seed_type in ALLOWED_SEEDS:
    self.garden.plants.append(seed_type)

# use in helper
def is_valid_seed(seed_type: str) -> bool:
    return seed_type in ALLOWED_SEEDS
```

## Review 03

Original Code:

```python
def calculate_growth(days):
    return days * 2
```

Suggestions on improvement:

- calculate_growth is not referenced by app or current tests so it should be removed for clarity.

## Review 04 - Simona 

### Original Code 

```python
def fertilize(self):
        if get_yes_no("Fertilize the soil?") == "yes":
            print(Fore.MAGENTA + "Your plants are ready to be picked!")
        else:
            print(Fore.YELLOW + "Your plants need fertilizer soon!")
```

Suggestions on improvement:

- The function could include a short "action line" before the feedback message and an outcome message.
- Adding a line break (\n) makes the output easier to read in the terminal when actions are performed repeatedly.

```python
def fertilize(self):
    if get_yes_no("Fertilize the soil?") == "yes":
        print(Fore.MAGENTA + "\nFertilising the soil...")
        print(Fore.GREEN + "Your plants are growing stronger!")
    else:
        print(Fore.YELLOW + "Don’t forget to fertilise soon!")
```





