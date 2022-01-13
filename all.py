from tkinter import*

root = Tk()
root.title("Menue")
root.configure(bg="black")
root.geometry("150x380")
root.maxsize(150,380)
root.minsize(150,380)

Button(text="Browser", pady=20, padx=10, width=20).pack(anchor="nw")
Button(text="Calculator", pady=20, padx=10, width=20).pack(anchor="nw")
Button(text="Text Editor", pady=20, padx=10, width=20).pack(anchor="nw")
Button(text="Media", pady=20, padx=10, width=20).pack(anchor="nw")
Button(text="Weather", pady=20, padx=10, width=20).pack(anchor="nw")
Button(text="Clock", pady=20, padx=10, width=20).pack(anchor="nw")



root.mainloop()