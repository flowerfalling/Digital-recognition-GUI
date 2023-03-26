# -*- coding: utf-8 -*-
# @Time    : 2023/3/26 20:42
# @Author  : 之落花--falling_flowers
# @File    : main.py
# @Software: PyCharm
import tkinter as tk


class App:
    def __init__(self):
        self.line_id = None
        self.line_points = []
        self.root = tk.Tk()
        self.root.title('手写数字识别器')
        self.root.resizable(width=False, height=False)
        self.canvas = tk.Canvas(height=368, width=368, relief='groove', bd=2)
        self.canvas.pack()
        self.text = tk.StringVar(self.root, '数字:')
        self.canvas.bind('<Button-1>', self.set_start)
        self.canvas.bind('<B1-Motion>', self.draw_line)
        self.canvas.bind('<ButtonRelease-1>', self.end_line)
        self.root.mainloop()

    def draw_line(self, event):
        self.line_points.extend((event.x, event.y))
        if self.line_id is not None:
            self.canvas.delete(self.line_id)
        self.line_id = self.canvas.create_line(self.line_points, width=30)

    def set_start(self, event):
        self.line_points.extend((event.x, event.y))

    def end_line(self, _):
        self.line_points.clear()
        self.line_id = None


def main():
    App()
    pass


if __name__ == '__main__':
    main()
