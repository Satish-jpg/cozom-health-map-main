import os

directory = "C:/Users/maury/OneDrive/Desktop/cozom-health-map-main"

# सभी Python फाइलों के लिए रिप्लेस करें
for filename in os.listdir(directory):
    if filename.endswith(".py"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        content = content.replace("WebMD", "Cozom")
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(content)

print("Replacement completed successfully.")
