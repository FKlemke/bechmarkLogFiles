import os

directory = "./RawLogFiles/"

lineCount = 0
fileCount = 0
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        fileCount = fileCount + 1
        with open("./RawLogFiles/" + filename) as inF:
            lines = inF.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                lineCount = lineCount + 1
        continue
    else:
        continue

print fileCount
print lineCount

