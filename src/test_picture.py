import sys
sys.path.append('/home/royd1990/donkeycar')
from donkeycar import Vehicle
from donkeycar.parts.camera import MockCamera
from donkeycar.parts.datastore import Tub



V = Vehicle()

#add a camera part
cam = MockCamera()
V.add(cam, outputs=['image'], threaded=True)

#add tub part to record images
tub = Tub(path='~/d2/gettings_started', 
          inputs=['image'], 
          types=['image_array'])
V.add(tub, inputs=['image'])

#start the drive loop at 10 Hz
#V.start(rate_hz=10)
