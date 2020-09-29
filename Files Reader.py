import os

location = 'C:/Users/owais/OneDrive/Desktop/Chaiflix/'
files_in_dir = []

# r=>root, d=>directories, f=>files
for r, d, f in os.walk(location):
   for item in f:
      files_in_dir.append(os.path.join(r, item))

for item in files_in_dir:
   print(item)
