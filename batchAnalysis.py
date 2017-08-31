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

def parseHeaderWrk2 (sourcefile):
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

def parseBuildTimes (sourcefile, plotVal1):
    with open(sourcefile) as inF:
        for c, line in enumerate(inF):
            values = line.split()

            if "user" in line:
                with open(targetfile, "a") as outF:
                    outF.write(values[1] + "," + getContestant(sourcefile) + "\n")
                    minutes, seconds =  values[1].split('m')
                    seconds = seconds[:-5]
                    plotVal1.append((float(minutes) * 60.0) + float(seconds))
                    return plotVal1


def setHeaderJSON():
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

def visusalize1Vals(titelName, plotVal1):
    canvasTitle = titelName
    valuesList1 = plotVal1

    n_groups = 3
    fig, ax = plt.subplots()
    fig.canvas.set_window_title(canvasTitle)

    index = np.arange(n_groups)
    bar_width = 0.20
    opacity = 0.8

    rects1 = plt.bar(index + 0.00, valuesList1, bar_width,
                     alpha=opacity,
                     color='g',
                     label='Dubug')

    label_week_lists = ('Perfect', 'Vapor', 'Kitura')

    plt.ylabel('ms')
    plt.title(canvasTitle)
    plt.xticks(index + bar_width, label_week_lists)
    plt.legend(bbox_to_anchor=(1, 1),
               bbox_transform=plt.gcf().transFigure)

    autolabel(rects1, ax)

    plt.savefig('datalyzed/img/' + testCase + '.png')

def visusalize2Vals(titelName, plotVal1, plotVal2):
    canvasTitle = titelName
    valuesList1 = plotVal1
    valuesList2 = plotVal2
    n_groups = 3
    fig, ax = plt.subplots()
    fig.canvas.set_window_title(canvasTitle)

    index = np.arange(n_groups)
    bar_width = 0.20
    opacity = 0.8

    print(valuesList1)
    print(valuesList2)

    rects1 = plt.bar(index + 0.00, valuesList1, bar_width,
                     alpha=opacity,
                     color='g',
                     label='Latency')
    rects2 = plt.bar(index + bar_width, valuesList2, bar_width,
                     alpha=opacity,
                     color='c',
                     label='Requests per Second')

    label_week_lists = ('Perfect', 'Vapor', 'Kitura')

    plt.ylabel('ms')
    plt.title(canvasTitle)
    plt.xticks(index + bar_width, label_week_lists)
    plt.legend(bbox_to_anchor=(1, 1),
               bbox_transform=plt.gcf().transFigure)

    autolabel(rects1, ax)
    autolabel(rects2, ax)

    plt.savefig('datalyzed/img/' + testCase + '.png')

def showPlot(plt):
    plt.tight_layout()
    plt.show()


# MAIN START
plotVal1 = []
plotVal2 = []

# JSON V1
testCase = "JSONbenchmarkingV1"
titelName = "JSON benchmarking"
sourcefile1 = './RawLogFiles/jsonPerfectClientWrk2V1.txt'
sourcefile2 = './RawLogFiles/jsonVaporClientWrk2V1.txt'
sourcefile3 = './RawLogFiles/jsonKituraClientWrk2V1.txt'
plotVal1 = []
plotVal2 = []
targetfile = 'datalyzed/csv/' + testCase + '.csv'
setHeaderJSON()
parseHeaderWrk2(sourcefile1)
parseHeaderWrk2(sourcefile2)
parseHeaderWrk2(sourcefile3)
visusalize2Vals(titelName,plotVal1,plotVal2)

# JSON V2
testCase = "JSONbenchmarkingV2"
titelName = "JSON benchmarking / Non generated JSON"
sourcefile1 = './RawLogFiles/jsonPerfectClientWrk2V2.txt'
sourcefile2 = './RawLogFiles/jsonVaporClientWrk2V2.txt'
sourcefile3 = './RawLogFiles/jsonKituraClientWrk2V2.txt'
plotVal1 = []
plotVal2 = []
targetfile = 'datalyzed/csv/' + testCase + '.csv'
setHeaderJSON()
parseHeaderWrk2(sourcefile1)
parseHeaderWrk2(sourcefile2)
parseHeaderWrk2(sourcefile3)
visusalize2Vals(titelName,plotVal1,plotVal2)

