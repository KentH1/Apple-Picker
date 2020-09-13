from mpu6050 import mpu6050
import time
mpu = mpu6050(0x68)

while True:
    accel_data=mpu.get_accel_data()
    print("ACC X: "+str(accel_data['x']))
    print("ACC Y: "+str(accel_data['y']))
    print("ACC Z: "+str(accel_data['z']))
    
    gyro_data=mpu.get_gyro_data()
    print("Gyro X: "+str(gyro_data['x']))
    print("Gyro Y: "+str(gyro_data['y']))
    print("Gyro Z: "+str(gyro_data['z']))
    print("---------------------------")
    time.sleep(1)
