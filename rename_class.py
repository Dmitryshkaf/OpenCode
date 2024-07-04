import os

# Директория с текстовыми файлами
directory = 'data/valid/labels'

# Функция для замены текста в файле
def replace_class_in_file(file_path, replacements):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # Замена имени класса в каждой строке
    with open(file_path, 'w', encoding='utf-8') as file:
        for line in lines:
            for old_class, new_class in replacements.items():
                if line.startswith(old_class):
                    line = line.replace(old_class, new_class, 1)
            file.write(line)

# Замены, которые нужно сделать
replacements = {
    'helmet': '0',
    'head': '1'
}

# Итерирование по файлам в директории
for filename in os.listdir(directory):
    if filename.endswith('.txt'):  # Проверка, что это текстовый файл
        file_path = os.path.join(directory, filename)
        replace_class_in_file(file_path, replacements)
        print(f"Замены в файле {filename} выполнены.")

print("Все замены выполнены.")
