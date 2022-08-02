
### 73 WEI 20220802
import tkinter as tk
import tkinter.messagebox as tkMessageBox

win = tk.Tk()
win.geometry("400x400")
win.configure(bg='#303841')

tkMessageBox.showinfo("Entry","Missing file.")
tkMessageBox.showwarning("ERROR","Warning!!!")
tkMessageBox.showerror("Auto","Check your files")
result=tkMessageBox.askquestion("Recover","Download?")
print(result)

label1 =tk.Label(win,text="Successfully installed.",fg="#79a8a9",bg='#303841')
label1.place(x=50, y=50)
tk.Label(win,text="Chart",width=30,height=17,fg="#79a8a9",bg='#232931').place(x=480, y=90)

win.mainloop()

# Hello