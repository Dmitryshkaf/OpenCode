import os

# Директория с текстовыми файлами аннотаций
directory = 'data/valid/labels'
# Директория с изображениями
images_directory = 'data/valid/images'

def get_image_size(image_path):
    from PIL import Image
    with Image.open(image_path) as img:
        return img.size

def convert_coordinates(file_path, image_size):
    new_lines = []
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split()
            if len(parts) != 5:
                print(f"Неверный формат строки: {line.strip()} в файле {file_path}")
                continue
            
            label, x1, y1, x2, y2 = parts
            x1, y1, x2, y2 = float(x1), float(y1), float(x2), float(y2)
            
            # Получение размеров изображения
            image_width, image_height = image_size
            
            # Вычисление центра и размеров bounding box
            x_center = (x1 + x2) / 2 / image_width
            y_center = (y1 + y2) / 2 / image_height
            width = (x2 - x1) / image_width
            height = (y2 - y1) / image_height
            
            new_lines.append(f"{label} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}")
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write('\n'.join(new_lines))

# Итерирование по файлам в директории
for filename in os.listdir(directory):
    if filename.endswith('.txt'):  # Проверка, что это текстовый файл
        file_path = os.path.join(directory, filename)
        # Предполагается, что имя изображения совпадает с именем файла аннотации
        image_path = os.path.join(images_directory, filename.replace('.txt', '.jpg'))
        if not os.path.exists(image_path):
            image_path = image_path.replace('.jpg', '.png')
        
        if os.path.exists(image_path):
            image_size = get_image_size(image_path)
            convert_coordinates(file_path, image_size)
            print(f"Обработан файл {filename}")
        else:
            print(f"Изображение для {filename} не найдено")

print("Все замены выполнены.")
