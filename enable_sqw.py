#!/usr/bin/python

import SDL_DS3231
ds3231 = SDL_DS3231.SDL_DS3231(1, 0x68)
bin(ds3231._read(0x0e))[2:].zfill(8)
ds3231._write(0x0e, 0b00000000)
bin(ds3231._read(0x0e))[2:].zfill(8)

