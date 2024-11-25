from interface import Center, Size
import numpy as np
from sensor_msgs.msg import CameraInfo

class Validate:
    def __init__(self):
        pass

    def __validateCenter(self, center: Center):
        if not isinstance(center.x, (int, float)) or not isinstance(center.y, (int, float)):
            raise Exception("Center values must be numbers")

    def __validateSize(self, size: Size):
        if not isinstance(size.width, (int, float)) or not isinstance(size.height, (int, float)):
            raise Exception("Size values must be numbers")
    
    def __validateCenterDepth(self, centerDepth):
        if centerDepth <= 0:
            raise Exception("Center depth is not valid")
        
    def __validateCompareCameraInfo(self, currentCameraInfo: CameraInfo, cameraInfo: CameraInfo):
        equal = True
        equal = equal and (cameraInfo.width == currentCameraInfo.width)
        equal = equal and (cameraInfo.height == currentCameraInfo.height)
        equal = equal and np.all(np.isclose(np.asarray(cameraInfo.K),
                                            np.asarray(currentCameraInfo.K)))
        return equal