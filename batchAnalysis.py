import numpy as np
import matplotlib.pyplot as plt

plt.style.use('dark_background')
import numpy as np
import re

# toolbox functions
def getContestant(fileString):
    contestant = "NOT FOUND"
    if "Perfect" in fileString:
        contestant = "Perfect"

    if "Vapor" in fileString:
        contestant = "Vapor"
    if "Kitura" in fileString:
       contestant = "Kitura"
    return contestant

def parseFileJSON (sourcefile):
    with open(sourcefile) as inF:
        for c, line in enumerate(inF):
            values = line.split()

            if len(values) is 5 and c > 4 and c < 7:
                with open(targetfile, "a") as outF:

                    outF.write(values[1] + "," + values[2] + "," + values[3] + "," + values [4]
                               + "," +  values[0] + "," + getContestant(sourcefile) + "\n")

            if len(values) is 5 and c == 5:
                plotVal1.append(float(values[1][:-2]))

            if len(values) is 5 and c == 6:
                plotVal2.append(float(values[1]))

def setHeaderJSON ():
    with open(targetfile, "a") as outF:
        outF.write("Stats" + "\n")
        outF.write("Avg" + "," + "Stdev" + "," + "Max" + "," + "Stdev" + "\n")


def autolabel(rects, ax):
    # Get y-axis height to calculate label position from.
    (y_bottom, y_top) = ax.get_ylim()
    y_height = y_top - y_bottom

    for rect in rects:
        # print(dir(rect))
        height = 0

        if rect.get_y() < 0:
            height = rect.get_y()
            # print(str(rect.get_y()))
        else:
            height = rect.get_height()
            # print(rect.get_height())

        print(str(rect.get_height()))
        # Fraction of axis height taken up by this rectangle
        p_height = (height / y_height)

        # If we can fit the label above the column, do that;
        # otherwise, put it inside the column.
        if p_height > 0.95:  # arbitrary; 95% looked good to me.
            label_position = height - (y_height * 0.05) if (height > 0) else height + (y_height * 0.05)
        else:
            label_position = height + (y_height * 0.01) if (height > 0) else height - (y_height * 0.001)

        ax.text(rect.get_x() + rect.get_width() / 2.0, label_position,
                '%d' % int(height),
                ha='center', va='bottom')



testCase = "JSONbenchmarkingV1"
titelName = "JSON benchmarking"
sourcefile1 = './RawLogFiles/jsonPerfectClientWrk2V1.txt'
sourcefile2 = './RawLogFiles/jsonVaporClientWrk2V1.txt'
sourcefile3 = './RawLogFiles/jsonKituraClientWrk2V1.txt'

plotVal1 = []
plotVal2 = []

targetfile = 'datalyzed/' + testCase + '.csv'

setHeaderJSON()
parseFileJSON(sourcefile1)
parseFileJSON(sourcefile2)
parseFileJSON(sourcefile3)


# with open(targetfile, "a") as outF:
#     outF.write("Full distribution" + "\n")
#     outF.write("Value" + "," + "Percentile" + "," + "TotalCount" + "," + "1/(1-Percentile)" + "\n")
# with open(sourcefile) as inF:
#     for c, line in enumerate(inF):
#         values = line.split()
#
#         if len(values) is 4 and c > 18:
#             with open(targetfile, "a") as outF:
#                 outF.write(values[0] + "," + values[1] + "," + values[2] + "," + values[3] + "\n")


print plotVal1
print plotVal2

canvasTitle = "JSON benchmarking"

valuesList1 = plotVal1
valuesList2 = plotVal2

n_groups = 3
fig, ax = plt.subplots()
fig.canvas.set_window_title(canvasTitle)

index = np.arange(n_groups)
bar_width = 0.20
opacity = 0.8


rects1 = plt.bar(index + 0.00, valuesList1, bar_width,
                 alpha=opacity,
                 color='g',
                 label='Latency')
rects2 = plt.bar(index + bar_width, valuesList2, bar_width,
                 alpha=opacity,
                 color='c',
                 label='Req/Sec')
# rects3 = plt.bar(index + bar_width * 2, valuesKitura, bar_width,
#                  alpha=opacity,
#                  color='c',
#                  label='Kitura')

label_week_lists = ('Perfect', 'Vapor','Kitura')

plt.ylabel('ms')
plt.title(canvasTitle)
plt.xticks(index + bar_width, label_week_lists)
plt.legend(bbox_to_anchor=(1, 1),
           bbox_transform=plt.gcf().transFigure)

autolabel(rects1, ax)
autolabel(rects2, ax)
# autolabel(rects3, ax)

plt.savefig('datalyzed/' + testCase + '.png')

plt.tight_layout()
plt.show()