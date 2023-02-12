from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from GenderIdentifier import GenderIdentifier


def test():
    if model_chosen.get() == '[请选择模型]':
        messagebox.showinfo(title='提示', message='请选择一个模型')
    else:
        gender_identifier = GenderIdentifier("1.wav", model_chosen.get())
        result = gender_identifier.process()
        show.config(text=result[0] + ' ' + result[1])


# 创建主窗口
win = Tk()
win.title("基于MFCC的说话人性别识别系统")
sw = win.winfo_screenwidth()
sh = win.winfo_screenheight()
ww = 400
wh = 230
x = (sw - ww) / 2
y = (sh - wh) / 2
win.geometry("%dx%d+%d+%d" % (ww, wh, x, y))

# 添加文本内,设置字体的前景色和背景色，和字体类型、大小
title = Label(win, text="基于MFCC的说话人性别识别系统", bg="yellow", fg="red", font=('Times', 16, 'bold italic'))
# 将文本内容放置在主窗口内
title.grid(row=0, padx=35, pady=0)

# 模型选择下拉框
model_chosen = ttk.Combobox(win)
# 使用 grid() 来控制控件的位置
model_chosen.grid(row=1, sticky="w", padx=35, pady=20)
# 设置下拉菜单中的值
model_chosen['value'] = ('[请选择模型]', 'GMM', 'HMM')
model_chosen.current(0)

Button(win, text="预测", width=10, command=test).grid(row=1, sticky="e", padx=35, pady=20)

show = Label(win, text='[结果显示处]', font=('Arial', 16))
show.grid()
manual = Label(win, text='使用说明：\n'
                         '1.将待测音频置于本目录下并命名为1.wav\n'
                         '2.在下拉框中选择一种模型并点击“预测”按钮', fg="blue")
manual.grid(padx=35, pady=10)

# 调用主事件循环，让窗口程序保持运行。
win.mainloop()
