'''
Created on Nov 1, 2013

@author: Edoardo Foco
'''
import WebSite
import sys
import os

# data structures
file_list = []
list_of_interesting_websites = []

# validating input
if not len(sys.argv) == 1:
    path = sys.argv[1]
   
else:
    print "\nWarning: Incorrect Usage \nUsage: python check_for_mailing_lists.py $path \n"    
    quit()

# resolving directories
for dirs in os.walk(path):
        if "/raw" in dirs[0]:
            file_list.append(dirs[0])

if len(file_list)==0:
    print "\nWarning: Incorrect Path, no files were found\n"
    quit()
    
# process websites
for path in file_list:
    tmp = WebSite.analyse_website(path)
    if tmp['interesting']:
        list_of_interesting_websites.append(tmp)

# print interesting results
for websites in list_of_interesting_websites:
    print websites

print "Interesting Websites:",len(list_of_interesting_websites),"/",len(file_list)

if __name__ == '__main__':
    pass