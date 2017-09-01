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