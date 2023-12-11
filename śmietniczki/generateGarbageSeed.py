import random
from datetime import datetime, timedelta
import os

# Funkcja do generowania losowej daty w zakresie od 1 stycznia 2022 do 31 grudnia 2024
def generate_random_date():
    start_date = datetime(2022, 1, 1)
    end_date = datetime(2024, 12, 31)
    random_date = start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))
    return random_date.strftime('%Y-%m-%d %H:%M:%S')

# Funkcja do generowania danych
def generate_garbage_data(num):
    data = []
    for i in range(1, num + 1):
        user_id = 4
        bin_id = 4
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
num_of_runs = 5  # Możesz zmienić tę liczbę na ilość plików, jaką chcesz wygenerować
for run in range(1, num_of_runs + 1):
    file_name = f'garbage-{run}.js'
    garbage_data = generate_garbage_data(10)  # Możesz zmienić tę liczbę na ilość wpisów w pliku
    save_to_file(garbage_data, file_name)

print(f"{num_of_runs} plik(i/ów) zostały wygenerowane.")
