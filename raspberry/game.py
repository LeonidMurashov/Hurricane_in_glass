from rpiReciev import getMsg, msgResponce
import time

LOW_ENERGY = 10
HIGH_ENERGY = 20


if __name__ == "__main__":
	
	system_on = False
	while True:
		system_on = int(msgResponce("isOn"))
		if system_on:
			T1_in = int(msgResponce("T 10"))
			T1_out = int(msgResponce("T 8"))
			T2_in = int(msgResponce("T 11"))
			T2_out = int(msgResponce("T 9"))
			energy = ((T1_out - T1_in) + (T2_out - T2_in))/2#((T1_out-T1_in)/T1_out + (T2_out-T2_in)/T2_out) / 2#

			if energy < LOW_ENERGY:
				msgResponce("L 1 0 0")
			elif energy > HIGH_ENERGY:
				msgResponce("L 0 1 0")
			else:
				msgResponce("L 1 1 0")


		time.delay(0.1)
