import os 
import h5py
import numpy as np
import scipy.io as sio
data_folder = r"D:\Downloads\sub_beta_day\500_BW"

# try use h5py to read mat file,if it doesn't work, use scipy.io to read
def read_mat_file(file_path):
    try:
        data = h5py.File(file_path, 'r')
    except:
        data = sio.loadmat(file_path)
    return data

IT_path = os.path.join(data_folder, "OBJ500_IT.mat")
IT_index = read_mat_file(IT_path) 
IT_left_index = IT_index['LYP_IT'][0,0].squeeze()
IT_right_index = IT_index['LYP_IT'][0,1].squeeze()

EVC_path = os.path.join(data_folder, "primary.mat")
EVC_index = read_mat_file(EVC_path)
EVC_left_index = np.unique(np.concatenate([EVC_index['LYP_V1'][0,0],EVC_index['LYP_V2'][0,0],EVC_index['LYP_V3'][0,0]]))
EVC_right_index = np.unique(np.concatenate([EVC_index['LYP_V1'][0,1],EVC_index['LYP_V2'][0,1],EVC_index['LYP_V3'][0,1]]))

print(IT_left_index.shape,IT_right_index.shape)
print(EVC_left_index.shape,EVC_right_index.shape)

# read the fMRI resp data  
resp_left_array, resp_right_array = [], []
for i in range(1,11):
    resp_path = os.path.join(data_folder,"LYP_beta_" + str(i).zfill(2))
    resp_data = read_mat_file(resp_path)
    resp_left_data, resp_right_data = resp_data['betaLH'], resp_data['betaRH']
    resp_left_array.append(resp_left_data)
    resp_right_array.append(resp_right_data)

# compute the average of the data
resp_left_array = np.array(resp_left_array)
resp_right_array = np.array(resp_right_array)
resp_left_mean = np.mean(resp_left_array,axis=0)
resp_right_mean = np.mean(resp_right_array,axis=0)

# extract the data of the selected voxels
resp_left_IT = resp_left_mean[:,IT_left_index]
resp_right_IT = resp_right_mean[:,IT_right_index]
resp_left_EVC = resp_left_mean[:,EVC_left_index]
resp_right_EVC = resp_right_mean[:,EVC_right_index]

# merge the left and right data
resp_IT = np.concatenate([resp_left_IT,resp_right_IT],axis=1)
resp_EVC = np.concatenate([resp_left_EVC,resp_right_EVC],axis=1)

# save the data
np.save(r"C:\Users\DELL\Desktop\Predict\resp_IT.npy",resp_IT)
np.save(r"C:\Users\DELL\Desktop\Predict\resp_EVC.npy",resp_EVC)

# first read the index from train and test image dataset
img_train_folder = r"C:\Users\DELL\Desktop\Predict\train_img"
img_test_folder = r"C:\Users\DELL\Desktop\Predict\test_img"
train_idx = np.sort([int(img.split(".")[0]) for img in os.listdir(img_train_folder)])
test_idx = np.sort([int(img.split(".")[0]) for img in os.listdir(img_test_folder)])

# split the resp data into train and test
resp_IT = np.load(r"C:\Users\DELL\Desktop\Predict\resp_IT.npy",allow_pickle=True)
resp_EVC = np.load(r"C:\Users\DELL\Desktop\Predict\resp_EVC.npy",allow_pickle=True)

resp_IT_train = resp_IT[train_idx-1,:]
resp_IT_test = resp_IT[test_idx-1,:]
resp_EVC_train = resp_EVC[train_idx-1,:]
resp_EVC_test = resp_EVC[test_idx-1,:]

# delete the zero columns
resp_IT_train = resp_IT_train[:,~np.all(resp_IT_train == 0, axis=0)]
resp_IT_test = resp_IT_test[:,~np.all(resp_IT_test == 0, axis=0)]
resp_EVC_train = resp_EVC_train[:,~np.all(resp_EVC_train == 0, axis=0)]
resp_EVC_test = resp_EVC_test[:,~np.all(resp_EVC_test == 0, axis=0)]

# save the splited data
np.save(r"C:\Users\DELL\Desktop\Predict\resp_IT_train.npy",resp_IT_train)
np.save(r"C:\Users\DELL\Desktop\Predict\resp_IT_test.npy",resp_IT_test)
np.save(r"C:\Users\DELL\Desktop\Predict\resp_EVC_train.npy",resp_EVC_train)
np.save(r"C:\Users\DELL\Desktop\Predict\resp_EVC_test.npy",resp_EVC_test)
