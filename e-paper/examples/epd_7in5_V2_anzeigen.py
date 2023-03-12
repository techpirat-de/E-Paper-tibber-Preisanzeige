#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd7in5_V2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

def schreibe_display():
    try:
        logging.info("epd7in5_V2 Demo")
        epd = epd7in5_V2.EPD()
        
        logging.info("init and Clear")
        epd.init()
        epd.Clear()

        font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
        font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)

        logging.info("4.read bmp file on window")
        Himage2 = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
        
        # Zeige das Bild auf dem Display an
        bmp = Image.open(os.path.join(picdir, 'chart_von_heute.jpg'))
        Himage2.paste(bmp, (50,10))
        epd.display(epd.getbuffer(Himage2))
        # time.sleep(3600)
        # Bereinige das Display um einbrennen zu vermeiden
        # logging.info("Clear...")
        # epd.init()
        # epd.Clear()
        # Versetze das Display in den Schlafmodus
        # logging.info("Goto Sleep...")
        # epd.sleep()
        
    except IOError as e:
        logging.info(e)
        
    except KeyboardInterrupt:    
        logging.info("ctrl + c:")
        epd7in5_V2.epdconfig.module_exit()
    
    # schreibe_display()
schreibe_display()