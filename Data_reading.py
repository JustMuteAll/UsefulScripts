'''
Read hdf5 file and save numpy arrays as png images
''' 
import h5py
import numpy as np
from PIL import Image

filename = r"D:\Downloads\nsd_stimuli.hdf5"
save_path = r"C:\Users\DELL\Desktop\DataSet\NSD"
with h5py.File(filename, "r") as f:
    # Print all root level object names (aka keys) 
    # these can be group or dataset names 
    print("Keys: %s" % f.keys())
    # get first object name/key; may or may NOT be a group
    a_group_key = list(f.keys())[0]
    print(f[a_group_key])
    print(f[a_group_key].shape[0])
    print(type(f[a_group_key][0]))
    for i in range(f[a_group_key].shape[0]):
        #print(f[a_group_key][i])
        img = Image.fromarray(f[a_group_key][i])
    # save image to save_path
        img.save(save_path + "\\" + str(i) + ".png")
    # # get the object type for a_group_key: usually group or dataset
    # print(type(f[a_group_key])) 

    # # If a_group_key is a group name, 
    # # this gets the object names in the group and returns as a list
    # data = list(f[a_group_key])

    # # If a_group_key is a dataset name, 
    # # this gets the dataset values and returns as a list
    # data = list(f[a_group_key])
    # # preferred methods to get dataset values:
    # ds_obj = f[a_group_key]      # returns as a h5py dataset object
    # ds_arr = f[a_group_key][()]  # returns as a numpy array