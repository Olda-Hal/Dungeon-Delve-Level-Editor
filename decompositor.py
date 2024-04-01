def main(args):
    code = []
    with open(args.file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.endswith(":\n"):
                print("Found block: " + line)
                code.append(CodeBlock(line))

        print(lines)

class CodeBlock:
    def __init__(self, name):
        self.name = name
        self.lines = []
    