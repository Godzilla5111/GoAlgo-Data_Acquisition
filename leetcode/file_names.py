# import OS module
import os

# Get the list of all files and directories
path = "C:/Users/ANURAG SINGH/Desktop/IIT KGP/Semesters/SEM-5/AI61005/assignment/leetcode/questions"
dir_list = os.listdir(path)

print("Files and directories in '", path, "' :")
urls = []
titles = []
for name in dir_list:
    x,y = name.split('.')
    urls.append('https://leetcode.com/problems/'+x+'/')

# prints all files
file = open('urls.txt','w')
file.write('\n'.join(urls))
