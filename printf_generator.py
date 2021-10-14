# printf_generator - generate printf calls to print long text
# (c) svc64
import sys
if len(sys.argv) != 2:
    print(f"usage: {sys.argv[0]} <text_file>")
else:
    text_file = open(sys.argv[1], 'r')
    for line in text_file.readlines():
        printf_call = "printf(\"" + "%c" * len(line) + "\"" + ''.join([", " + str(ord(c)) for c in line]) + ");"
        print(printf_call)
    text_file.close()
