
import os
import zipfile
import tkinter as tk
import sv_ttk

root = tk.Tk()
root.title("Python Compressed Files Extractor")
# root.geometry("600x400")
sv_ttk.set_theme("dark")

path_var = tk.StringVar()
extn_var = tk.StringVar()
extrPath_var = tk.StringVar()


def submit():
    path = path_var.get()
    extn = extn_var.get()
    extrPath = extrPath_var.get()
    path_var.set("")
    extn_var.set("")
    extrPath_var.set("")
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(extn):
                zip_file_path = os.path.join(root, file)
                with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
                    zip_ref.extractall(extrPath)


path_label = tk.ttk.Label(root, text="Root Path of all Compressed Files: ")
path_entry = tk.ttk.Entry(root, textvariable=path_var)

extn_label = tk.ttk.Label(root, text="Compressed File Extension: ")
extn_entry = tk.ttk.Entry(root, textvariable=extn_var)

extrPath_label = tk.ttk.Label(root, text="Location to Store Extracted Data: ")
extrPath_entry = tk.ttk.Entry(root, textvariable=extrPath_var)

sub_btn = tk.ttk.Button(root, text="Extract Files", command=submit)
theme_btn = tk.ttk.Button(root, text="Toggle Theme", command=sv_ttk.toggle_theme)
exit_btn = tk.ttk.Button(root, text="Exit", command=root.destroy)

path_label.grid(row=0, column=0, padx=10)
path_entry.grid(row=0, column=1, pady=5)
extn_label.grid(row=1, column=0)
extn_entry.grid(row=1, column=1, pady=5)
extrPath_label.grid(row=2, column=0)
extrPath_entry.grid(row=2, column=1, pady=5)
sub_btn.grid(row=0, column=2)
theme_btn.grid(row=1, column=2, padx=10)
exit_btn.grid(row=2, column=2)

root.mainloop()
