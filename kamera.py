from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.hflip = True
camera.vflip = True

def take_photo():
    camera.start_preview()
    sleep(4)
    camera.capture('image.jpg')
    camera.stop_preview()
    
def take_video (duration = 10):
    global camera
    with open("video.h264", "wb") as capture_file:
        camera.resolution = (1296, 972)
        camera.framerate = 24
        camera.start_recording(capture_file)
        camera.wait_recording(duration)
        camera.stop_recording()
    
def main():
    command = input("Haluatko ottaa: a: photo b: video\n")
    

    if command == "a":
        take_photo()
    elif command == "b":
        take_video()
        
main()        