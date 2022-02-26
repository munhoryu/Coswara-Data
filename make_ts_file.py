from commons import *


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
            # if i_sample_info >= 10:
            #     break
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
