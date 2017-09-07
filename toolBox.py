
##############################################################
# Contains the model for parsing raw files and visualization #
##############################################################

import matplotlib.pyplot as plt
plt.style.use('dark_background')
import numpy as np
import re

# comment these two files out if you don't have Menlo installed or follow install steps on
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

def parseHeaderWrk22 (sourcefile, plotVal1, plotVal2,targetfile):
    latency = 0.0
    with open(sourcefile) as inF:
        for c, line in enumerate(inF):
            values = line.split()

            if len(values) is 5 and c > 4 and c < 7:
                with open(targetfile, "a") as outF:
                    outF.write(values[1] + "," + values[2] + "," + values[3] + "," + values [4]
                               + "," +  values[0] + "," + getContestant(sourcefile) + "\n")

            if c == 7 and "Latency" in line:
                values = line.split()
                latency = values[1][:-2]
                latency = float(latency)
                plotVal1.append(latency)

            if "#[Max" in line:
                values = line.split()
                plotVal2.append(float(values[6][:-1]))
                return plotVal1,plotVal2

def parseHeaderWrk2 (sourcefile, plotVal1, plotVal2, targetfile):
    with open(sourcefile) as inF:
        for c, line in enumerate(inF):
            values = line.split()

            if len(values) is 5 and c > 4 and c < 7:
                with open(targetfile, "a") as outF:

                    outF.write(values[1] + "," + values[2] + "," + values[3] + "," + values [4]
                               + "," +  values[0] + "," + getContestant(sourcefile) + "\n")

            if len(values) is 5 and c == 5:
                plotVal1.append(float(values[1][:-2]))

            if "#[Max" in line:
                values = line.split()
                plotVal2.append(float(values[6][:-1]))
                return plotVal1, plotVal2

def parseHeaderWrk2VsWrkVal(sourcefile, plotVal1, targetfile):
    latency = 0.0
    with open(sourcefile) as inF:
        lines = inF.readlines()
        for i in range(0, len(lines)):
            line = lines[i]
            # if len(values) is 5 and c > 4 and c < 7:
            #     with open(targetfile, "a") as outF:
            #
            #         outF.write(values[1] + "," + values[2] + "," + values[3] + "," + values [4]
            #                    + "," +  values[0] + "," + getContestant(sourcefile) + "\n")

            if "Latency" in line and len(line.split()) == 5:
                values = line.split()
                if "us" in values[1]:
                    latency = float(values[1][:-2])
                    latency /=1000
                else:
                    latency = float(values[1][:-2])
                plotVal1.append(latency)
                return plotVal1

def parseHeaderWrk (sourcefile, plotVal1, plotVal2,targetfile):
    latency = 0.0
    requests = 0.0
    with open(sourcefile) as inF:
        lines = inF.readlines()
        for i in range(0, len(lines)):
            line = lines[i]

            if "Latency" in line and len(line.split()) == 5:
                values = line.split()
                if "us" in values[1]:
                    latency = float(values[1][:-2])
                    latency /=1000
                else:
                    latency = float(values[1][:-2])
                plotVal1.append(latency)

            if "Requests/sec:" in line:
                values = line.split()
                requests = float(values[1])
                plotVal2.append(requests)
        return plotVal1, plotVal2

def parseBuildTimes (sourcefile, plotVal1, targetfile):
    with open(sourcefile) as inF:
        for c, line in enumerate(inF):
            values = line.split()

            if "user" in line:
                with open(targetfile, "a") as outF:
                    outF.write(values[1] + "," + getContestant(sourcefile) + "\n")
                    minutes, seconds =  values[1].split('m')
                    seconds = seconds[:-5]
                    if  '0' in minutes:
                        plotVal1.append(float(seconds))
                    else:
                        plotVal1.append((float(minutes) * 60.0) + float(seconds))
                    return plotVal1

def parseTopClient (sourcefile, plotVal1, plotVal2, plotVal3, targetfile):

    with open(sourcefile) as inF:
        lines = inF.readlines()

        for i in range(0, len(lines)):
            line = lines[i]
            th = 0
            if "wrk2" in line:
                values = lines[i].split()

                cpu = float(values[2])
                th = values[4]

                if "/" in th:
                    # th.split('/')
                    th = re.findall('\d+',values[4])
                    th = float(th[0])
                    # print th
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
        height = 0

        if rect.get_y() < 0:
            height = rect.get_y()
        else:
            height = rect.get_height()
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

