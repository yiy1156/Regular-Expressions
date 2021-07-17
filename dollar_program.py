'''
Note: if program does not run in Python 3, try running using Python 2
'''
import re
import sys

def main():
    if len(sys.argv) == 1:
        sys.argv = [sys.argv[0], "test_dollar_phone_corpus.txt", "dollar_output.txt"]
    if len(sys.argv) == 3:
        INPUT_FILE = str(sys.argv[1])
        OUTPUT_FILE = str(sys.argv[2])
    else:
        print ("Invalid use, only use two commands.")
        return

    FULL_PATTERN_DOLLARS = re.compile('|'.join([
      r'[\$][\d{1,3}]\,\d{1,3}\,\d{1,3}', # $1,000,000
      r'[\$][\d{1,3}]\,\d{1,3}\.\d{1,2}', # $100,000.00, $10,000.00
      r'[\$][\d{1,5}]\.\d{1,2}', # $10000.00
      r'[\$](\d+\.\d{1,2})',  # $.50, $1.50
      r'[\$][\d{1,3}]\,\d{1,3}', #$100,000, $10,000, 1,000
      r'billion|billions',
      r'trillion|trillions',
      r'million|millions'
    ]), re.IGNORECASE)

    PATTERN = ""
    counter = 0

    try:
        input_file = INPUT_FILE
        output_file = open(OUTPUT_FILE, 'w+')
        print ("Reading from file: " + INPUT_FILE + "...")
        PATTERN = FULL_PATTERN_DOLLARS
        matches = open("dollar_output.txt", "w+")

        newLine = ""

        for i, line in enumerate(open(input_file)):
            newLine = line
            for match in re.finditer(PATTERN, line):
                counter += 1
                matches.write(match.group(0)+"\n")
                newLine = line.replace(match.group(0), "[" + match.group(0) + "]")

            output_file.write(newLine)

        print (str(counter) + " lines written to " + OUTPUT_FILE)

    except IOError:
        print ("File not found.")

main()
