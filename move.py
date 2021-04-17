class MOVE:
	def move_ninepoint(flag, pan_servo, tilt_servo): #按九固定点扫描方式
		if flag == 0:
			pan_servo.angle(100)
			tilt_servo.angle(80)
			flag = 1
		elif flag == 1:
			pan_servo.angle(100)
			tilt_servo.angle(90)
			flag = 2
		elif flag == 2:
			pan_servo.angle(100)
			tilt_servo.angle(100)
			flag = 3
		elif flag == 3:
			pan_servo.angle(90)
			tilt_servo.angle(100)
			flag = 4
		elif flag == 4:
			pan_servo.angle(90)
			tilt_servo.angle(90)
			flag = 5
		elif flag == 5:
			pan_servo.angle(90)
			tilt_servo.angle(80)
			flag = 6
		elif flag == 6:
			pan_servo.angle(80)
			tilt_servo.angle(80)
			flag = 7
		elif flag == 7:
			pan_servo.angle(80)
			tilt_servo.angle(90)
			flag = 8
		elif flag == 8:
			pan_servo.angle(80)
			tilt_servo.angle(100)
			flag = 0

	def move_coiled(flag, pan_servo, tilt_servo,i,j):  # 按连续范围扫描方式
		if flag == 0:
			pan_servo.angle(j)
			tilt_servo.angle(i)
			time.sleep_ms(500)
			i += 1
			if i == 100:
				flag = 1
		if flag == 1:
			pan_servo.angle(j)
			tilt_servo.angle(i)
			time.sleep_ms(500)
			j -= 1
			if j == 85:
				flag = 2
		if flag == 2:
			pan_servo.angle(j)
			tilt_servo.angle(i)
			time.sleep_ms(500)
			i -= 1
			if i == 85:
				flag = 3
		if flag == 3:
			pan_servo.angle(j)
			tilt_servo.angle(i)
			time.sleep_ms(500)
			j += 1
			if j == 100:
				flag = 0
		return [flag,i,j]
	def move_multipoint(flag, pan_servo, tilt_servo,i,j):  # 按口型多点监测
		if flag == 0:
			pan_servo.angle(j)
			tilt_servo.angle(i)
			i += 5
			if i == 105:
				flag = 1
		if flag == 1:
			pan_servo.angle(j)
			tilt_servo.angle(i)
			time.sleep_ms(500)
			j -= 5
			if j == 80:
				flag = 2
		if flag == 2:
			pan_servo.angle(j)
			tilt_servo.angle(i)
			time.sleep_ms(500)
			i -= 5
			if i == 80:
				flag = 3
		if flag == 3:
			pan_servo.angle(j)
			tilt_servo.angle(i)
			time.sleep_ms(500)
			j += 5
			if j == 105:
				flag = 0
		return [flag,i,j]