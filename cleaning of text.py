import re
mystring ="i am going to attain 9 workshop $ on machine learning"
cleaned =re.sub('[^A-Za-z0-9]+', ' ', mystring)
print (cleaned)