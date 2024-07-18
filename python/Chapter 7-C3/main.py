def has_enough_gas(gallons_in_car, miles_one_way, miles_per_gallon):
    gallons_needed = 2*(miles_one_way/miles_per_gallon)
    print(f"gallons_in_car: {gallons_in_car}")
    print(f"gallons_needed: {gallons_needed}")
    if gallons_needed <= gallons_in_car:
        return True
    return False