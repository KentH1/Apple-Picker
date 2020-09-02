#https://pypi.org/project/spidev/
import spidev
spi = spidev.SpiDev()
spi.open(0.0, device) #Connects to the specified SPI device, opening /dev/spidev<bus>.<device>

# # Available Settings
# spi.bits_per_word
# spi.cshigh
# spi.loop #Enables the Loopback mode
# spi.no_cs #Disables chip select
# spi.lsbfirst
# spi.max_speed_hz
# spi.mode #SPI mode as two bit pattern of clock polarity and phase [CPOL|CPHA], min: 0b00 = 0, max: 0b11 = 3
# spi.threewire #Shares SI/SO Signals

spi.readbytes(n) #Read n bytes from SPI device.
spi.close() #Disconnects the SPI