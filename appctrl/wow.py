import time
import pyautogui as gui
from . import AppCtrl
from utils.screenshot import regionMatchesColor


class WowClassicApp(AppCtrl):
    title = "魔兽世界"

    def __init__(self, hWnd = None):
        super().__init__()
        if (hWnd is not None):
            self.hWnd = hWnd

    def isCharacterSelect(self):
        """Test if in Character Select screen.
        """
        # 只适合16:9分辨率
        rect = self.getRect()
        return regionMatchesColor((rect[0] + ((rect[2] - rect[0]) / 1936) * 865, rect[1] + ((rect[3] - rect[1]) / 1119) * 1024, 10, 10), (120, 17, 17), 16)

    def isLoginScreen(self):
        # 1920x1080窗口, (20, 60, 30, 70)区域内颜色为#000
        rect = self.getRect()
        return regionMatchesColor((rect[0] + ((rect[2] - rect[0]) / 1936) * 20, rect[1] + ((rect[3] - rect[1]) / 1119) * 60, 10, 10), (0, 0, 0), 16)

    def enterGame(self):
        self.activate()
        rect = self.getRect()
        gui.moveTo(rect[0] + ((rect[2] - rect[0]) / 1936) * 860, rect[1] + ((rect[3] - rect[1]) / 1119) * 990, 1)
        gui.click()

    def antiIdle(self):
        self.activate()
        gui.keyDown('w')
        time.sleep(0.05)
        gui.keyUp('w')
        gui.keyDown('s')
        time.sleep(0.05)
        gui.keyUp('s')
