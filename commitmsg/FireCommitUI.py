from tkinter import *
from tkinter import ttk
from funcs import *
from functools import partial


root = Tk()
root.title("FireCommit - v6.0")
root.geometry("880x540")
#root.columnconfigure(0, weight=1)
#root.rowconfigure(0, weight=1)
tabs = ttk.Notebook(root)
tabs.pack(fill=BOTH, expand=True)
fr_1 = ttk.Frame(tabs)
fr_2 = ttk.Frame(tabs)
tabs.add(fr_1, text="COMMSG")
tabs.add(fr_2, text="LOG")

#mainframe = ttk.Frame(root, padding="3 3 12 12")
#tabs.grid(sticky=(W, E))

fr_1_1 = ttk.LabelFrame(fr_1, text="Topic & Keywords") #borderwidth = 2, relief=SOLID
fr_1_1['padding'] = (5,10,5,10)
fr_1_1.grid(column=0, row=0, padx=10, pady=10, sticky="nsew")
#fr_1_1.place(relx=0.5, rely=0, anchor=N)

fr_1_2 = ttk.LabelFrame(fr_1, text="Author & Branch")
fr_1_2['padding'] = (5,10,5,10)
fr_1_2.grid(column=0, row=1, padx=10, pady=10, sticky="nsew")
#fr_1_2.place(relx=0.5, rely=0.5, anchor=CENTER)

fr_1_3 = ttk.LabelFrame(fr_1, text="Check & Push")
fr_1_3['padding'] = (5,10,5,10)
fr_1_3.grid(column=0, row=2, padx=10, pady=10, sticky="nsew")
#fr_1_3.place(relx=0.5, rely=0.99, anchor=S)

### Frame 1_1
selected_topic = StringVar()
topic_cb = ttk.Combobox(fr_1_1, textvariable=selected_topic)
topic_cb['values'] = tuple(getTopicsAsList())
topic_cb['state'] = 'readonly'
topic_cb.grid(column = 1, row = 0, sticky=(W, E))

keywords = StringVar()
keywords_in = ttk.Entry(fr_1_1, width=7, textvariable=keywords)
keywords_in.grid(column=1, row=1, sticky=(W, E))

ttk.Label(fr_1_1, text="TOPIC").grid(column=0, row=0, sticky=(W, E))
ttk.Label(fr_1_1, text="Keywords").grid(column=0, row=1, sticky=(W, E))
###


### Frame 1_2
selected_author = StringVar()
author_cb = ttk.Combobox(fr_1_2, textvariable=selected_author)
author_cb['values'] = getAuthorAsList()
author_cb['state'] = 'readonly'
author_cb.grid(column = 1, row = 0, sticky=(W, E))

selected_branch = StringVar()
branch_cb = ttk.Combobox(fr_1_2, textvariable=selected_branch)
branch_cb['values'] = getBranchAsList()
branch_cb['state'] = 'readonly'
branch_cb.grid(column = 1, row = 1, sticky=(W, E))

ttk.Label(fr_1_2, text="Author").grid(column=0, row=0, sticky=(W, E))
ttk.Label(fr_1_2, text="Branch").grid(column=0, row=1, sticky=(W, E))
ttk.Label(fr_1_2, text="Changes").grid(column=0, row=2, sticky=(W, E))

changes_1 = StringVar()
changes_2 = StringVar()
changes_3 = StringVar()
changes_1 = ttk.Entry(fr_1_2, width=10, textvariable=changes_1)
changes_2 = ttk.Entry(fr_1_2, width=10, textvariable=changes_2)
changes_3 = ttk.Entry(fr_1_2, width=10, textvariable=changes_3)
changes_1.grid(column=1, row=2, sticky=(W, E))
changes_2.grid(column=1, row=3, sticky=(W, E))
changes_3.grid(column=1, row=4, sticky=(W, E))
###



### Frame 1_3
ttk.Label(fr_1_3, text="Check1").grid(column=0, row=0, sticky=(W, E))
ttk.Label(fr_1_3, text=check1()).grid(column=1, row=0, sticky=(W, E))
ttk.Label(fr_1_3, text="Check2").grid(column=0, row=1, sticky=(W, E))
ttk.Label(fr_1_3, text=check2()).grid(column=1, row=1, sticky=(W, E))
ttk.Label(fr_1_3, text="Check3").grid(column=0, row=2, sticky=(W, E))
ttk.Label(fr_1_3, text=check3()).grid(column=1, row=2, sticky=(W, E))
commit_with_args = partial(commit, selected_topic, keywords, selected_author, selected_branch, [changes_1, changes_2, changes_3])
ttk.Button(fr_1_3, text="Save", command=save).grid(column=0, row=3, sticky=W)
ttk.Button(fr_1_3, text="Commit", command=commit_with_args).grid(column=1, row=3, sticky=W)
ttk.Button(fr_1_3, text="Push", command=push).grid(column=2, row=3, sticky=W)
###


#feet_entry.focus()
#root.bind("<Return>", calculate)

for x in [fr_1_1, fr_1_2, fr_1_3]:
    for widget in x.winfo_children():
        widget.grid_configure(padx=10, pady=5)

root.mainloop()