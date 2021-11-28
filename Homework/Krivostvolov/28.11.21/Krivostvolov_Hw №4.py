flash_1 = 256
flash_2 = 512
flash_3 = 1024
flash_4 = 2097152
file = 0
while flash_1 > 50:
    flash_1 -= 50
    file += 1
else:
    print(f"На флешке 1 поместится {file} файлов")
file = 0
while flash_2 > 50:
    flash_2 -= 50
    file += 1
else:
    print(f"На флешке 2 поместится {file} файлов")
file = 0
while flash_3 > 50:
    flash_3 -= 50
    file += 1
else:
    print(f"На флешке 3 поместится {file} файлов")
file = 0
while flash_4 > 50:
    flash_4 -= 50
    file += 1
else:
    print(f"На флешке 4 поместится {file} файлов")