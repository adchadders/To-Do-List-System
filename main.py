class Task:
    def __init__(self, name, description, time, repeat):
        self.name = name
        self.description = description
        self.time = time
        self.repeat = repeat
        
        self.complete = False
        self.subtasks = []

    def add_subtask(self, sub_name, sub_description, sub_time, sub_repeat):
        subtask = Task(sub_name, sub_description, sub_time, sub_repeat)
        self.subtasks.append(subtask)

    def label_complete(self):
        self.complete = True

    def label_incomplete(self):
        self.complet = False

    def list_subtasks(self):
        for subtask in self.subtasks:
            print(subtask.name)



toDo = Task("To do list", "",0, True)

toDo.add_subtask("Laundry", "Clean Clothes", 10, True)

toDo.list_subtasks()


