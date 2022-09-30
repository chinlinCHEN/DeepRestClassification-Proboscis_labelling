import glob
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import pickle
import os
import cv2
import sys
from PIL import Image
Image.Image.tostring = Image.Image.tobytes
from skimage import io

from multiprocessing import Pool


import utils.os_utils as os_utils
import utils.plot_utils as plot_utils
import utils.signal_utils as signal_utils




dlc_output_path_list = [
'../samples/',

]




## Main ##




for dlc_outputFile_dir in dlc_output_path_list:

	if not os.path.exists(dlc_outputFile_dir):
		print("/nThe output path doesn't exist.../n")
		sys.exit(0)
	else:


	PER_h5_Dir= dlc_outputFile_dir
	outputPERdir = PER_h5_Dir+'outputs/'

	if not os.path.exists(outputPERdir):
		os.makedirs(outputPERdir)

	
	Filt_PER_movie_dir = outputPERdir+'Filtered_PER_movie/'
	if not os.path.exists(Filt_PER_movie_dir):
		os.makedirs(Filt_PER_movie_dir)


	pbsc0_X, pbsc0_Y, pbsc1_X, pbsc1_Y,\
	fix_pbsc0_X, fix_pbsc0_Y,\
	smth_pbsc1_X, smth_pbsc1_Y, med_pbsc1_X, med_pbsc1_Y, savgl_pbsc1_X, savgl_pbsc1_Y, sarimax_pbsc1_X, sarimax_pbsc1_Y,\
	PER_exten_len, smth_PER_exten_len, med_PER_exten_len, savgl_PER_exten_len, sarimax_PER_exten_len, \
	norm_PER_exten_len, norm_smth_PER_exten_len, norm_med_PER_exten_len, norm_savgl_PER_exten_len, norm_arima_PER_exten_len=os_utils.openDicData(outputPERdir)



	#for i in range(0, len(pbsc0_X)):
	# for i in range(6000, 7440):
	# for i in (0,1,150,1000,5000,7000,7430):
	# for i in (1,774,775,776):
	#  	Plot_movie_frame(i)

	pool=Pool()
	#pool.map(Plot_movie_frame, (350, 5620, 5655, 1875, 7439))
	pool.map(plot_utils.Plot_movie_frame, range(0, len(pbsc1_X)))
	#pool.map(Plot_movie_frame, (1,774,775,776))
	# pool.map(Plot_movie_frame, range(774,776))
	
	pool.close()
	pool.join()
	del pool




	os.chdir(Filt_PER_movie_dir)
	os.system('ffmpeg -y -r 30 -start_number 00000 -i VidFrame%05d.jpg -vcodec libx264 -pix_fmt yuv420p -crf 32 '+ date+'-'+genotype+'-'+fly+'-'+recrd_num+'-_filtered_PER_labels.mp4')


	print('removing frames in ', Filt_PER_movie_dir)
	os.chdir(Filt_PER_movie_dir)
	os.system('rm *.jpg')
	















	


