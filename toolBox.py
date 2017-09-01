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
                    # th.split('/')
                    th = re.findall('\d+',values[4])
                    th = float(th[0])
                else:
                    th = float(th)

                mem = values[7]
                if not "M" in mem:
                    mem = re.findall('\d+',values[7])
                    mem = float(mem[0])
                    mem = mem / 1024
                else:
                    mem = re.findall('\d+', values[7])
                    mem = float(mem[0])

                with open(targetfile, "a") as outF:
                    outF.write(str(cpu) + "," + str(th) + "," + str(mem) + ","
                               + getContestant(sourcefile) + "\n")

                plotVal1.append(cpu)
                plotVal2.append(th)
                plotVal3.append(mem)
    return plotVal1, plotVal2, plotVal3

def parseErrorsWrk2 (sourcefile, plotVal1, plotVal2, targetfile):
    with open(sourcefile) as inF:
        lines = inF.readlines()

        for i in range(0, len(lines)):
            line = lines[i]

            if "#[Buckets" in line:
                values = lines[i+2].split()
                reqT = values[0]
                reqT = float(reqT)
                plotVal1.append(reqT)


            if "Socket errors:" in line:
                values = line.split()
                errCon = values[3][:-1]
                errRead = values[5][:-1]
                err = float(errRead) + float(errCon)
                timeOut = float(values[9])
                err = err + timeOut
                plotVal2.append(err)

                # with open(targetfile, "a") as outF:
                #     outF.write(str(reqT) + "," + str(err) + "," + getContestant(sourcefile) + "\n")

    return plotVal1, plotVal2

# def parseThreadServer(sourcefile, plotVal1, targetfile):
#     with open(sourcefile) as inF:
#         lines = inF.readlines()
#         for i in range(0, len(lines)):
#             line = lines[i]
#             if "PID" in line:
#                 values = lines[i + 1].split()
#                 th = values[4]
#                 if "/" in th:
#                     th.split('/')
#                     th = float(th[0])
#                 th = float(th)
#
#
#                 with open(targetfile, "a") as outF:
#                     # outF.write(values[2] + "," + values[4] + "," + values[7] + ","
#                     #            + getContestant(sourcefile) + "\n")
#
#                     outF.write(str(th) + "," + getContestant(sourcefile) + "\n")
#
#                 plotVal1.append(th)
#         return plotVal1

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



def visusalize2Pie(titelName, plotVal1, plotVal2, testcase):

    toasted = False

    total = plotVal1[0]
    if not plotVal2:
        return
    if plotVal2[0] > plotVal1[0]:
        plotVal2[0] = plotVal1[0]
        toasted = True

    rest = plotVal1[0] - plotVal2[0]
    errors = plotVal2[0]

    colors_set = ('#29FE13','#D53BD2')

    labels = 'Total Requests', 'Errors'
    sizes = [rest, errors]
    if toasted == False:
        explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')
    else:
        explode = (0, 0.0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, colors = colors_set, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title(titelName, color='c')

    # plt.show()
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
    valuesList1 = [i / 60 for i in plotVal1]
    valuesList2 = [i / 60 for i in plotVal2]
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

    plt.ylabel('Minutes')
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

    label_week_lists = ('Perfect', 'Vapor', 'Vapor Manual','Kitura')

    plt.ylabel('ms')
    plt.title(canvasTitle)
    plt.xticks(index + bar_width, label_week_lists)
    plt.legend(bbox_to_anchor=(1, 1),
               bbox_transform=plt.gcf().transFigure)

    autolabel(rects1, ax)
    autolabel(rects2, ax)

    plt.savefig('datalyzed/img/' + testcase + '.png')

def visusalizeTopServer(titelName, plotVal1, plotVal2, plotVal3, testcase):
    canvasTitle = titelName
    valuesList1 = plotVal1
    valuesList2 = plotVal2
    valuesList3 = plotVal3

    f, axarr = plt.subplots(3, sharex=True)
    axarr[0].set_title(titelName,color='#D53BD2')
    axarr[0].plot(plotVal1,color='#D53BD2')
    axarr[0].set_ylabel('CPU %',color='#D53BD2')
    axarr[1].plot(plotVal2,color='#29FE13')
    # axarr[1].set_title('Threads',color='#29FE13')
    axarr[1].set_ylabel('Threads',color='#29FE13')
    axarr[2].plot(plotVal3,color='c')
    # axarr[2].set_title('Memory kB',color='c')
    axarr[2].set_ylabel('Memory MB',color='c')
    # plt.tight_layout()
    f.savefig('datalyzed/img/' + testcase + '.png')



# def visusalize1ValueSet(titelName, plotVal1, testcase):
#     canvasTitle = titelName
#     valuesList1 = plotVal1
#     n_groups = 3
#     fig, ax = plt.subplots()
#     fig.canvas.set_window_title(canvasTitle)
#
#     index = np.arange(n_groups)
#     bar_width = 0.20
#     opacity = 0.8
#
#     rects1 = plt.bar(index + 0.00, valuesList1, bar_width,
#                      alpha=opacity,
#                      color='#29FE13',
#                      label='Latency')
#     # rects2 = plt.bar(index + bar_width, valuesList2, bar_width,
#     #                  alpha=opacity,
#     #                  color='#D53BD2',
#     #                  label='Req/Sec')
#
#     label_week_lists = ('Perfect', 'Vapor', 'Kitura')
#
#     plt.ylabel('ms')
#     plt.title(canvasTitle)
#     plt.xticks(index + bar_width, label_week_lists)
#     plt.legend(bbox_to_anchor=(1, 1),
#                bbox_transform=plt.gcf().transFigure)
#
#     autolabel(rects1, ax)
#     # autolabel(rects2, ax)
#
#     # plt.savefig('datalyzed/img/' + testcase + '.png')

def showPlot(plt):
    plt.tight_layout()
    plt.show()