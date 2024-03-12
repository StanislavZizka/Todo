import tkinter as tk

def get_input():
    input_value = entry.get()
    terminals.insert(tk.END, "Vstup: " + input_value + "\n")



root = tk.Tk()
root.title("To-Do app")


label = tk.Label(root, text="Vstup:")
label.pack()

entry = tk.Entry(root)
entry.pack()

terminals = tk.Text(root, height=10, width=50)
terminals.pack()

button = tk.Button(root, text="Odeslat", command=get_input)
button.pack()







root.mainloop()