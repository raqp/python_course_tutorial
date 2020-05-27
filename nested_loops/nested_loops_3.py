# # Petq e hashvel xmbi mijin gnahatakan@
my_list = [{"name": "John", "points": [50, 60]}, {"name": "Robert", "points": [65, 75]},
           {"name": "Richard", "points": [80, 90]}]

summary = 0

for student in my_list:
    for point in student["points"]:
        summary += point


print(summary / (2 * len(my_list)))
