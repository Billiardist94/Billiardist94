my_file = input('Enter file name: ')
class File():
    def __init__(self, text, files):
        self.text = text
        self.files = files

    def read_file(self, *args):
        file = open(self.files, 'r')
        print(file.read(*args))
        file.close()

    def write_file(self):
        file = open(self.files, 'w')
        file.write(self.text)
        file.close()

    def append_to_file(self):
        file = open(self.files, 'a')
        file.write(self.text)
        file.close()

notepad = File(input('Enter text: '), my_file)
notepad.write_file()
notepad.read_file()
