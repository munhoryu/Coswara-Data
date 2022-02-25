import matplotlib.pyplot as plt
import librosa
import os
import sys
import subprocess
import numpy as np
import glob
import json
import pandas as pd
import random
from commons import *

print("process start!")

sample_info_list = load_sample_info_list()
# print('len(sample_info_list)', len(sample_info_list))
# print(sample_info_list[:5])


def check_sample(file_name):
    x, sr = load_file(file_name)

    x_normalized = (x - x.mean(axis=0)) / x.std(axis=0)
    # print('mean', x_normalized.mean())
    # print('std', x_normalized.std())

    pad = 0.25*sr
    db_max = 50
    hop_length = np.floor(0.010*sr).astype(int)  # 10ms
    win_length = np.floor(0.020*sr).astype(int)  # 20ms
    x_trimmed = trim_silence(x_normalized, pad, db_max, win_length, hop_length)

    fig, axs = plt.subplots(3, 1)
    # fig.suptitle(file_name)
    axs[0].plot(x, c='k')
    axs[1].plot(x_normalized, c='r')
    axs[2].plot(x_trimmed, c='g')
    plt.show()


# file_name = samples_list[0]
# file_name = os.path.join(file_name, 'breathing-deep.wav')
# check_data(file_name)

# sample_name = samples_list[0]
# for class_dir in class_dirs:
#     file_name = os.path.join(sample_name, f'{class_dir}.wav')
#     check_data(file_name)

# sample_path = sample_path_from_info(sample_info_list[0])
# class_file_name = class_file_names[0]
# file_name = os.path.join(sample_path, class_file_name)
# check_sample(file_name)

# sample_path = sample_path_from_info(sample_info_list[0])
# for class_file_name in class_file_names:
#     file_name = os.path.join(sample_path, class_file_name)
#     check_sample(file_name)

for i in range(len(sample_info_list)):
    print(f'sample {i+1}/{len(sample_info_list)}')
    sample_path = sample_path_from_info(sample_info_list[i])
    for class_file_name in class_file_names:
        print(f'checking {sample_path}:{class_file_name}')
        file_name = os.path.join(sample_path, class_file_name)
        check_sample(file_name)

print("process complete!")