def autolabelDec(rects, ax):
    # Get y-axis height to calculate label position from.
    (y_bottom, y_top) = ax.get_ylim()
    y_height = y_top - y_bottom

    for rect in rects:
        height = 0

        if rect.get_y() < 0:
            height = rect.get_y()
        else:
            height = rect.get_height()

        p_height = (height / y_height)

        if p_height > 0.95:  # arbitrary; 95% looked good to me.
            label_position = height - (y_height * 0.05) if (height > 0) else height + (y_height * 0.05)
        else:
            label_position = height + (y_height * 0.01) if (height > 0) else height - (y_height * 0.001)

        ax.text(rect.get_x() + rect.get_width() / 2.0, label_position,
                '%.1f' % height, ha='center', va='bottom')

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
    labels = 'Successful Requests', 'Errors'
    sizes = [rest, errors]

    if toasted == False:
        explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')
    else:
        explode = (0, 0.0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, colors = colors_set, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title(titelName)
    # plt.show()
    plt.savefig('datalyzed/img/' + testcase + '.png')

def autolabel1(rects, ax):
    for rect in rects:
        height = rect.get_height()
        if height.is_integer():
            ax.text(rect.get_x() + rect.get_width() / 2., 0.30 * height,
                    '%d' % height, ha='center', va='bottom')
        else:
            ax.text(rect.get_x() + rect.get_width() / 2., 0.30 * height,
                   '%.2f' % height, ha='center', va='bottom')

def autolabel1B(rects, ax):
    for rect in rects:
        height = rect.get_height()
        if height.is_integer():
            ax.text(rect.get_x() + rect.get_width() / 2., 0.30 * height,
                    '%d' % height, ha='center', va='bottom')
        else:
            ax.text(rect.get_x() + rect.get_width() / 2., 0.30 * height,
                   '%.1f' % height, ha='center', va='bottom')

def visusalizeValueSets(titelName, plotVal1, plotVal2, testcase):
    fig = plt.figure()
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)

    labelLists = ('Perfect', 'Vapor', 'Kitura')
    n_groups = 3
    index = np.arange(n_groups)
    bar_width = 0.40
    opacity = 0.8


    ax1.set_title(titelName, color='w')
    ax1.set_ylabel('Avg latency in ms', color='#29FE13')
    ax2.set_ylabel('Successful requests', color='#D53BD2')

    # xlabels = [format(label, ',.0f') for label in ax1.get_xticks()]
    # ax1.set_xticklabels(xlabels)

    rects1 = ax1.bar(index + 0.00, plotVal1, bar_width,
                     alpha=opacity,
                     color='#29FE13',
                     label='Debug mode')

    rects2 = ax2.bar(index + bar_width, plotVal2, bar_width,
                     alpha=opacity,
                     color='#D53BD2',
                     label='Release mode')
    plt.xticks(index + bar_width, labelLists)
    ax1.axes.get_xaxis().set_visible(False)
    autolabel1(rects1, ax1)
    autolabel1(rects2, ax2)

    fig.savefig('datalyzed/img/' + testcase + '.png')

def visusalizeWrkVsWrk2ValueSets(titelName, plotVal1, plotVal2, plotVal3, plotVal4, testcase):
    fig = plt.figure()
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)

    labelLists = ('Perfect', 'Vapor', 'Kitura')
    n_groups = 3
    index = np.arange(n_groups)
    bar_width = 0.20
    opacity = 0.8


    ax1.set_title(titelName, color='w')
    ax1.set_ylabel('Avg latency in ms', color='#29FE13')
    ax2.set_ylabel('Requests/Second', color='#D53BD2')


    rects1 = ax1.bar(index + 0.00, plotVal1, bar_width,
                     alpha=opacity,
                     color='#29FE13',
                     label='wrk')
    rects3 = ax1.bar(index + bar_width, plotVal3, bar_width,
                     alpha=opacity,
                     color='#D53BD2',
                     label='wrk2 on 50% load')
    rects4 = ax1.bar(index + bar_width * 2, plotVal4, bar_width,
                     alpha=opacity,
                     color='c',
                     label='wrk2 Business case')
    bar_width = 0.60
    rects2 = ax2.bar(index + bar_width, plotVal2, bar_width,
                     alpha=opacity,
                     color='#D53BD2',
                     label='wrk')

    ax1.legend(('100% load', '50% load', 'Business case'))


    plt.xticks(index + bar_width, labelLists)

    ax1.axes.get_xaxis().set_visible(False)
    autolabelDec(rects1, ax1)
    autolabelDec(rects3, ax1)
    autolabelDec(rects4, ax1)
    autolabel(rects2, ax2)
    plt.show()
    # fig.savefig('datalyzed/img/' + testcase + '.png')

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
                     label='Debug mode')
    rects2 = plt.bar(index + bar_width, valuesList2, bar_width,
                     alpha=opacity,
                     color='#D53BD2',
                     label='Release mode')

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
    fig = plt.figure()
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)

    labelLists = ('Perfect', 'Vapor', 'Vapor Manual','Kitura')

    n_groups = 4
    index = np.arange(n_groups)
    bar_width = 0.40
    opacity = 0.8

    ax1.set_title(titelName, color='w')
    ax1.set_ylabel( "Avg latency in ms", color='#29FE13')
    ax2.set_ylabel( "Successful requests", color='#D53BD2')


    rects1 = ax1.bar(index + 0.00, plotVal1, bar_width,
                     alpha=opacity,
                     color='#29FE13',
                     label='Latency')
    rects2 = ax2.bar(index + bar_width, plotVal2, bar_width,
                     alpha=opacity,
                     color='#D53BD2',
                     label='Requests Total')

    ax1.axes.get_xaxis().set_visible(False)

    plt.xticks(index + bar_width, labelLists)
    autolabel1(rects1, ax1)
    autolabel1(rects2, ax2)
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
    # plt.show()
    f.savefig('datalyzed/img/' + testcase + '.png')

