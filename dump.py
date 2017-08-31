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
