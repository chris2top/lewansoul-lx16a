import serial
import lewansoul_lx16a

SERIAL_PORT = '/dev/ttyUSB0'

controller = lewansoul_lx16a.ServoController(
    serial.Serial(SERIAL_PORT, 115200, timeout=1),
)

# control servos directly
#controller.move(1, 100) # move servo ID=1 to position 100

# or through proxy objects
servo1 = controller.servo(1)
#servo2 = controller.servo(2)

servo1.move(0)

# synchronous move of multiple servos
#servo1.move_prepare(300)
#servo2.move_prepare(600)
#controller.move_start()
