from tkinter import *
from tkinter import ttk
class todo:
    def __init__(self, root):
        self.root = root
        self.root.title('TO DO LIST')
        self.root.geometry('650x410+300+150')
        # "To Do List" Title
        self.label = Label(self.root, text='To Do List',
            font=("MN Kunghaeng Bold", 28), width=10,bd=0.5,bg='#f3d9fa', fg='#862e9c')
        self.label.pack(side='top', fill=BOTH)

        # All tasks
        self.main_text = Listbox(self.root, height=5, bd=0.5, width=32, font=("MN Kunghaeng", 25, "bold"), justify="center")
        self.main_text.place(x=40, y=180)

        # Adding task label
        self.text = Text(self.root, bd=0.5, height=1, width=33, font=("MN Kunghaeng", 25, "bold"))
        self.text.place(x=30, y=55)

        def add():
            """ Add contents by append text from Add Text label """
            content = self.text.get(1.0, END)
            print(content)
            self.main_text.insert(END, content)
            with open('data.txt', 'a') as file:
                file.write(content)
                file.seek(0)
                file.close()
            self.text.delete(1.0, END)

        def delete():
            delete_ = self.main_text.curselection()
            look = self.main_text.get(delete_)
            with open('D:\PSCP\PSCP-Project\PSCP-Project\data.txt', 'r+') as f:
                new_f = f.readlines()
                print('-----------------------')
                print(delete_)
                print(look)
                print(new_f)
                print('-----------------------')
                f.seek(0)
                for line in new_f:
                    item = str(look)
                    if item not in line:
                        f.write(line)
                f.truncate()
            self.main_text.delete(delete_)
        with open('D:\PSCP\PSCP-Project\PSCP-Project\data.txt', 'r') as file:
            # readlines -> Taking all text that is separated by line and containing them in a list
            read = file.readlines()
            for i in read:
                ready = i.split()
                self.main_text.insert(-1, ready)
                file.close()
        self.button = Button(self.root, text="Add", font=("MN Kunghaeng Bold", 24),
                    width=8,bd=0.5, bg='#a9e34b', command=add)
        self.button.place(x=70, y=110)
        self.button2 = Button(self.root, text='Delete', font='sarif, 24 bold italic',
                    width=8,bd=0.5, bg='#ff8787', fg='black', command=delete)
        self.button2.place(x=400, y=110)

def main():
    root = Tk()
    ui = todo(root)
    root.mainloop()
if __name__ == "__main__":#เรียกหาหน้าต่าง
    main()
