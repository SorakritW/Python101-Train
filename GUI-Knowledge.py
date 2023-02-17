from tkinter import *
from tkinter import ttk, messagebox

GUI = Tk() # Comment
GUI.title('โปรแกรมบันทึกข้อมูล')
GUI.geometry('500x400') #นี่คือขนาดโปรแกรม


L1 = Label(GUI,text='โปรแกรมบันทึกความรู้', font=('Angsana New',16),fg='green')
L1.place(x=10,y=20)

#######################
def Show():
    messagebox.showinfo('Show Box','ไม่บอก!!')

def Show2():
    messagebox.showinfo('Show Box','กดปุ่ม 2 ทำไม')

def Show3():
    messagebox.showinfo('Show Box','กดปุ่ม 3 อีกแล้ว')

def Show4():
    messagebox.showerror('Show Box','กดปุ่ม 4 กับ 5 ไม่ได้นะ')
###########################
B1 = ttk.Button(GUI,text='เงินมีอยู่กี่บาท',command=Show)
B1.pack(ipadx=30,ipady=30,pady=50) #.pack = จะที่ Center แล้ว ยืดไป

B2 = ttk.Button(GUI,text='ทำปุ่ม 2 เพิ่มนะ',command=Show2) 
#B2.pack(ipadx=30,ipady=30,pady=50)
B2.place(x=50,y=200)  # ขนาดจะเล็ก เอาไว้ไปกำหนดจุดวางปุ่ม

FB1 = Frame(GUI)  # create frame
FB1.place(x=50,y=300)
B3 = ttk.Button(FB1,text='ทำปุ่ม 3 เพิ่มนะ',command=Show3)  #สร้าง ปุ่มใน FB1 แทน GUI
B3.pack(ipadx=20,ipady=20)  # ขนาดจะเล็ก เอาไว้ไปกำหนดจุดวางปุ่ม


B4 = ttk.Button(GUI,text='ทำปุ่ม 4 เพิ่มนะ',command=Show4)
B4.pack(ipadx=40,ipady=40,pady=50)


FB2 = LabelFrame(GUI)  # create frame
FB2.place(x=400,y=250)
B5 = ttk.Button(FB2,text='ทำปุ่ม 5 เพิ่มนะ',command=Show4)  #สร้าง ปุ่มใน FB2 แทน GUI
B5.pack(ipadx=20,ipady=20)  # ขนาดจะเล็ก เอาไว้ไปกำหนดจุดวางปุ่ม

GUI.mainloop()
