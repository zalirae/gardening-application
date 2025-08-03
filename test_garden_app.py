from gardening_app import Garden, is_valid_seed

def test_is_valid_seed():
    assert is_valid_seed("orange tree")
    assert is_valid_seed("pumpkin")
    assert not is_valid_seed("apple")
    assert not is_valid_seed("")
    print("test_is_valid_seed passed.")

def test_garden_initial_plants():
    g = Garden()
    assert "tomatoes" in g.plants
    assert "tulips" in g.plants
    print("test_garden_initial_plants passed.")

def test_garden_plant_addition():
    g = Garden()
    g.plants.append("pumpkin")
    assert "pumpkin" in g.plants
    print("test_garden_plant_addition passed.")

# Run tests
test_is_valid_seed()
test_garden_initial_plants()
test_garden_plant_addition()

print("All tests passed.")