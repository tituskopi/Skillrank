import json

# Read the JSON data from the ex5.json file
with open("C:\\Users\\TITUS KOPI\\Desktop\\Skillrank\\Assesment 2\\ex5.json", "r") as file:
    data = json.load(file)

# Find the donut with the name "Old Fashioned" and add a new batter named "Tea"
for donut in data:
    if donut['name'] == 'Old Fashioned':
        donut['batters']['batter'].append({'id': '1005', 'type': 'Tea'})

# Write the updated JSON data back to the ex5.json file
with open("C:\\Users\\TITUS KOPI\\Desktop\\Skillrank\\Assesment 2\\ex5.json", "w") as file:
    json.dump(data, file, indent=4)

print("Batter named Tea for donut with name Old Fashioned added and ex5.json updated.")