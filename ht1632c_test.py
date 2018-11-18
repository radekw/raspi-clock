#!/usr/bin/python3

import time
import random
import ht1632c

CS0_PIN = 20        # Wire to CS pin on board0
CS1_PIN = 21        # Wire to CS pin on board0 & board1
RD_PIN = 0          # DO NOT WIRE
WR_PIN = 19         # Wire to WR pin on board0 & board1
DATA_PIN = 16       # Wire to DATA pin on board0 & board1
VCC = 17            # Wire to VCC pin on board0 & board1
GND = 25            # Wire to GND pin on board0 & board1

def main():
    LED = ht1632c.Driver(WR_PIN, DATA_PIN, CS0_PIN, CS1_PIN)
    LED.POST()

    LED.ScrollString("The quick brown fox jumps over the lazy dog!", 9999, 3)
    
    time.sleep(1)    

    for a in range(0, 99):             # loop 99 times
        for i in range(0, 128, 2):     # because full columns are being populated addresses are even (0x00, 0x02, 0x04 ... 0x7F)
            LED.WriteDataByte(i, random.randrange(0, 0xFF))
        #endfor
    #endfor    
    return
#enddef

if __name__ == '__main__':
    main()
