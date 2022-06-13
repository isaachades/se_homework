import pyperclip
import time


# 稳定不出错
class clipboard():
    def getClipboard(self):
        while True:
            t = listener().main()
            print(t)


class listener():
    def clipboard_get(self):
        """获取剪贴板数据"""
        data = pyperclip.paste()
        return data

    def main(self):
        # 后台脚本：每隔0.2秒，读取剪切板文本，检查有无指定字符或字符串，如果有则执行替换
        # recent_txt 存放最近一次剪切板文本，初始化值只多执行一次paste函数读取和替换
        recent_txt = self.clipboard_get()
        while True:
            # txt 存放当前剪切板文本
            txt = self.clipboard_get()
            # 剪切板内容和上一次对比如有变动，再进行内容判断，判断后如果发现有指定字符在其中的话，再执行替换
            if txt != recent_txt:
                recent_txt = txt  # 没查到要替换的子串，返回None
                return recent_txt

                # 检测间隔（延迟0.2秒）
            time.sleep(0.2)


if __name__ == '__main__':
    clipboard().getClipboard()