def visusalizeValueSetsCR(titelName, plotVal1, plotVal2, testcase):
    fig = plt.figure()
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)

    labelLists = ('Perfect', 'Vapor', 'Kitura')

    n_groups = 3
    index = np.arange(n_groups)
    bar_width = 0.25
    opacity = 0.8

    ax1.set_title(titelName, color='w')
    ax1.set_ylabel('Avg latency in ms', color='#29FE13')
    ax2.set_ylabel('Successful requests', color='#D53BD2')

    wrkLat = [plotVal1[0],plotVal1[1],plotVal1[2]]
    wrk2Lat = [plotVal1[3],plotVal1[4],plotVal1[5]]
    wrkRyLat = [plotVal1[6],plotVal1[7],plotVal1[8]]

    wrkReq = [plotVal2[0], plotVal2[1], plotVal2[2]]
    wrkReq = [int(i) for i in wrkReq]
    wrk2Req = [plotVal2[3],plotVal2[4],plotVal2[5]]
    wrkRyReq = [plotVal2[6],plotVal2[7],plotVal2[8]]

    rects1 = ax1.bar(index + 0.00, wrkLat, bar_width,
                     alpha=opacity,
                     color='#29FE13',
                     label='Wrk Latency')

    rects2 = ax1.bar(index + bar_width, wrk2Lat, bar_width,
                     alpha=opacity,
                     color='#D53BD2',
                     label='Wrk2 Latency')
    rects3 = ax1.bar(index + bar_width * 2, wrkRyLat, bar_width,
                     alpha=opacity,
                     color='c',
                     label='Wrk Ryan Latency')

    rects4 = ax2.bar(index + 0.00, wrkReq, bar_width,
                     alpha=opacity,
                     color='#29FE13',
                     label='Wrk')

    rects5 = ax2.bar(index + bar_width, wrk2Req, bar_width,
                     alpha=opacity,
                     color='#D53BD2',
                     label='Wrk2')
    rects6 = ax2.bar(index + bar_width * 2, wrkRyReq, bar_width,
                     alpha=opacity,
                     color='c',
                     label='Wrk Ryan Collins')

    # ax2.set_xticks(index + bar_width, labelLists)

    ax1.set_xticks(index + bar_width)
    ax1.set_xticklabels(labelLists)

    ax2.set_xticks(index + bar_width)
    ax2.set_xticklabels(labelLists)

    plt.legend(bbox_to_anchor=(1, 1),
               bbox_transform=plt.gcf().transFigure)

    # plt.xticks(index + bar_width, labelLists)
    autolabel1(rects1, ax1)
    autolabel1(rects2, ax1)
    autolabel1(rects3, ax1)

    autolabel1(rects4, ax2)
    autolabel1(rects5, ax2)
    autolabel1(rects6, ax2)
    fig.savefig('datalyzed/img/' + testcase + '.png')


def visualizeStd():
    import matplotlib.pyplot as plt
    import numpy as np

    avg = [47.89,17.42,77.87]
    # std = [19.45,22.11,34.93]
    std = [61.77, 95.83, 59.33]
    x = np.array([1,2,3])
    e = np.array(avg)

    yerr = std
    plt.errorbar(x, e, yerr=yerr,elinewidth=5, ecolor='#D53BD2',marker='D',ls = 'None')

