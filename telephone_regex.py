'''
Note: if program does not run in Python 3, try running using Python 2
'''
import re
import sys

def main():
    if len(sys.argv) == 1:
        sys.argv = [sys.argv[0], "test_dollar_phone_corpus.txt", "telephone_output.txt"]
    if len(sys.argv) == 3:
        INPUT_FILE = str(sys.argv[1])
        OUTPUT_FILE = str(sys.argv[2])
    else:
        print ("Invalid use, only use two commands.")
        return

    FULL_PATTERN_PHONE = re.compile('|'.join([
      r'\(\d{3}\)[\s]\d{3}[\s-]\d{4}', # (123) 123-1234
      r'\(\d{3}\)[-]\d{3}[\s-]\d{4}', # (123)-123-1234
      r'\d{3}[-]\d{3}[\s-]\d{4}' # 123-123-1234
    ]), re.IGNORECASE)

    PATTERN = ""
    counter = 0

    try:
        input_file = INPUT_FILE
        output_file = open(OUTPUT_FILE, 'w+')
        print ("Reading from file: " + INPUT_FILE + "...")
        PATTERN = FULL_PATTERN_PHONE
        matches = open("telephone_output.txt", "w+")

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
