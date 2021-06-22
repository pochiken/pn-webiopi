#   Copyright 2021 pochiken
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import smbus
from time import sleep
from webiopi.utils.types import toint
from webiopi.devices.i2c import I2C
from webiopi.devices.sensor import Temperature,Humidity
i2c = smbus.SMBus(1)

class AM2320(I2C, Temperature, Humidity):
    def __init__(self, slave=0x5C):
        I2C.__init__(self, toint(slave))
        self.__startMeasuring__()
        
    def __str__(self):
        return "AM2320(slave=0x%02X)" % self.slave
            
    def __family__(self):
        return [Temperature.__family__(self), Humidity.__family__(self)]
    
    def __startMeasuring__(self):
        try:
          i2c.write_i2c_block_data(self.slave, 0x00, [])
        except:
          pass
          sleep(.003)
          i2c.write_i2c_block_data(self.slave, 0x03, [0x00, 0x04])
        
    def readRawData(self):
        self.__startMeasuring__()
        sleep(.015)
        data_bytes = i2c.read_i2c_block_data(self.slave, 0, 8)
        sleep(0.25)
        # CRC
        crc = 0xFFFF
        for i in range(6):
          crc ^= data_bytes[i]
          for j in range(8):
            if (crc & 0x0001 == 1):
              crc >>= 1
              crc ^= 0xA001
            else:
              crc >>= 1

        if data_bytes[7] << 8 | data_bytes[6] != crc:
          raise Exception("AM2320(slave=0x%02X): data CRC error" % self.slave)
        else:
          raw_t = float(data_bytes[4] << 8 | data_bytes[5]) / 10
          self.raw_h = float(data_bytes[2] << 8 | data_bytes[3]) / 1000
          return (raw_t)            

    def __getCelsius__(self):
        raw_t = self.readRawData()
        return raw_t
    
    def __getFahrenheit__(self):
        return self.Celsius2Fahrenheit()

    def __getKelvin__(self):
        return self.Celsius2Kelvin()

    def __getHumidity__(self):
        return self.raw_h
       
class AM2321(AM2320):
    def __init__(self, slave = 0x5C):
        AM2320.__init__(self, slave)

    def __str__(self):
        return "AM2321(slave=0x%02X)" % self.slave
