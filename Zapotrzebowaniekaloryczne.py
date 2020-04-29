user_sex = input("Jesteś mężyczyzną, czy kobietą? (M/K)")
if user_sex == "M":
    ratio = 5
else:
    ratio = -151
user_age = int(input("\nIle masz lat?"))
user_height = int(input("\nIle masz wzrostu?"))
user_weight = int(input("\nIle ważysz?"))
multiplier = int
user_activity = input("\nWybierz swoją aktywność fizyczną:"
                    "\n1. Praca siedząca, brak dodatkowej aktywności fizycznej"
                    "\n2. Praca niefizyczna, mało aktywny tryb życia"
                    "\n3. Lekka praca fizyczna,  regularne ćwiczenia 3-4 razy (ok. 5h) w tygodniu"
                    "\n4. Praca fizyczna, regularne ćwiczenia od 5razy (ok. 7h) w tygodniu"
                    "\n5. Praca fizyczna ciężka, regularne ćwiczenia 7razy w tygodniu")
if user_activity == 1:
    multiplier = 1.2
elif user_activity == 2:
    multiplier = 1.4
elif user_activity == 3:
    multiplier = 1.6
elif user_activity == 4:
    multiplier = 1.8
else:
    multiplier = 2
base = 10 * user_height + 6.25 * user_height -5 * user_age + ratio
calories = base * multiplier
print("\nTwoje zapotrzebowanie kalorii to: " + str(calories) + "kcal")
