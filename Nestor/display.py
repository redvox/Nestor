##
#  @filename   :   main.cpp
#  @brief      :   7.5inch e-paper display demo
#  @author     :   Yehui from Waveshare
#
#  Copyright (C) Waveshare     July 28 2017
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documnetation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to  whom the Software is
# furished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS OR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
##


from epd import epd7in5
from PIL import Image, ImageDraw, ImageFont

EPD_WIDTH = 640
EPD_HEIGHT = 384


def display(weather):
    epd = epd7in5.EPD()
    epd.init()

    # clear
    image = Image.new('1', (EPD_WIDTH, EPD_HEIGHT), 1)
    draw = ImageDraw.Draw(image)

    # fonts
    font_thahoma = ImageFont.truetype('Nestor/fonts/tahoma.ttf', 20)
    font_weathericons = ImageFont.truetype('Nestor/fonts/weathericons-regular-webfont.ttf', 25)
    font_black = ImageFont.truetype('Nestor/fonts/Roboto-Black.ttf', 24)
    font_light = ImageFont.truetype('Nestor/fonts/Roboto-Light.ttf', 24)

    weather_now = weather
    weather_today = weather['today']
    weather_tomorrow = weather['tomorrow']

    # WEATHER NOW
    draw.text((0, 0), weather_now['weather_icon'], font=font_weathericons, fill=0)
    today_string = weather_now['temp'] + " (" + weather_now['feels_like'] + ")"
    draw.text((40, 0), today_string, font=font_black, fill=0)

    # WEATHER TODAY
    draw.text((120, 0), weather_today['weather_icon'], font=font_weathericons, fill=0)
    today_string = weather_today['high'] + " / " + weather_today['low']
    draw.text((160, 0), today_string, font=font_black, fill=0)

    # WEATHER TOMORROW
    draw.text((230, 0), weather_tomorrow['weather_icon'], font=font_weathericons, fill=0)
    tomorrow_string = weather_tomorrow['high'] + " / " + weather_tomorrow['low']
    draw.text((270, 0), tomorrow_string, font=font_black, fill=0)

    epd.display_frame(epd.get_frame_buffer(image))

    # print("DRAW")
    # # For simplicity, the arguments are explicit numerical coordinates
    # image = Image.new('1', (EPD_WIDTH, EPD_HEIGHT), 1)  # 1: clear the frame
    # draw = ImageDraw.Draw(image)
    # font = ImageFont.truetype('Nestor/fonts/Roboto-Black.ttf', 24)
    # draw.rectangle((0, 6, 640, 30), fill=0)
    # draw.text((200, 10), 'e-Paper demo', font=font, fill=255)
    # draw.rectangle((200, 80, 600, 280), fill=0)
    # draw.arc((240, 120, 580, 220), 0, 360, fill=255)
    # draw.rectangle((0, 80, 160, 280), fill=255)
    # draw.arc((40, 80, 180, 220), 0, 360, fill=0)
    # print("")
    # epd.display_frame(epd.get_frame_buffer(image))
    #
    # print("IMAGE")
    # image = Image.open('Nestor/images/monocolor.bmp')
    # epd.display_frame(epd.get_frame_buffer(image))