class FileHandler:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def read_file(self):
        try:
            with open(self.input_file, 'r', encoding='utf-8') as file:
                content = file.read()
            return content
        except FileNotFoundError:
            print(f"Error: File '{self.input_file}' not found.")
            return ""

    def write_file(self, content):
        with open(self.output_file, 'w', encoding='utf-8') as file:
            file.write(content)
