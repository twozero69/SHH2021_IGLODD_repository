#!/usr/bin/env python
import rospy
from sensor_msgs.msg import PointCloud2
from std_msgs.msg import Bool
import sensor_msgs.point_cloud2 as pc2
import numpy as np
import ros_numpy
import pyautogui
import time
screenWidth, screenHeight=pyautogui.size()

dist=0.154
max_x=0.517+dist
max_y=0.161
param_x=max_x-dist
err=40
err2=50
state = 0
pos_x = 0
pos_y = 0 
start = 0

def callback(data):
      global state, start, pos_x, pos_y

      touchPoints = ros_numpy.numpify(data)
      touchCounts = touchPoints.shape[0]

      if touchCounts == 1:
            pub.publish(True)
            points=np.zeros((touchCounts,2))
            points[:,0]=touchPoints['x']
            points[:,1]=touchPoints['y']
            x=(max_x+points[0,0])/param_x*screenHeight
            y=(max_y+points[0,1])/max_y*screenWidth/2
            if state==0:
                  start=time.time()
                  pos_x=x
                  pos_y=y
                  pyautogui.moveTo(y, x)
                  state=1
            elif state==1:
                  pos_x=x
                  pos_y=y
                  pyautogui.moveTo(y, x)
                  if pos_x+err>x and x>pos_x-err and pos_y+err>y and y>pos_y-err:
                        if time.time()-start>0.3:
                              state=2
                  else:
                        state=0
            elif state==2:
                  if pos_x+err2>x and x>pos_x-err2 and pos_y+err2>y and y>pos_y-err2:
                        if time.time()-start>0.8:
                              pyautogui.click(pos_y, pos_x)
                              state=-1
                  else:
                        state=0

            #rospy.loginfo("%d: %f", state, time.time()-start)
                  
      else:
            pub.publish(False)
            state=0

rospy.init_node('twozeroClick', anonymous=True)
pub = rospy.Publisher('flag', Bool, queue_size = 10)
rospy.Subscriber("twozeroLidar/result", PointCloud2, callback)
rospy.spin()
