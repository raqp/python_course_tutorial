class Notebook:

    def __init__(self, name, color, memory):
        self.name = name
        self.color = color
        self.memory = memory
        self.programs = []

    def show_info(self):
        print(f"Notebook: {self.name}\nColor: {self.color}\nMemory: {self.memory}")

    def install(self, program):
        print(f"Start to install {program}")
        self.programs.append(program)
        print("Instalation finished.")

    def uninstall(self, program):
        self.programs.remove(program)


notebook_1 = Notebook("Dell", "black", "500GB")
notebook_1.install("Google Chrome")

notebook_2 = Notebook("Lenovo", "red", "500GB")


