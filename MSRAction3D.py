from __future__ import print_function
from os.path import join
from os import listdir
import numpy as np
import action_data_lib

data_dir='Data/MSR/MSRAction3DSkeletonReal3D'

def read():
    print('Loading MSR 3D Data, data directory %s' % data_dir)
    data,labels,lens,subjects=[],[],[],[]
    filenames = []
    documents = [join(data_dir, d)
                 for d in sorted(listdir(data_dir))]
    filenames.extend(documents)
    filenames = np.array(filenames)


    for file in filenames:
        action=np.loadtxt(file)[:,:3].flatten()

        labels.append(action_data_lib.full_fname2_str(data_dir, file, 'a'))
        frame_size = len(action) / 60 # 20 iskeleton num x,y,z 3D points
        lens.append(frame_size)
        action=np.asarray(action).reshape(frame_size,60)
        data.append(action)
        subjects.append(action_data_lib.full_fname2_str(data_dir, file, 's'))
        #print(action.shape,frame_size)
    data = np.asarray(data)
    labels = np.asarray(labels)
    lens = np.asarray(lens)
    subjects = np.asarray(subjects)
    print('data shape: %s, label shape: %s,lens shape %s' % (data.shape, labels.shape, lens.shape))

    return action_data_lib.test_train_splitter_MSR_FLOR(1, data, labels, lens, subjects)

