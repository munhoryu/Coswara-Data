import os
import glob
import random
import librosa
import numpy as np
import json
from commons import *


def write_sample_info_list(sample_info_list, file_name='sample_info.json'):
    json.dump(sample_info_list, open(file_name, 'w'))


def read_sample_info_list(file_name='sample_info.json'):
    sample_info_list = json.load(open(file_name))
    return sample_info_list


def make_sample_info_list():
    if not os.path.exists(coswara_data_dir):
        raise("Check the Coswara dataset directory!")
    if not os.path.exists(extracted_data_dir):
        raise("Check the extracted dataset directory!")
    date_dirs = list(map(os.path.basename, glob.glob(
        '{}/202*'.format(extracted_data_dir))))
    # print(len(date_dirs))
    # print(date_dirs)
    sample_info_list = []
    for date_dir in date_dirs:
        # print(date_dir)
        date_path = os.path.join(extracted_data_dir, date_dir)
        # print(date_path)
        sample_dirs = list(
            map(os.path.basename, glob.glob('{}/*'.format(date_path))))
        # print(sample_dirs)
        for sample_dir in sample_dirs:
            # sample_path = os.path.join(date_path, sample_dir)
            sample_info_list.append(
                {'date_dir': date_dir, 'sample_dir': sample_dir})
        # print(len(sample_info_list))
    # # shuffle samples
    # random.seed(a=42)
    # random.shuffle(sample_info_list)
    # # print(sample_info_list[:5])
    # # reduce samples
    # sample_info_list = sample_info_list[:1200]
    # # print(len(sample_info_list))

    return sample_info_list


def check_sample_info_list(sample_info_list):
    checked_sample_info_list = []
    for i_sample in range(len(sample_info_list)):
        sample_path = sample_path_from_info(sample_info_list[i_sample])
        if (i_sample+1) % 100 == 0:
            print(f'sample {i_sample+1}/{len(sample_info_list)}')
        # print(f'checking {sample_path}')
        errors = 0
        for i_class in range(len(class_file_names)):
            class_file_name = class_file_names[i_class]
            # print(f'{class_file_name}')
            file_name = os.path.join(sample_path, class_file_name)
            x, sr = process_file(file_name)
            if sr == None:
                print('load or size error')
                errors += 1
                continue
        if errors == 0:
            checked_sample_info_list.append(sample_info_list[i_sample])
    print(f'sample info length: {len(sample_info_list)}')
    print(f'checked sample info length: {len(checked_sample_info_list)}')
    return checked_sample_info_list


def load_sample_info_list():
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

    # print(len(sample_info_list))
    return sample_info_list
