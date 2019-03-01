import numpy as np
import utility


#a = np.load("input_label.npy")
#b = np.load("input_data.npy")
#print (a)
#cv2.imwrite("test.jpg",b[0])
#cv2.imwrite("test1.jpg",b[1])
data, label = utility.read_10_classes_from_imagenet()
np.save("input_data.npy", data)
np.save("input_label.npy", label)