# HTML V1
testCase = "HTMLbenchmarkingV1"
titelName = "HTML benchmarking"
sourcefile1 = './RawLogFiles/htmlPerfectClientWrk2V1.txt'
sourcefile2 = './RawLogFiles/htmlVaporClientWrk2V1.txt'
sourcefile3 = './RawLogFiles/htmlKituraClientWrk2V1.txt'
plotVal1 = []
plotVal2 = []
targetfile = 'datalyzed/csv/' + testCase + '.csv'
setHeaderJSON()
parseHeaderWrk2(sourcefile1)
parseHeaderWrk2(sourcefile2)
parseHeaderWrk2(sourcefile3)
visusalize2Vals(titelName,plotVal1,plotVal2)

# HTML V2
testCase = "HTMLbenchmarkingV2"
titelName = "HTML benchmarking / Large HTML"
sourcefile1 = './RawLogFiles/htmlPerfectClientWrk2V2.txt'
sourcefile2 = './RawLogFiles/htmlVaporClientWrk2V2.txt'
sourcefile3 = './RawLogFiles/htmlKituraClientWrk2V2.txt'
plotVal1 = []
plotVal2 = []
targetfile = 'datalyzed/csv/' + testCase + '.csv'
setHeaderJSON()
parseHeaderWrk2(sourcefile1)
parseHeaderWrk2(sourcefile2)
parseHeaderWrk2(sourcefile3)
visusalize2Vals(titelName,plotVal1,plotVal2)

# STRESS V1
testCase = "STRESSbenchmarkingV1"
titelName = "Stress Test benchmarking"
sourcefile1 = './RawLogFiles/stressPerfectClientWrk2V1.txt'
sourcefile2 = './RawLogFiles/stressVaporClientWrk2V1.txt'
sourcefile3 = './RawLogFiles/stressKituraClientWrk2V1.txt'
plotVal1 = []
plotVal2 = []
targetfile = 'datalyzed/csv/' + testCase + '.csv'
setHeaderJSON()
parseHeaderWrk2(sourcefile1)
parseHeaderWrk2(sourcefile2)
parseHeaderWrk2(sourcefile3)
visusalize2Vals(titelName,plotVal1,plotVal2)

# STRESS V2
testCase = "STRESSbenchmarkingV2"
titelName = "Stress Test benchmarking / High Load"
sourcefile1 = './RawLogFiles/stressPerfectClientWrk2V2.txt'
sourcefile2 = './RawLogFiles/stressVaporClientWrk2V2.txt'
sourcefile3 = './RawLogFiles/stressKituraClientWrk2V2.txt'
plotVal1 = []
plotVal2 = []
targetfile = 'datalyzed/csv/' + testCase + '.csv'
setHeaderJSON()
parseHeaderWrk2(sourcefile1)
parseHeaderWrk2(sourcefile2)
parseHeaderWrk2(sourcefile3)
visusalize2Vals(titelName,plotVal1,plotVal2)

# STRESS V3
testCase = "STRESSbenchmarkingV3"
titelName = "Stress Test benchmarking / Spike Load"
sourcefile1 = './RawLogFiles/stressPerfectClientWrk2V3.txt'
sourcefile2 = './RawLogFiles/stressVaporClientWrk2V3.txt'
sourcefile3 = './RawLogFiles/stressKituraClientWrk2V3.txt'
plotVal1 = []
plotVal2 = []
targetfile = 'datalyzed/csv/' + testCase + '.csv'
setHeaderJSON()
parseHeaderWrk2(sourcefile1)
parseHeaderWrk2(sourcefile2)
parseHeaderWrk2(sourcefile3)
visusalize2Vals(titelName,plotVal1,plotVal2)

# BUILD TIMES V1
testCase = "BUILDSbenchmarkingV1"
titelName = "Build times"
sourcefile1 = './RawLogFiles/btDebugPerfectServerV1.txt'
sourcefile2 = './RawLogFiles/btDebugVaporServerV1.txt'
sourcefile3 = './RawLogFiles/btDebugKituraServerV1.txt'

sourcefile4 = './RawLogFiles/btReleasePerfectServerV1.txt'
sourcefile5 = './RawLogFiles/btReleaseVaporServerV1.txt'
sourcefile6 = './RawLogFiles/btReleaseKituraServerV1.txt'

plotVal1 = []
plotVal2 = []

targetfile = 'datalyzed/csv/' + testCase + '.csv'

parseBuildTimes(sourcefile1,plotVal1)
parseBuildTimes(sourcefile2,plotVal1)
parseBuildTimes(sourcefile3,plotVal1)

parseBuildTimes(sourcefile4,plotVal2)
parseBuildTimes(sourcefile5,plotVal2)
parseBuildTimes(sourcefile6,plotVal2)

legend = ["Debug","Release"]
visusalize2Vals(titelName,plotVal1,plotVal2)