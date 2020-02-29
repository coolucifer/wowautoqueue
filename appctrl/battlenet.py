import time
import pyautogui as gui
import win32gui

from . import AppCtrl

class BattleNetApp(AppCtrl):
    classname = 'Qt5QWindowOwnDCIcon'

    def start_game(self):
        hWnd = self.getWindow()
        rect = self.getRect()

        click_pos = (rect[0] + 320, rect[3] - 60)

        self.activate()
        gui.moveTo(*click_pos, 1)
        gui.click()
        gui.moveTo(100, 100)

    def select_account(self, index):
        # 选择从最下往上数第x个wow账号
        hWnd = self.getWindow()
        rect = self.getRect()

        # wow选择按钮位置
        account_btn_pos = (rect[0] + 475, rect[3] - 130)
        # wow_x 位置
        # 从下往上数, 第一个wow y是 rect3 - 170, 第二个wow y是 rect3 - 200
        # 账号只有两个wow, 多出来的修改对应值
        wow_x_pos = (rect[0] + 475, rect[3] - (140 + 30 * index))

        self.activate()
        gui.moveTo(*account_btn_pos, 1)
        gui.click()
        gui.moveTo(*wow_x_pos, .5)
        gui.click()



