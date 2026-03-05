file = open("sample_log.txt", "r")

error_count = 0

for line in file:
    if "error" in line.lower():
        print("Error found:", line.strip())
        error_count += 1

print("Total errors found:", error_count)
