import audio
from GyroSim import GyroSim
import math 
import helper
from VectorAnimation import VectorAnimation
from time import sleep

gyro_sim=GyroSim(90, 0, 1)
vector_animation = VectorAnimation()
event = None
k=900

while True:
    sleep(0.05)
    gyro_sim.update()
    print("delta heading: ", gyro_sim.get_delta_heading())

    if event and not event.is_set(): 
        continue
    if abs(gyro_sim.get_delta_heading()) < 5:
        continue

    #audio
    doppler_frequency = helper.clamp(1, k * abs(gyro_sim.get_delta_heading() ** -1), 10000)
    isLeft = gyro_sim.get_delta_heading() > 0
    beep = audio.generate_stereo_beep(isLeft, doppler_frequency=doppler_frequency)
    event = audio.async_play_stereo_audio(beep)

    #vector animation
    vector_animation.update(gyro_sim.get_heading())
    

