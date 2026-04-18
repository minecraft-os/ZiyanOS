import ctypes
import tkinter as tk

# 模拟 Win + Space 切换输入法
def win_space_switch():
    user32 = ctypes.WinDLL('user32', use_last_error=True)

    # 按键对应值
    VK_LWIN = 0x5B
    VK_SPACE = 0x20
    KEYEVENTF_KEYUP = 0x0002

    # 按下 Win
    user32.keybd_event(VK_LWIN, 0, 0, 0)
    # 按下空格
    user32.keybd_event(VK_SPACE, 0, 0, 0)
    # 松开空格
    user32.keybd_event(VK_SPACE, 0, KEYEVENTF_KEYUP, 0)
    # 松开 Win
    user32.keybd_event(VK_LWIN, 0, KEYEVENTF_KEYUP, 0)

# 可拖动悬浮窗
class FloatWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.overrideredirect(True)        # 无边框
        self.attributes('-topmost', True)  # 置顶
        self.attributes('-alpha', 0.90)    # 半透明
        self.geometry('220x90+100+100')
        self.config(bg='#333333')

        # 拖动支持
        self.bind('<Button-1>', self.start_drag)
        self.bind('<B1-Motion>', self.on_drag)

        # 界面
        tk.Label(self, text='输入法切换', fg='white', bg='#333', font=('微软雅黑', 10)).pack(pady=2)
        tk.Button(self, text='切换输入法（Win+Space）',
                  bg='#0078D4', fg='white',
                  command=win_space_switch).pack(pady=5, padx=10, fill=tk.X)

    def start_drag(self, e):
        self._x = e.x
        self._y = e.y

    def on_drag(self, e):
        deltax = e.x - self._x
        deltay = e.y - self._y
        self.geometry(f'+{self.winfo_x() + deltax}+{self.winfo_y() + deltay}')

if __name__ == '__main__':
    app = FloatWindow()
    app.mainloop()