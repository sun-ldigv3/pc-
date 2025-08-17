import tkinter as tk

print("创建最简单的窗口测试...")
root = tk.Tk()
root.title("简单测试")
root.geometry("300x200+100+100")  # 设置窗口大小和位置
root.attributes('-topmost', True)  # 窗口置顶

# 添加一个按钮
btn = tk.Button(root, text="点击我关闭窗口", command=root.quit)
btn.pack(expand=True)

print("即将显示窗口...")
root.mainloop()
print("程序结束")
