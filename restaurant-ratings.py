# your code goes here

scores_file = open("scores.txt")

restaurants_dict = {}

for line in scores_file:
    line = line.rstrip()
    split_line = line.split(":")
    restaurants_dict[split_line[0]] = split_line[1]

rest_tuples = restaurants_dict.items()  # returns a list of tuples

rest_sorted = sorted(rest_tuples)  # alphabetizes the tuples

for rest_name, rest_score in rest_sorted:  # unpack the tuples
    print "%s is rated at %s" % (rest_name, rest_score)
