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
from make_ts_file import *

print("process start!")

sample_info_list = load_sample_info_list()
# plot_samples_classes(sample_info_list)
make_ts_file(sample_info_list, 'coswara-4k.ts')


print("process complete!")
