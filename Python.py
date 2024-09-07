import os

file_names = [
    'Aggregate Listening Data',
    'Weekly Orders Report',
    'Top Monthly Sellers',
    'Peak Online Time',
    'Movie Duration Match',
    'Finding Doctors',
    'Salaries Differences',
    'Finding Updated Records',
    'Find all inspections which are part of an inactive program',
    'Order all countries by the year they first participated in the Olympics',
    'Total Cost Of Orders'
]

# Directory where the files will be created
directory = '/Users/spatta8/Desktop/SQL-Solutions/Stratascratch'

# Ensure the directory exists
os.makedirs(directory, exist_ok=True)

for name in file_names:
    # Replace spaces and special characters in file names
    file_path = os.path.join(directory, name + '.txt')
    with open(file_path, 'w') as file:
        file.write('')  # Creating an empty file or write some content if needed
