from threading import Thread

def show():
    print("This is child thread ")

t = Thread(target= show())
t.start()
print("This is the parent or default thread")
