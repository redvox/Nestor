# coding=utf-8
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
from os import environ

if not environ.get("DRY_RUN"):
    from epd import epd7in5

from PIL import Image, ImageDraw, ImageFont

EPD_WIDTH = 640
EPD_HEIGHT = 384


def truncate(string, max_length):
    return string[:max_length] + (string[max_length:] and '..')


def display_departures(draw, departures):
    font_bold = ImageFont.truetype('Nestor/fonts/Roboto-Bold.ttf', 14)

    x = 0
    y = 350

    departures_string = []
    for departure in departures:
        departures_string.append(departure['time'] + ' ' + departure['delay'] + ' <' + departure['line'] + '>')
    draw.text((x, y), '   •   '.join(departures_string), font=font_bold, fill=0)


def display_calendar(draw, calendar):
    font_bold = ImageFont.truetype('Nestor/fonts/Roboto-Bold.ttf', 14)
    font_light = ImageFont.truetype('Nestor/fonts/Roboto-Light.ttf', 14)

    x = -132
    y = 50

    weekday = ""
    for event in calendar:
        text_size_px = 20

        if weekday != event['weekday']:
            weekday = event['weekday']
            y = 50
            x += 132
            draw.text((x, y), event['weekday'], font=font_bold, fill=0)

        y += text_size_px
        if event['start_hour'] != '00:00':
            event_test = '• {start_hour}  ({source})'
        else:
            event_test = '• ({source})'

        draw.text((x, y), event_test.format(**event),
                  font=font_bold,
                  fill=0)

        y += text_size_px
        draw.text((x, y), truncate(event['summary'], 18), font=font_light, fill=0)


def display_weather(draw, weather):
    font_weather_icons = ImageFont.truetype('Nestor/fonts/weathericons-regular-webfont.ttf', 25)
    font_black = ImageFont.truetype('Nestor/fonts/Roboto-Black.ttf', 24)

    weather_now = weather
    weather_today = weather['today']
    weather_tomorrow = weather['tomorrow']

    # WEATHER NOW
    draw.text((0, 0), weather_now['weather_icon'], font=font_weather_icons, fill=0)
    today_string = weather_now['temp'] + " (" + weather_now['feels_like'] + ")"
    draw.text((40, 0), today_string, font=font_black, fill=0)

    # WEATHER TODAY
    draw.text((180, 0), weather_today['weather_icon'], font=font_weather_icons, fill=0)
    today_string = weather_today['high'] + " / " + weather_today['low']
    draw.text((220, 0), today_string, font=font_black, fill=0)

    # WEATHER TOMORROW
    draw.text((320, 0), weather_tomorrow['weather_icon'], font=font_weather_icons, fill=0)
    tomorrow_string = weather_tomorrow['high'] + " / " + weather_tomorrow['low']
    draw.text((360, 0), tomorrow_string, font=font_black, fill=0)


def render(now, weather, calendar, departures):
    # clear
    image = Image.new('1', (EPD_WIDTH, EPD_HEIGHT), 1)
    draw = ImageDraw.Draw(image)

    # fonts
    font_weathericons = ImageFont.truetype('Nestor/fonts/weathericons-regular-webfont.ttf', 25)
    font_black = ImageFont.truetype('Nestor/fonts/Roboto-Black.ttf', 24)
    font_thahoma = ImageFont.truetype('Nestor/fonts/tahoma.ttf', 12)
    font_bold = ImageFont.truetype('Nestor/fonts/Roboto-Bold.ttf', 14)
    font_light = ImageFont.truetype('Nestor/fonts/Roboto-Light.ttf', 14)

    # UPDATE DATE
    draw.text((525, 0), 'Last Refesh', font=font_bold, fill=0)
    draw.text((525, 20), now, font=font_bold, fill=0)

    display_weather(draw, weather)
    display_calendar(draw, calendar)
    display_departures(draw, departures)

    if not environ.get("DRY_RUN"):
        push_to_display(image)
    else:
        image.save("display.png", "PNG")


def push_to_display(image):
    epd = epd7in5.EPD()
    epd.init()
    epd.display_frame(epd.get_frame_buffer(image))
