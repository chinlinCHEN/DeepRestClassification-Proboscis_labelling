"""
Use pythonw to run the script!!!
"""

import sys
import os
import deeplabcut


# path_model_config_file='/mnt/data/CLC/dlc/PER-CLC-2020-03-18/config.yaml'
path_model_config_file='../DLC_model/config.yaml'



output_dir = '../outputs/'
if not os.path.exists(output_dir):
	os.makedirs(output_dir)


input_video = '../outputs/video.mp4'


## For refining and re-training the network:
# deeplabcut.extract_outlier_frames(path_model_config_file,videofile_path)
# deeplabcut.refine_labels(path_model_config_file)
# deeplabcut.merge_datasets(path_model_config_file)
# deeplabcut.create_training_dataset(path_model_config_file)
# deeplabcut.train_network(path_model_config_file, displayiters=500, saveiters=1000, maxiters=11000)
# deeplabcut.evaluate_network(path_model_config_file, plotting=True)


## Make prediction on video:

dlc_h5_filename=input_video.split('/')[-1].split('.')[0]+'_DLC_resnet50_PERMar18shuffle1_10000.h5'

path=[input_video]

if not os.path.exists(output_dir+dlc_h5_filename):

	print('\nDLC process in ', input_video,'\n')

	deeplabcut.analyze_videos(path_model_config_file, path,  save_as_csv=True, videotype='.mp4')
	deeplabcut.create_labeled_video(path_model_config_file, path, draw_skeleton=True, videotype='mp4')
	# deeplabcut.plot_trajectories(path_model_config_file, path)
		


else: 
	print('DLC_resnet50_PERMar18shuffle1_10000.h5 already exists')




