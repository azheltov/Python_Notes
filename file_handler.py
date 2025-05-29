# file_handler.py

# Open and read the file
with open("sample.txt", "r") as file:
    lines = file.readlines()

# Remove whitespace and duplicates
cleaned = set(line.strip() for line in lines)

# Write cleaned data to a new file
with open("cleaned_sample.txt", "w") as file:
    for item in cleaned:
        file.write(item + "\n")

print("Cleaned data saved to cleaned_sample.txt")
