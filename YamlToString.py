# Change the name of the file according to your yaml file.
file_name = "input.yaml"
yaml_file = open(file_name, "r")

yaml_file_lines = yaml_file.read().split('\n')

yamlStr = ""

for line in yaml_file_lines:
    if line.__contains__("\""):
        line = line.replace("\"", "\\\"")
    yamlStr += str(line) + "\\n"

print(yamlStr)
