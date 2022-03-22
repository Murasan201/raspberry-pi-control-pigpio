import pigpio
pi = pigpio.pi()

#PWMパラメータ
pwm_pin1 = 18 #PWM出力ピンを指定
pwm_pin2 = 19 #PWM出力ピンを指定
duty1 = 70 #デューティー比を%で指定
duty2 = 40 #デューティー比を%で指定
freq = 1000 #PWM周波数をHzで指定

#パラメータ変換
cnv_dutycycle1 = int((duty1 * 1000000 / 100))
cnv_dutycycle2 = int((duty2 * 1000000 / 100))

#PWMを出力
pi.hardware_PWM(pwm_pin1, freq, cnv_dutycycle1)
pi.hardware_PWM(pwm_pin2, freq, cnv_dutycycle2)