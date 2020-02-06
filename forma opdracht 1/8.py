file_before = open("file2comprez.txt", "r")
lines = file_before.readlines()
comprezed_lines = []
for line in lines:
    if line != "\n":
        comprezed_lines.append(line.strip() + "\n")

file_before.close()
file_after = open("comprezedfile.txt", "w")
file_after.writelines(comprezed_lines)
file_after.close()
