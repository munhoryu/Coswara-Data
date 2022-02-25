import os
import glob
import random
import librosa


# data paths
coswara_data_dir = os.path.abspath('.')
extracted_data_dir = os.path.join(coswara_data_dir, 'Extracted_data')

class_labels = ['breathing', 'cough', 'counting', 'vowel']
class_file_names = ['breathing-deep.wav',
                    'cough-shallow.wav', 'counting-fast.wav', 'vowel-a.wav']
sr = 48000


def sample_path_from_info(info):
    # print(f'sample_path_from_info{info}')
    # pass
    date_dir = info['date_dir']
    sample_dir = info['sample_dir']
    path = extracted_data_dir
    path = os.path.join(path, date_dir)
    path = os.path.join(path, sample_dir)
    return path


def load_sample_info_list():
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
    # shuffle samples
    random.seed(a=42)
    random.shuffle(sample_info_list)
    # print(sample_info_list[:5])
    # reduce samples
    sample_info_list = sample_info_list[:1200]
    # print(len(sample_info_list))

    return sample_info_list


def load_file(path):
    sr, removeaudio, chunk, db_max = 48000, False, 3, 50
    try:
        x, sr = librosa.load(path, sr=sr)
        return x, sr
    except:
        print('load err', path)


def trim_silence(x, pad, db_max, frame_length=256, hop_length=64):
    _, ints = librosa.effects.trim(
        x, top_db=db_max, frame_length=frame_length, hop_length=hop_length)
    start = int(max(ints[0]-pad, 0))
    end = int(min(ints[1]+pad, len(x)))
    return x[start:end]
