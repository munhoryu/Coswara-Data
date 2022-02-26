from commons import *
import matplotlib.pyplot as plt


def check_sample_classes(sample_path):
    fig, axs = plt.subplots(4, 1, figsize=(20, 10))
    # fig.suptitle(file_name)

    # for class_file_name in class_file_names:
    for i in range(len(class_file_names)):
        class_file_name = class_file_names[i]
        print(f'{class_file_name}')
        file_name = os.path.join(sample_path, class_file_name)
        x, sr = process_file(file_name)
        axs[i].set_title(f'{class_labels[i]} Signal')
        # axs[i].plot(x, c='k')
        t = np.arange(0, len(x)) / sr
        axs[i].plot(t, x, c='k')
    # plt.axis('off')
    # plt.title(file_name)
    plt.show()


def plot_samples_classes(sample_info_list):
    for i in range(len(sample_info_list)):
        sample_path = sample_path_from_info(sample_info_list[i])
        print(f'sample {i+1}/{len(sample_info_list)}')
        print(f'checking {sample_path}')
        check_sample_classes(sample_path)
