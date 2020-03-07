import os
from io import BytesIO
from random import randint

from PIL import Image, ImageFont, ImageDraw


class VerifyCode:
    def __init__(self, width=100, height=40, size=4):
        self.width = width
        self.height = height
        self.size = size
        self.__code = ""  # 验证码字符串
        self.pen = None  # 画笔

    @property
    def code(self):
        return self.__code

    def generate(self):
        # 创建画布
        im = Image.new("RGB", (self.width, self.height), self.__rand_color())
        self.pen = ImageDraw.Draw(im)
        # 产生4位随机数
        self.rand_String()
        # 画验证码
        self.__draw_code()
        # 4)、画干扰点
        self.__draw_point()
        # 5)、画干扰线
        self.__rand_line()
        # 6)、返回验证码图片
        # 缓冲区
        buf = BytesIO()
        # 把图片放到缓冲区
        im.save(buf, 'png')
        # 获取图片的二进制
        res = buf.getvalue()
        buf.close()
        im.save("vc.png")
        return res

    def __rand_color(self):
        return (randint(0, 255), randint(0, 255), randint(0, 255))

    def rand_String(self):
        for i in range(self.size):
            self.__code += str(randint(0, 9))

    def __draw_code(self):
        path = os.path.join(os.path.dirname(os.getcwd()), 'static/fonts/simkai.ttf')
        font = ImageFont.truetype(path, size=20, encoding="utf-8")
        # 计算字符宽度
        width = (self.width - 20) // self.size
        # 逐个字符画
        for i in range(len(self.__code)):
            x = 13 + width * i  # 计算每个字符的x坐标
            self.pen.text((x, 9), self.__code[i], font=font, fill=self.__rand_color())

    def __draw_point(self):
        for i in range(150):
            self.pen.point((randint(1, self.width - 1), randint(1, self.height - 1)), self.__rand_color())

    def __rand_line(self):
        for i in range(5):
            self.pen.line([(randint(1, self.width - 1), randint(1, self.height - 1)),
                           (randint(1, self.width - 1), randint(1, self.height - 1))], fill=self.__rand_color(),
                          width=1)


vc = VerifyCode()