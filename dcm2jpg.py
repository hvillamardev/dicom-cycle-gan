import imageio
import numpy as np
import pydicom
import os
from config import Params
import pandas as pd

# make it True if you want in PNG format
PNG = False
# Specify the .dcm folder path
folder_path = Params.path_dcm
# Specify the output jpg/png folder path
jpg_folder_path = Params.path_jpg
# for p in os.listdir(folder_path):
#     for q in os.listdir(os.path.join(folder_path, p)):
#         dcm_path = os.path.join(folder_path, p, q)
#         images_path = os.listdir(dcm_path)
#         for n, image in enumerate(images_path):
#             ds = pydicom.read_file(os.path.join(dcm_path, image), force=True)
#             img = ds.pixel_array.astype(float)
#             scaled_image = (np.maximum(img, 0) / img.max()) * 255.0
#             scaled_image = np.uint8(scaled_image)
#             image = image.replace('.dcm', '.jpg')
#             jpg_folder_path = dcm_path.replace("DCM", "JPG")
#             if not os.path.exists(jpg_folder_path):
#                 os.makedirs(jpg_folder_path)
#             imageio.imwrite(os.path.join(jpg_folder_path, image), scaled_image)
#             if n % 50 == 0:
#                 print('{} image converted'.format(n))

scans=[]
for p in os.listdir(folder_path):
    for q in os.listdir(os.path.join(folder_path, p)):
        dcm_path = os.path.join(folder_path, p, q)
        images_path = os.listdir(dcm_path)
        for n, image in enumerate(images_path):
            ds = pydicom.read_file(os.path.join(dcm_path, image), force=True)
            mod_ds = {data_elem.keyword: data_elem.value for data_elem in ds.values()}
            scans.append(mod_ds)

df = pd.DataFrame(scans)
