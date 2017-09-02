############################################################
# Contains only code that got dumped or temporarily stored #
############################################################



with open(targetfile, "a") as outF:
    outF.write("Full distribution" + "\n")
    outF.write("Value" + "," + "Percentile" + "," + "TotalCount" + "," + "1/(1-Percentile)" + "\n")
with open(sourcefile) as inF:
    for c, line in enumerate(inF):
        values = line.split()

        if len(values) is 4 and c > 18:
            with open(targetfile, "a") as outF:
                outF.write(values[0] + "," + values[1] + "," + values[2] + "," + values[3] + "\n")


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
                th = float(th)

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

    def visualizeTop():
        plotVal1 = []
        plotVal2 = []
        plotVal3 = []
        targetfile = 'datalyzed/csv/' + testcase + '.csv'
        toolBox.setHeaderTop(targetfile)
        plotVal1, plotVal2, plotVal3 = toolBox.parseTopServer(sourcefile1, plotVal1, plotVal2, plotVal3, targetfile)
        plotVal1, plotVal2, plotVal3 = toolBox.parseTopServer(sourcefile2, plotVal1, plotVal2, plotVal3, targetfile)
        plotVal1, plotVal2, plotVal3 = toolBox.parseTopServer(sourcefile3, plotVal1, plotVal2, plotVal3, targetfile)
        toolBox.visusalizeThreads(titelName, plotVal1, plotVal2, plotVal3, targetfile)

        def parseErrorsWrk2(sourcefile, plotVal1, plotVal2, plotval3, targetfile):
            with open(sourcefile) as inF:
                lines = inF.readlines()

                for i in range(0, len(lines)):
                    line = lines[i]

                    if "Socket errors:" in line:
                        values = lines[i - 1].split()
                        tp = values[4][:-2]
                        tp = float(tp)

                        values = line.split()
                        errCon = values[3][:-1]
                        errRead = values[5][:-1]
                        err = float(errRead) + float(errCon)
                        timeOut = float(values[9])

                        with open(targetfile, "a") as outF:
                            outF.write(str(tp) + "," + str(err) + "," + str(timeOut) + ","
                                       + getContestant(sourcefile) + "\n")

                        plotVal1.append(tp)
                        plotVal2.append(err)
                        plotval3.append(timeOut)

            return plotVal1, plotVal2, plotval3

        def visusalize3ValueSets(titelName, plotVal1, plotVal2, plotval3, testcase):
            canvasTitle = titelName
            valuesList1 = plotVal1
            valuesList2 = plotVal2
            valuesList3 = plotval3
            # valuesList3 = [10,20,30]

            n_groups = 3
            fig, ax = plt.subplots()
            fig.canvas.set_window_title(canvasTitle)

            index = np.arange(n_groups)
            bar_width = 0.20
            opacity = 0.8
            # print len(plotVal1)
            # print plotVal2
            # print plotval3

            rects1 = plt.bar(index + 0.00, valuesList1, bar_width,
                             alpha=opacity,
                             color='#29FE13',
                             label='Throughput in MB')
            rects2 = plt.bar(index + bar_width, valuesList2, bar_width,
                             alpha=opacity,
                             color='#D53BD2',
                             label='Socket Errors')
            rects3 = plt.bar(index + bar_width * 2, valuesList3, bar_width,
                             alpha=opacity,
                             color='c',
                             label='Timeout')

            label_week_lists = ('Perfect', 'Vapor', 'Kitura')

            # plt.ylabel('ms')
            plt.title(canvasTitle)
            plt.xticks(index + bar_width, label_week_lists)
            plt.legend(bbox_to_anchor=(1, 1),
                       bbox_transform=plt.gcf().transFigure)

            autolabel(rects1, ax)
            autolabel(rects2, ax)
            autolabel(rects3, ax)
            plt.show()
            # plt.savefig('datalyzed/img/' + testcase + '.png')



            def visualize1Group():
                plotVal1 = []
                targetfile = 'datalyzed/csv/' + testcase + '.csv'
                plotVal1 = toolBox.parseThreadServer(sourcefile1,plotVal1,targetfile)
                plotVal1 = toolBox.parseThreadServer(sourcefile2, plotVal1, targetfile)
                plotVal1 = toolBox.parseThreadServer(sourcefile3, plotVal1, targetfile)
                toolBox.visusalize1ValueSet(titelName,plotVal1,testcase)



def visusalize1ValueSet(titelName, plotVal1, testcase):
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
                     color='#29FE13',
                     label='Latency')
    # rects2 = plt.bar(index + bar_width, valuesList2, bar_width,
    #                  alpha=opacity,
    #                  color='#D53BD2',
    #                  label='Req/Sec')

    label_week_lists = ('Perfect', 'Vapor', 'Kitura')

    plt.ylabel('ms')
    plt.title(canvasTitle)
    plt.xticks(index + bar_width, label_week_lists)
    plt.legend(bbox_to_anchor=(1, 1),
               bbox_transform=plt.gcf().transFigure)

    autolabel(rects1, ax)
    # autolabel(rects2, ax)

    # plt.savefig('datalyzed/img/' + testcase + '.png')


    def parseThreadServer(sourcefile, plotVal1, targetfile):
        with open(sourcefile) as inF:
            lines = inF.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if "PID" in line:
                    values = lines[i + 1].split()
                    th = values[4]
                    if "/" in th:
                        th.split('/')
                        th = float(th[0])
                    th = float(th)


                    with open(targetfile, "a") as outF:
                        # outF.write(values[2] + "," + values[4] + "," + values[7] + ","
                        #            + getContestant(sourcefile) + "\n")

                        outF.write(str(th) + "," + getContestant(sourcefile) + "\n")

                    plotVal1.append(th)
            return plotVal1


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



    # OLD
    # def visusalizeValueSets(titelName, plotVal1, plotVal2, testcase):
    #     canvasTitle = titelName
    #     valuesList1 = plotVal1
    #     valuesList2 = plotVal2
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
    #     rects2 = plt.bar(index + bar_width, valuesList2, bar_width,
    #                      alpha=opacity,
    #                      color='#D53BD2',
    #                      label='Req/Sec')
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
    #     autolabel(rects2, ax)
    #
    #     plt.savefig('datalyzed/img/' + testcase + '.png')
