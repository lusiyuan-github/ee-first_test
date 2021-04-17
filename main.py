import sensor, image, time, math
from move import MOVE
from pid import PID
from pyb import Servo
i = 80	#云台T方向上的运动角度
j = 95	#云台P方向上的运动角度
flag = 0 	#设置标志位
counter = 0 	#设置记数位
pan_servo=Servo(1)
tilt_servo=Servo(2)
pan_servo.calibration(500,2500,500)
tilt_servo.calibration(500,2500,500)

pan_pid = PID(p=0.07, i=0.015, imax=90)
tilt_pid = PID(p=0.05, i=0.015, imax=90)
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)	#160*120
sensor.skip_frames(10)
sensor.set_auto_whitebal(False)	#便于识别而取消白平衡
clock = time.clock()
def find_max(blobs):
	max_size=0
	for blob in blobs:
		if blob[2]*blob[2] > max_size:
			max_blob=blob
			max_size = blob[2]*blob[2]
	return max_blob
while(True):
	clock.tick()
	img = sensor.snapshot()
	img.draw_cross(80,60)	#中心画十字为激光重合
	blobs = img.find_circles(threshold = 3000, x_margin = 10, y_margin = 10)
	if blobs:
		counter = 0
		max_blob = find_max(blobs)
		print("X: ", max_blob[0])
		print("Y: ", max_blob[1])
		pan_error = max_blob[0]-img.width()/2
		tilt_error = max_blob[1]-img.height()/2
		print("pan_error: ", pan_error)
		print("tilt_error: ", tilt_error)
		img.draw_circle(max_blob.x(),max_blob.y(),max_blob.r(),color=(255,0,0))	#画出圆
		img.draw_cross(int(max_blob[0]),int(max_blob[1]))	#画出圆心
		pan_output=pan_pid.get_pid(pan_error,1)
		tilt_output=tilt_pid.get_pid(tilt_error,1)
		print("pan_output",pan_output)
		print("tilt_output",tilt_output)
		print("pan_output_angle",pan_servo.angle())
		print("tile_output_angle",tilt_servo.angle())
		print("r=",max_blob.r())
		if abs(pan_error)>5 and abs(tilt_error)>5:	#误差过小时停止调整
			pan_servo.angle(pan_servo.angle()-pan_output)
			tilt_servo.angle(tilt_servo.angle()+tilt_output)
		if abs(pan_error)<=5 and abs(tilt_error)>5:
			tilt_servo.angle(tilt_servo.angle()+tilt_output)
		if abs(pan_error)>5 and abs(tilt_error)<=5:
			pan_servo.angle(pan_servo.angle()-pan_output)
		if abs(pan_error)<=5 and abs(tilt_error)<=5:
			continue
	else:
		counter+=1
		if counter==10:
			counter = 0
			flag = MOVE.move_ninepoint(flag, pan_servo, tilt_servo)#九点轮训扫描
	print(flag)
	print(pan_servo.angle())
	print(clock.fps())
	#print 处均为数据监测