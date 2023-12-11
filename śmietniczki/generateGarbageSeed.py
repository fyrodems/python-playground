import random
from datetime import datetime, timedelta
from tkinter import filedialog
import tkinter as tk

# Stała konfiguracyjna
CONFIG = {
    'user_ids': [4, 14, 15, 8],
    'dumpster_id_1': 4,
    'dumpster_id_2': 6,
    'entries_per_user': 10000,
}

# Funkcja do generowania losowej daty w zakresie od 1 stycznia 2022 do 31 grudnia 2024
def generate_random_date():
    start_date = datetime(2022, 1, 1)
    end_date = datetime(2024, 12, 31)
    random_date = start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))
    return random_date.strftime('%Y-%m-%d %H:%M:%S')

# Funkcja do generowania danych
def generate_garbage_data(user_id, bin_id, start_index, num_entries):
    data = []
    for i in range(start_index, start_index + num_entries):
        waste_type = random.randint(11, 15)
        weight = random.randint(50, 1000)
        date = generate_random_date()
        entry = [i, user_id, bin_id, waste_type, weight, date]
        data.append(entry)
    return data

# Funkcja do zapisu danych do pliku
def save_to_file(data, file_path):
    with open(file_path, 'a') as file:  # Zmieniono 'w' na 'a' (append), aby kontynuować zapis do istniejącego pliku
        for entry in data:
            file.write(f"  {entry},\n")

# Funkcja do obsługi okna dialogowego
def get_file_path():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.asksaveasfilename(defaultextension=".js", filetypes=[("JavaScript files", "*.js")])
    root.destroy()
    return file_path

# Main
# Pobierz ścieżkę pliku za pomocą okna dialogowego
file_path = get_file_path()

# Sprawdź, czy użytkownik wybrał lokalizację
if file_path:
    # Generuj dane dla użytkowników zgodnie z konfiguracją
    all_garbage_data = []
    start_index = 1

    for user_id in CONFIG['user_ids']:
        bin_id = CONFIG['dumpster_id_1'] if user_id != 8 else CONFIG['dumpster_id_2']
        user_data = generate_garbage_data(user_id, bin_id, start_index, CONFIG['entries_per_user'])
        all_garbage_data.extend(user_data)
        start_index += CONFIG['entries_per_user']

    # Zapisz dane do pliku
    save_to_file(all_garbage_data, file_path)

    print(f"Plik został zapisany w lokalizacji: {file_path}")
else:
    print("Anulowano zapisywanie pliku.")
