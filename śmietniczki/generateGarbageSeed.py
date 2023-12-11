import random
from datetime import datetime, timedelta

# Funkcja do generowania losowej daty w zakresie od 1 stycznia 2022 do 31 grudnia 2024
def generate_random_date():
    start_date = datetime(2022, 1, 1)
    end_date = datetime(2024, 12, 31)
    random_date = start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))
    return random_date.strftime('%Y-%m-%d %H:%M:%S')

# Funkcja do generowania danych
def generate_garbage_data(user_id, bin_id, num_entries):
    data = []
    for i in range(1, num_entries + 1):
        waste_type = random.randint(11, 15)
        weight = random.randint(50, 1000)
        date = generate_random_date()
        entry = [i, user_id, bin_id, waste_type, weight, date]
        data.append(entry)
    return data

# Funkcja do zapisu danych do pliku
def save_to_file(data, file_name):
    with open(file_name, 'w') as file:
        file.write("const garbageData = [\n")
        for entry in data:
            file.write(f"  {entry},\n")
        file.write("]\n")

# Main
file_name = 'garbage.js'

# Generuj 10 rekordów dla użytkowników o id 4, 14, 15 (z id śmietnika równym 4)
garbage_data_1 = generate_garbage_data(4, 4, 10)
garbage_data_2 = generate_garbage_data(14, 4, 10)
garbage_data_3 = generate_garbage_data(15, 4, 10)

# Generuj 10 rekordów dla użytkowników o id 8 (z id śmietnika równym 6)
garbage_data_4 = generate_garbage_data(8, 6, 10)

# Połącz dane dla wszystkich użytkowników
all_garbage_data = garbage_data_1 + garbage_data_2 + garbage_data_3 + garbage_data_4

# Zapisz dane do pliku
save_to_file(all_garbage_data, file_name)

print("Plik został wygenerowany.")
