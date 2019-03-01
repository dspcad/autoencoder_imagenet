import os 
import numpy as np
import cv2
import random


def read_class_mapping(filename):
    tbl = dict()
    f = open(filename, "r")
    lines = f.readlines()
    lines = [x.strip() for x in lines]
    for line in lines:
        elems = line.split()
        tbl[elems[0]] = elems[1]

    return tbl

def read_10_classes_from_imagenet():
    tbl = read_class_mapping("map_clsloc.txt")
    path="/data/imagenet/train/"
    f = open("config.txt", "r")
    folders = f.readlines()
    folders = [x.strip() for x in folders]
    print (folders)
 
    i=0
    data = []
    label = []
    for folder in folders:
        print (folder)
        path_to_folder = path+folder
        f_list = os.listdir(path_to_folder)
    
        #ground_truth = tbl[folder]
        ground_truth = i
        print ("ground truth: %d" % ground_truth)
        for f in f_list:
            #print (path_to_folder+"/"+f)
            img = cv2.imread(path_to_folder+"/"+f)
            img = cv2.resize(img, (256, 256)) 
            if img.shape[0]<224 or img.shape[1]<224:
                print (img.shape)
            crop_img = img[16:240, 16:240]
            data.append(crop_img)
            label.append(ground_truth)
    
        #print ("%s_data.npy" % folder)
        #np.save("%s_data.npy" % folder, data)
        i += 1


    c = list(zip(data, label))
    random.shuffle(c)
    data, label = zip(*c)

    np.save("input_data.npy", data)
    np.save("input_label.npy", label)


#a = np.load("input_label.npy")
#b = np.load("input_data.npy")
#print (a)
#cv2.imwrite("test.jpg",b[0])
#cv2.imwrite("test1.jpg",b[1])
read_10_classes_from_imagenet()
