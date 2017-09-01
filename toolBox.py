import numpy as np
import matplotlib.pyplot as plt
plt.style.use('dark_background')
import numpy as np
import re

# comment these two files out if you don't have Menlo installed or follow intallation on
# http://www.claridgechang.net/blog/how-to-use-custom-fonts-in-matplotlib
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Menlo'

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

def parseHeaderWrk2 (sourcefile, plotVal1, plotVal2,targetfile):
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
                return plotVal1,plotVal2

def parseBuildTimes (sourcefile, plotVal1, targetfile):
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

def parseTopServer (sourcefile, plotVal1, plotVal2, plotVal3, targetfile):
    with open(sourcefile) as inF:
        lines = inF.readlines()

        for i in range(0, len(lines)):
            line = lines[i]

            if "PID" in line:
                values = lines[i + 1].split()

                cpu = float(values[2])
                th = values[4]
                if "/" in th:
                    th.split('/')
                    th = float(th[0])

                mem = re.findall('\d+',values[7])
                mem = float(mem[0])

                with open(targetfile, "a") as outF:
                    # outF.write(values[2] + "," + values[4] + "," + values[7] + ","
                    #            + getContestant(sourcefile) + "\n")

                    outF.write(str(cpu) + "," + str(th) + "," + str(mem) + ","
                               + getContestant(sourcefile) + "\n")

                plotVal1.append(cpu)
                plotVal2.append(th)
                plotVal3.append(mem)
        return plotVal1, plotVal2, plotVal3

def setHeaderLatRegSec(targetfile):
    with open(targetfile, "a") as outF:
        outF.write("Stats" + "\n")
        outF.write("Avg" + "," + "Stdev" + "," + "Max" + "," + "Stdev" + "\n")

def setHeaderTop(targetfile):
    with open(targetfile, "a") as outF:
        outF.write("Stats" + "\n")
        outF.write("CPU" + "," + "Threads" + "," + "Memory" + "," + "Framework" + "\n")

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

        # print(str(rect.get_height()))
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

def visusalize2Vals(titelName, plotVal1, plotVal2, legend, testcase, xyLabel):
    canvasTitle = titelName
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
                     label=legend[0])
    rects2 = plt.bar(index + bar_width, valuesList2, bar_width,
                     alpha=opacity,
                     color='c',
                     label=legend[1])

    label_week_lists = xyLabel[1]

    plt.ylabel(xyLabel[0])
    plt.title(canvasTitle)
    plt.xticks(index + bar_width, label_week_lists)
    plt.legend(bbox_to_anchor=(1, 1),
               bbox_transform=plt.gcf().transFigure)

    autolabel(rects1, ax)
    autolabel(rects2, ax)

    plt.savefig('datalyzed/img/' + testcase + '.png')

def visusalizeLatReq(titelName, plotVal1, plotVal2, testcase):
    canvasTitle = titelName
    valuesList1 = plotVal1
    valuesList2 = plotVal2

    print "Value Lists"
    print valuesList1
    print valuesList2

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
                     label='Requests per Second')

    label_week_lists = ('Perfect', 'Vapor', 'Kitura')

    plt.ylabel('ms')
    plt.title(canvasTitle)
    plt.xticks(index + bar_width, label_week_lists)
    plt.legend(bbox_to_anchor=(1, 1),
               bbox_transform=plt.gcf().transFigure)

    autolabel(rects1, ax)
    autolabel(rects2, ax)

    plt.savefig('datalyzed/img/' + testcase + '.png')

def visusalizeValueSets(titelName, plotVal1, plotVal2, testcase):
    canvasTitle = titelName
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
                     color='#29FE13',
                     label='Latency')
    rects2 = plt.bar(index + bar_width, valuesList2, bar_width,
                     alpha=opacity,
                     color='#D53BD2',
                     label='Req/Sec')

    label_week_lists = ('Perfect', 'Vapor', 'Kitura')

    plt.ylabel('ms')
    plt.title(canvasTitle)
    plt.xticks(index + bar_width, label_week_lists)
    plt.legend(bbox_to_anchor=(1, 1),
               bbox_transform=plt.gcf().transFigure)

    autolabel(rects1, ax)
    autolabel(rects2, ax)

    plt.savefig('datalyzed/img/' + testcase + '.png')


def visusalizeBuildTimes(titelName, plotVal1, plotVal2, testcase):
    canvasTitle = titelName
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
                     color='#29FE13',
                     label='Debug')
    rects2 = plt.bar(index + bar_width, valuesList2, bar_width,
                     alpha=opacity,
                     color='#D53BD2',
                     label='Release')

    label_week_lists = ('Perfect', 'Vapor', 'Kitura')

    plt.ylabel('Seconds')
    plt.title(canvasTitle)
    plt.xticks(index + bar_width, label_week_lists)
    plt.legend(bbox_to_anchor=(1, 1),
               bbox_transform=plt.gcf().transFigure)

    autolabel(rects1, ax)
    autolabel(rects2, ax)

    plt.savefig('datalyzed/img/' + testcase + '.png')

def visusalizeValueSetsVaporTools(titelName, plotVal1, plotVal2, testcase):
    canvasTitle = titelName
    valuesList1 = plotVal1
    valuesList2 = plotVal2
    n_groups = 4
    fig, ax = plt.subplots()
    fig.canvas.set_window_title(canvasTitle)

    index = np.arange(n_groups)
    bar_width = 0.20
    opacity = 0.8

    rects1 = plt.bar(index + 0.00, valuesList1, bar_width,
                     alpha=opacity,
                     color='#29FE13',
                     label='Latency')
    rects2 = plt.bar(index + bar_width, valuesList2, bar_width,
                     alpha=opacity,
                     color='#D53BD2',
                     label='Req/Sec')

    label_week_lists = ('Perfect', 'Vapor', 'Vapor Special','Kitura')

    plt.ylabel('ms')
    plt.title(canvasTitle)
    plt.xticks(index + bar_width, label_week_lists)
    plt.legend(bbox_to_anchor=(1, 1),
               bbox_transform=plt.gcf().transFigure)

    autolabel(rects1, ax)
    autolabel(rects2, ax)

    plt.savefig('datalyzed/img/' + testcase + '.png')

def visusalizeThreads(titelName, plotVal1, plotVal2, testcase):
    canvasTitle = titelName
    valuesList1 = plotVal1
    valuesList2 = plotVal2
    n_groups = 4
    fig, ax = plt.subplots()
    fig.canvas.set_window_title(canvasTitle)

    index = np.arange(n_groups)
    bar_width = 0.20
    opacity = 0.8

    rects1 = plt.bar(index + 0.00, valuesList1, bar_width,
                     alpha=opacity,
                     color='#29FE13',
                     label='Latency')
    rects2 = plt.bar(index + bar_width, valuesList2, bar_width,
                     alpha=opacity,
                     color='#D53BD2',
                     label='Req/Sec')

    label_week_lists = ('Perfect', 'Vapor', 'Vapor Special','Kitura')

    plt.ylabel('ms')
    plt.title(canvasTitle)
    plt.xticks(index + bar_width, label_week_lists)
    plt.legend(bbox_to_anchor=(1, 1),
               bbox_transform=plt.gcf().transFigure)

    autolabel(rects1, ax)
    autolabel(rects2, ax)

    plt.savefig('datalyzed/img/' + testcase + '.png')

def showPlot(plt):
    plt.tight_layout()
    plt.show()