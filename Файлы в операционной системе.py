import os
import time

# Указываем путь к директории, которую нужно обойти
path = (r'C:\Users\Home\PycharmProjects\pythonProject\седьмой модуль')

# Используем os.walk() для обхода директории
for root, dirs, files in os.walk(path):
    # root - текущий путь к директории
    # dirs - список подкаталогов в текущем каталоге
    # files - список файлов в текущем каталоге

    print(f'Текущая директория: {root}')
    print(f'Подкаталоги: {dirs}')
    print(f'Файлы: {files}')
    print('-' * 70)


for file in files:
    full_file_path = os.path.join(root, file)
    print(f'Полный путь к файлу: {full_file_path}')
print('-' * 70)


last_modified_time = os.path.getmtime(full_file_path)
# Преобразуем время из timestamp в читаемый формат
readable_time = time.ctime(last_modified_time)
print(f'Время последнего изменения: {readable_time}')
print('-' * 70)


print('Размер файла: ', os.path.getsize(full_file_path))
print('-' * 70)

print( 'Родительская директория: ',os.path.dirname(full_file_path))
print('-' * 70)




