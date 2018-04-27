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
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

if not environ.get("DRY_RUN"):
    from epd import epd7in5

EPD_WIDTH = 640
EPD_HEIGHT = 384
TEXT_SIZE = 20
COLOR = 255  # white (255) or black (0)


def truncate(string, max_length):
    return string[:max_length] + (string[max_length:] and '..')


def display_departures(draw, departures):
    font_bold = ImageFont.truetype('Nestor/fonts/Roboto-Bold.ttf', 14)

    x = 0
    y = 350

    departures_string = []
    for departure in departures:
        departures_string.append(departure['time'] + ' ' + departure['delay'] + ' <' + departure['line'] + '>')
    draw.text((x, y), '   •   '.join(departures_string), font=font_bold, fill=COLOR)


def display_calendar(draw, event_list):
    font_bold = ImageFont.truetype('Nestor/fonts/Roboto-Bold.ttf', 14)
    font_light = ImageFont.truetype('Nestor/fonts/Roboto-Light.ttf', 14)

    x = -132
    y = 80

    ongoing_events = []

    weekday = ""
    for event in event_list:
        if not event['ongoing']:
            if weekday != event['weekday']:
                weekday = event['weekday']
                y = 80
                x += 132
                draw.text((x, y), event['weekday'], font=font_bold, fill=COLOR)

            y += TEXT_SIZE
            if event['start_hour'] != '00:00':
                event_test = '• {start_hour}  ({source})'
            else:
                event_test = '• ({source})'

            draw.text((x, y), event_test.format(**event),
                      font=font_bold,
                      fill=COLOR)

            y += TEXT_SIZE
            draw.text((x, y), truncate(event['summary'], 18), font=font_light, fill=COLOR)
        else:
            ongoing_events.append(event)

    ongoing_headline = ' '.join(['-> {summary} [{ongoing_days_left}]'.format(**event) for event in ongoing_events])
    draw.text((0, 50), ongoing_headline, font=font_light, fill=COLOR)


def display_weather(draw, weather):
    font_weather_icons = ImageFont.truetype('Nestor/fonts/weathericons-regular-webfont.ttf', 25)
    font_black = ImageFont.truetype('Nestor/fonts/Roboto-Black.ttf', 24)

    weather_now = weather
    weather_today = weather['today']
    weather_tomorrow = weather['tomorrow']

    # WEATHER NOW
    draw.text((0, 0), weather_now['weather_icon'], font=font_weather_icons, fill=COLOR)
    today_string = weather_now['temp'] + " (" + weather_now['feels_like'] + ")"
    draw.text((40, 0), today_string, font=font_black, fill=COLOR)

    # WEATHER TODAY
    draw.text((180, 0), weather_today['weather_icon'], font=font_weather_icons, fill=COLOR)
    today_string = weather_today['high'] + " / " + weather_today['low']
    draw.text((220, 0), today_string, font=font_black, fill=COLOR)

    # WEATHER TOMORROW
    draw.text((320, 0), weather_tomorrow['weather_icon'], font=font_weather_icons, fill=COLOR)
    tomorrow_string = weather_tomorrow['high'] + " / " + weather_tomorrow['low']
    draw.text((360, 0), tomorrow_string, font=font_black, fill=COLOR)


def black_screen(draw):
    draw.rectangle((0, 0, EPD_WIDTH, EPD_HEIGHT), fill=0)


def display_update_timestamp(draw):
    font_bold = ImageFont.truetype('Nestor/fonts/Roboto-Bold.ttf', 14)

    date_format = "%d-%m-%Y %H:%M"
    now = datetime.now().strftime(date_format)

    draw.text((525, 0), 'Last Refesh', font=font_bold, fill=COLOR)
    draw.text((525, 20), now, font=font_bold, fill=COLOR)


def render(weather, calendar, departures, dry_run):
    image = Image.new('1', (EPD_WIDTH, EPD_HEIGHT), 1)
    draw = ImageDraw.Draw(image)

    black_screen(draw)
    display_update_timestamp(draw)
    # display_weather(draw, weather)
    display_calendar(draw, calendar)
    display_departures(draw, departures)

    if not dry_run:
        push_to_display(image)
    else:
        image.save("display.png", "PNG")


def push_to_display(image):
    epd = epd7in5.EPD()
    epd.init()
    epd.display_frame(epd.get_frame_buffer(image))


def render_test_image():
    from epd import epd7in5
    epd = epd7in5.EPD()
    epd.init()
    image = Image.open('Nestor/images/monocolor.bmp')
    epd.display_frame(epd.get_frame_buffer(image))


def render_black_screen():
    from epd import epd7in5
    epd = epd7in5.EPD()
    epd.init()
    image = Image.new('1', (EPD_WIDTH, EPD_HEIGHT), 1)
    draw = ImageDraw.Draw(image)
    black_screen(draw)
    epd.display_frame(epd.get_frame_buffer(image))
