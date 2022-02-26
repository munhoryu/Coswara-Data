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
from plot_samples_classes import *
from sample_info import *

print("process start!")

# sample_info_list = make_sample_info_list() # 2375 samples
# write_sample_info_list(sample_info_list, 'sample_info_raw.json')

# sample_info_list = read_sample_info_list('sample_info_raw.json')

# sample_info_list = check_sample_info_list(sample_info_list) # 2300 samples
# write_sample_info_list(sample_info_list, 'sample_info_checked.json')

sample_info_list = read_sample_info_list('sample_info_checked.json')

# shuffle samples
random.seed(a=42)
random.shuffle(sample_info_list)
# reduce samples
sample_info_list = sample_info_list[:1200]
print(len(sample_info_list))

# plot_samples_classes(sample_info_list)


def make_ts_file(sample_info_list, ts_file_name='coswara.ts'):
    print('make ts file start...')
    with open(ts_file_name, 'w') as f:
        # @timeStamps false
        # @missing false
        # @equalLength true
        # @seriesLength 251
        f.write(f'@problemName Coswara data set\n')
        f.write(f'@timeStamps false\n')
        f.write(f'@univariate true\n')
        # f.write(f'@classLabel true clear cough exp h rest\n')
        f.write(f'@classLabel true')
        for class_label in class_labels:
            f.write(f' {class_label}')
        f.write('\n')
        f.write(f'@data\n')

        for i_sample_info, sample_info in enumerate(sample_info_list):
            if i_sample_info >= 10:
                break
            sample_path = sample_path_from_info(sample_info)
            if (i_sample_info+1) % 100 == 0:
                print(f'sample {i_sample_info+1}/{len(sample_info_list)}')
            for i_class, class_file_name in enumerate(class_file_names):
                # print(f'{class_file_name}')
                file_name = os.path.join(sample_path, class_file_name)
                x, sr = process_file(file_name)
                x = librosa.resample(x, orig_sr=sr, target_sr=4000)
                # x = [1, 2, 3]
                for i_data in range(len(x)):
                    if i_data != len(x)-1:
                        f.write(f'{x[i_data]},')
                    else:
                        f.write(f'{x[i_data]}:{class_labels[i_class]}\n')
    print('make ts file done')


ts_file_name = 'coswara.ts'
make_ts_file(sample_info_list, 'coswara-4k.ts')


def check_sample(file_name):
    x, sr = process_file(file_name)
    plt.figure()
    plt.plot(x, c='k')
    # plt.axis('off')
    # plt.title(file_name)
    plt.show()

    # fig, axs = plt.subplots(3, 1)
    # # fig.suptitle(file_name)
    # axs[0].plot(x, c='k')
    # axs[1].plot(x_normalized, c='r')
    # axs[2].plot(x_trimmed, c='g')
    # plt.show()


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

# for i in range(len(sample_info_list)):
#     print(f'sample {i+1}/{len(sample_info_list)}')
#     sample_path = sample_path_from_info(sample_info_list[i])
#     for class_file_name in class_file_names:
#         print(f'checking {sample_path}:{class_file_name}')
#         file_name = os.path.join(sample_path, class_file_name)
#         check_sample(file_name)


print("process complete!")
