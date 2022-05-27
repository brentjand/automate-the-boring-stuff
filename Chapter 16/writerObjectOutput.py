import csv

outputFile = open('output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
outputWriter.writerow([1, 2, 3.141592, 4])
outputFile.close()


# If the newline='' argument is not used, the rose in output.csv will be double-spaced, meaning 1 row will be skipped between
# each data record (row).