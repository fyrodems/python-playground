import random
from datetime import datetime, timedelta

# Stała konfiguracyjna
CONFIG = {
    'user_ids': [4, 14, 15, 8],
    'dumpster_id_1': 4,
    'dumpster_id_2': 6,
    'entries_per_user': 10,
}

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

        # Dodaj strukturę createList na koniec pliku
        file.write("\nconst createList = (list) => {\n")
        file.write("  return list.map((g) => ({\n")
        file.write("    garbage_ID: g[0],\n")
        file.write("    garbage_usersID: g[1],\n")
        file.write("    garbage_dumpsterID: g[2],\n")
        file.write("    garbage_typeID: g[3],\n")
        file.write("    garbage_weight: g[4],\n")
        file.write("    garbage_date: new Date(g[5]),\n")
        file.write("  }))\n")
        file.write("\nexport default createList(garbageData)")

# Main
file_name = 'garbage.js'

# Generuj dane dla użytkowników zgodnie z konfiguracją
all_garbage_data = []
for user_id in CONFIG['user_ids']:
    bin_id = CONFIG['dumpster_id_1'] if user_id != 8 else CONFIG['dumpster_id_2']
    user_data = generate_garbage_data(user_id, bin_id, CONFIG['entries_per_user'])
    all_garbage_data.extend(user_data)

# Zapisz dane do pliku
save_to_file(all_garbage_data, file_name)

print("Plik został wygenerowany.")
