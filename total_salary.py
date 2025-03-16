def total_salary(path):
	try:
		total = 0
		quantity = 0

		with open(path, encoding="UTF-8") as file:
			for line in file:
				salary = int(line.strip().split(",")[1])
				total += salary
				quantity += 1

			average = total/quantity
		return int(total), int(average)
	
	except FileExistsError:
		raise FileExistsError("Такого файла не існує.")
	
	except FileNotFoundError:
		raise FileNotFoundError("Файл не знайдено.")
	
	except (IOError, ValueError) as msg:
		raise IOError(f"При обробці файлу сталася помилка: {msg}")
	
try:
	total, average = total_salary("C:\\my_repo\\goit-pycore-hw-04\\salary_file.txt")
	print (f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

except (FileExistsError, FileNotFoundError, IOError) as msg:
	print(msg)

