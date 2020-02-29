import win32gui

class AppCtrl(object):

    classname = None
    title = None

    def __init__(self):
        self.hWnd = self.getWindow()
    
    def getWindow(self):
        assert(self.classname is not None or self.title is not None)
        return win32gui.FindWindow(self.classname, self.title)

    def getRect(self):
        # (x1, y1, x2, y2)
        # 1920x1080窗口返回(312, 140, 2248, 1259), 即1936x1119
        # 1600x900窗口返回(472, 230, 2088, 1169), 即1616x939
        # 可知窗口比游戏窗口x增加16, y增加39, 在计算时设为偏移量(全屏游戏不受此影响)
        return win32gui.GetWindowRect(self.hWnd)

    def activate(self):
        win32gui.SetForegroundWindow(self.hWnd)
