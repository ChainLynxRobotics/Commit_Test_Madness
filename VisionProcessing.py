import cv2
import numpy as np
obj_pts = np.matrix([(0.0,0.0,0.0), (0.0, 1.0, 0.0), (1.0, 1.0, 0.0), (1.0, 0.0, 0.0)])
cam = np.matrix([(250, 0, 558), (0, 250, 50), (0, 0, 1)], dtype = "double")
dist_coeffs = np.array([0.0, 0.0, 0.0, 0.0])
image_points = np.array([[479.87487793, 220.1733551 ],
       [631.66522217, 220.36279297],
       [635.27069092, 369.67810059],
       [481.52929687, 371.36853027]])
rVec = None
tVec = None

result = cv2.solvePnP(objectPoints=obj_pts, imagePoints=image_points, cameraMatrix=cam, distCoeffs=dist_coeffs, rvec=rVec, tvec=tVec)
#change
print("Rotational Vector: " + str(result[1]))
print("Translational Vector: " + str(result[2]))