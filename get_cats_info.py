def get_cats_info(path:str):

	cats_info = []

	try:
		with open(path, encoding="utf-8") as file:
			for line in file:
				parts = line.strip().split(",")
				if len(parts) == 3:

					cat = {"id": parts[0], "name": parts[1], "age": parts[2]}
					cats_info.append(cat)

				else:
					print(f"Введено неправильний формат даних в строці: {line}")

	except FileNotFoundError:
		print("Файл не знайдено.")

	except (IOError) as msg:
		print(f"При обробці файлу сталася помилка: {msg}")
	
	except ValueError:
		print(f"Виникла помилка: {line.strip()} було пропущено")

	except Exception as e:
		print(f"Виникла помилка {e}")

	return cats_info

cats_info = get_cats_info("C:\\my_repo\\goit-pycore-hw-04\\cats_file.txt")
print (cats_info)
