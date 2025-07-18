import csv


f = open("tags", "w")

for i in range(2):
    with open('Tag' + str(i) + '.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='"', quotechar='|')
        tags = []
        for row in spamreader:
            if len(row) > 1:
                tags.append(row[1])
        tags = ",".join(tags)
        tags = tags.split(",")
        for tag in tags:
            tag = tag.removeprefix(' ')
            if tag != "":
                f.write(tag+"\n")
f.close()