from tkinter import *
from tkinter import ttk
from FireCommitScript import *

def save():
    pass

def push():
    pass

root = Tk()
root.title("FireCommit - v6.0")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


selected_topic = StringVar()
topic_cb = ttk.Combobox(mainframe, textvariable=selected_topic)
topic_cb['values'] = tuple(getTopicsAsList())
topic_cb['state'] = 'readonly'
topic_cb.grid(column = 1, row = 0, sticky=(W, E))

keywords = StringVar()
keywords_in = ttk.Entry(mainframe, width=7, textvariable=keywords)
keywords_in.grid(column=1, row=1, sticky=(W, E))

ttk.Label(mainframe, text="TOPIC").grid(column=0, row=0, sticky=(W, E))
ttk.Label(mainframe, text="Keywords").grid(column=0, row=1, sticky=(W, E))
ttk.Label(mainframe, text="Author(s)").grid(column=0, row=2, sticky=(W, E))
ttk.Label(mainframe, text="Scope").grid(column=0, row=3, sticky=(W, E))
ttk.Label(mainframe, text="Branch").grid(column=0, row=4, sticky=(W, E))
ttk.Label(mainframe, text="Check").grid(column=0, row=5, sticky=(W, E))

ttk.Button(mainframe, text="Save", command=save).grid(column=0, row=6, sticky=W)
ttk.Button(mainframe, text="Push", command=push).grid(column=1, row=6, sticky=W)

#feet_entry.focus()
#root.bind("<Return>", calculate)
root.mainloop()