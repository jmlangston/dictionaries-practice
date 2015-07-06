# put your code here.

test_file = open("twain.txt")

my_dict = {} # key will be word, value will be word count

for line in test_file:
    line = line.rstrip()
    split_line = line.split(" ")
    for word in split_line:
        if word not in my_dict:
            my_dict[word] = 0
        if word in my_dict:
            my_dict[word] = my_dict[word] + 1


for key in my_dict:
    print "%s %d" % (key, my_dict[key]) 
