import os
import shutil
import numpy as np

def train_val_test_split(n):
    train = np.sort(np.random.choice(n, size=int(0.8*n), replace=False))
    left = np.setdiff1d(np.arange(n), train)
    val = np.sort(np.random.choice(left, size=int(0.5*len(left)), replace=False))
    test = np.setdiff1d(left, val)
    return train, val, test

# A function to split train and test data in a random sequence,including image and caption, and save them
def split_data(Img_folder,Caption_file,split_ratio):
    # read all the images and captions
    Img_list = os.listdir(Img_folder)
    Caption_list = np.load(Caption_file,allow_pickle=True)
    print(len(Img_list))
    print(len(Caption_list))
    assert len(Img_list) == len(Caption_list)
    num = len(Img_list)

    # shuffle the index
    index = np.arange(num)
    np.random.shuffle(index)

    # split the data 
    train_index = np.sort(index[:int(num*split_ratio)])
    test_index = np.sort(index[int(num*split_ratio):])
    train_Img = [Img_list[i] for i in train_index]
    test_Img = [Img_list[i] for i in test_index]
    train_Caption = [Caption_list[i] for i in train_index]
    test_Caption = [Caption_list[i] for i in test_index]
    
    # save the image to seperate folders
    train_folder = r"C:\Users\DELL\Desktop\Predict\train_img"
    test_folder = r"C:\Users\DELL\Desktop\Predict\test_img"
    if not os.path.exists(train_folder):
        os.makedirs(train_folder)
    if not os.path.exists(test_folder):
        os.makedirs(test_folder)
    for img in train_Img:
        print(img)
        shutil.copy(os.path.join(Img_folder, img), train_folder)
    for img in test_Img:
        print(img)
        shutil.copy(os.path.join(Img_folder, img), test_folder)
    
    # save the captions in seperate files
    np.save(r"C:\Users\DELL\Desktop\Predict\train_Caption.npy",train_Caption)
    np.save(r"C:\Users\DELL\Desktop\Predict\test_Caption.npy",test_Caption)
