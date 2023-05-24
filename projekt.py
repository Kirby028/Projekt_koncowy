import sys

def parse_arguments():
    if len(sys.argv) != 3:
        print("program.exe pathFile1.x pathFile2.y")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if input_file.endswith(".json"):
        input_format = "json"
    elif input_file.endswith(".yml") or input_file.endswith(".yaml"):
        input_format = "yaml"
    elif input_file.endswith(".xml"):
        input_format = "xml"
    else:
        print("Nieobsługiwany format pliku wejściowego.")
        sys.exit(1)

    if output_file.endswith(".json"):
        output_format = "json"
    elif output_file.endswith(".yml") or output_file.endswith(".yaml"):
        output_format = "yaml"
    elif output_file.endswith(".xml"):
        output_format = "xml"
    else:
        print("Nieobsługiwany format pliku wyjściowego.")
        sys.exit(1)

    return input_file, output_file, input_format, output_format

input_file, output_file, input_format, output_format = parse_arguments()
print("Input file:", input_file)
print("Output file:", output_file)
print("Input format:", input_format)
print("Output format:", output_format)
