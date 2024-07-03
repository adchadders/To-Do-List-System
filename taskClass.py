from datetime import date
class Task:

    def __init__(self, name, description, time_freq, deadline):

        self.name = name
        self.description = description
        self.time_freq = time_freq
        self.deadline = deadline

        self.date_created = date.today()
        self.complete = False
        self.subtasks = []


    def get_name(self):
        return self.name
    
    def set_name(self,new_name):
        self.name = new_name

    
    def get_description(self):
        return self.description
    
    def set_description(self, new_description):
        self.description = new_description


    def get_time_freq(self):
        return self.time_freq
    
    def set_time_freq(self, new_time_freq):
        self.time_freq = new_time_freq

    
    def get_deadline(self):
        return self.deadline
    
    def set_deadline(self, new_deadline):
        self.deadline = new_deadline

    
    def get_complete(self):
        return self.complete
    
    def set_comlete(self, new_complete):
        self.complete = new_complete


    def get_subtasks(self):
        return self.subtasks
    
    def add_subtask(self):
        self.subtasks.append(createTask())




    def print_info(self):
        print("Name: ",self.name)
        print("Description: ",self.description)
        print("Time/Freq: ",self.time_freq)
        print("Deadline: ",self.deadline)
        print("Complete: ",self.complete)

        if self.subtasks != []:
            for task in self.subtasks:
                print("     ",task.name,task.complete)
            