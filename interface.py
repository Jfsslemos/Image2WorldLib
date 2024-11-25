from sensor_msgs.msg import Image, CameraInfo
from geometry_msgs.msg import Vector3, Quaternion
from cv_bridge import CvBridge
from typing import Union
import numpy as np

bridge = CvBridge()

class Center(Vector3):
  def __init__(self, x: float = 0, y: float = 0, z: float = 0):
    super().__init__(x, y, z)

class Size:
  def __init__(self, width: float = 0, height: float = 0, depth: float = 0):
    self.width = width
    self.height = height
    self.depth = depth

class Color:
  def __init__(self, r: float = 0, g: float = 0, b: float = 0):
    self.r = r
    self.g = g
    self.b = b

class Sensor:
  def __init__(self):
    self.imageDepth: np.ndarray  = np.array([])
    self.cameraInfo: CameraInfo = CameraInfo()
  
  def setSensorData(self, image: Union[Image, np.ndarray], cameraInfo: CameraInfo):
    if isinstance(image, (Image)):
      self.imageDepth = bridge.imgmsg_to_cv2(image, desired_encoding='passthrough')
    else:
      self.imageDepth = image
    self.cameraInfo = cameraInfo
class Description2D:
  def __init__(self, 
               center: Center = Center(), 
               size: Size = Size(), 
               maxSize: Vector3 = Vector3(), 
               label: str = "", 
               score: float = 0.0):
    self.center: Center = center
    self.size: Size = size
    self.maxSize: Vector3 = maxSize
    self.label: str = label
    self.score: float = score

class Box:
  def __init__(self, 
               center: Center = Center(), 
               orientation: Quaternion = Quaternion(), 
               size: Size = Size(), 
               color: Color = Color()):
    self.center: Center = center
    self.orientation: Quaternion = orientation
    self.size: Size = size
    self.color: Color = color

class Description3D:
  def __init__(self, 
               description2D: Description2D = Description2D(), 
               box: Box = Box()):
    self.description2D: Description2D = description2D
    self.box: Box = box

  def __setData(self,
                description2D: Description2D, 
                box: Box):
    self.description2D = description2D
    self.box = box
  
class Data:
  def __init__(self, 
               sensor: Sensor = Sensor(), 
               description2D: Description2D = Description2D()):
    self.sensor: Sensor = sensor
    self.description2D: Description2D = description2D

  def __setData(self, description2D: Description2D, image: Union[Image, np.ndarray], cameraInfo: CameraInfo):
        self.description2D = description2D
        self.sensor.setSensorData(image, cameraInfo)
