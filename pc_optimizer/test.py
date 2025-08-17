import tkinter as tk
from tkinter import messagebox

print("开始创建测试窗口...")
root = tk.Tk()
print("设置窗口标题...")
root.title("测试窗口")
print("设置窗口大小...")
root.geometry("300x200")
print("创建标签...")
label = tk.Label(root, text="如果你能看到这个窗口，说明tkinter工作正常！")
label.pack(pady=20)
print("创建按钮...")
btn = tk.Button(root, text="点击我", command=lambda: messagebox.showinfo("提示", "按钮点击成功！"))
btn.pack()
print("启动主循环...")
root.mainloop()
print("程序结束...")
