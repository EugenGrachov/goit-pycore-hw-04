def get_cats_info(path:str):

	cats_info = []

	try:
		with open(path, encoding="utf-8") as file:
			for line in file:
				parts = line.strip().split(",")
				if len(parts) == 3:

					cat_info = {"id": parts[0], "name": parts[1], "age": parts[2]}
					cats_info.append(cat_info)
				
				# else:
				# 	print(f"Неправильний формат даних в строці: {line}")

	except FileNotFoundError:
		raise FileNotFoundError("Файл не знайдено.")
	
	except (IOError, ValueError) as msg:
		raise IOError(f"При обробці файлу сталася помилка: {msg}")
	
	return cats_info

cats_info = get_cats_info("C:\\my_repo\\goit-pycore-hw-04\\cats_file.txt")
print(cats_info)
