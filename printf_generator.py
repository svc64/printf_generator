# printf_generator - generate printf calls to print long text
# (c) svc64
import sys
if len(sys.argv) != 2:
    print(f"usage: {sys.argv[0]} <text_file>")
else:
    text_file = open(sys.argv[1], 'r')
    text_lines = text_file.readlines()
    text_file.close()
    for line in text_lines:
        printf_call = "printf(\"" + "%c" * len(line) + "\"" + ''.join([", " + str(ord(c)) for c in line]) + ");"
        print(printf_call)
