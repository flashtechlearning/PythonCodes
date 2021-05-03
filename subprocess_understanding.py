import subprocess

#p1 = subprocess.run('git --version', shell = True , text = True , capture_output = True)


#p1_output = p1.stdout



with open('git_status.txt' , 'w') as f:
    p2 = subprocess.run('git status', shell = True , text = True , stdout = f)

string1 = '.py'

all_string = []

# opening a text file
with open('git_status.txt', 'r') as read_file:
    # Loop through the file line by line
    for line in read_file:
        for item in line.split(' '):
            all_string.append(item)

# closing text file
read_file.close()

final_files_from_git_status = []

print('************')
for i in all_string:
    result = i.find(string1)
    if result >= 0:
        final_files_from_git_status.append(i.strip())


for i in final_files_from_git_status:
    print(i)


# p3 = subprocess.run('git add ', shell = True , text = True, capture_output = True)
#
# p3 = subprocess.run('git commit -m "Automated commit"', shell = True , text = True, capture_output = True)
