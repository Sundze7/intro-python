languages = ['Python', 'Java', 'C++', 'JavaScript', 'Ruby']

# run a loop for each item of the list

for language in languages:
    print(language)
    
print()

# while loop
i = 1
n = 5

while i < n:
    print(i)
    i = i + 1
        
print()

# Using break
for i in range(5):
    if i == 3:
        break
    print(i)
    
print()


#using continue
for i in range(5):
    if i == 3:
        continue
    print(i)