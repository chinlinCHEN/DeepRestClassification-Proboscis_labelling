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
import itertools

from multiprocessing import Pool


import utils.os_utils as os_utils
import utils.plot_utils as plot_utils
import utils.signal_utils as signal_utils


rawdatalist=[
'../samples/',
]

dlc_output_path_list = [
'../outputs/',

]




def Plot_movie_frame(current_Idx):

	initial_Idx=int(video_start_number)

	frame_idx=current_Idx-initial_Idx

	print(Filt_PER_movie_dir)
	print(CamDir)
	print('current_Idx:', current_Idx)
	print('frame_idx:', frame_idx)

	# print(CamDir+'camera_6_img_'+str(current_Idx)+'.jpg')
	# print(os.path.exists(CamDir+'camera_6_img_'+str(current_Idx)+'.jpg'))

	#current_img=Image.open(CamDir+'camera_6_img_'+str(current_photo_Idx)+'.jpg')
	current_img=io.imread(CamDir+'camera_6_img_'+str(current_Idx)+'.jpg')

	#print('type current_img', type(current_img))


	raw_PER_img=current_img.copy()
	smth_PER_img=current_img.copy()
	med_PER_img=current_img.copy()
	savgl_PER_img=current_img.copy()
	sarimax_PER_img=current_img.copy()

	raw_PER_img = cv2.cvtColor(raw_PER_img, cv2.COLOR_GRAY2BGR)
	smth_PER_img = cv2.cvtColor(smth_PER_img, cv2.COLOR_GRAY2BGR)
	med_PER_img = cv2.cvtColor(med_PER_img, cv2.COLOR_GRAY2BGR)
	savgl_PER_img = cv2.cvtColor(savgl_PER_img, cv2.COLOR_GRAY2BGR)
	sarimax_PER_img = cv2.cvtColor(sarimax_PER_img, cv2.COLOR_GRAY2BGR)


	PER_exten_len_flow, xax, xaxislimit = plot_utils.get_FlowTrace(PER_exten_len, frame_idx)
	smth_PER_exten_len_flow, xax, xaxislimit = plot_utils.get_FlowTrace(smth_PER_exten_len, frame_idx)
	med_PER_exten_len_flow, xax, xaxislimit = plot_utils.get_FlowTrace(med_PER_exten_len, frame_idx)
	savgl_PER_exten_len_flow, xax, xaxislimit = plot_utils.get_FlowTrace(savgl_PER_exten_len, frame_idx)
	sarimax_PER_exten_len_flow, xax, xaxislimit = plot_utils.get_FlowTrace(sarimax_PER_exten_len, frame_idx)

	print('len xax', len(xax))
	print('len xaxislimit', len(xaxislimit))
	print('len PER_exten_len_flow', len(PER_exten_len_flow))


	titles=['Raw_deeplabcut_lables', 'Running_window (kernel=3 frames)', 'Median_filter (kernel=3 frames)', 'Savitzky–Golay_filter (kernel=3 frames)', 'Sarimax_filter_from_Deeplabcut']

	# print( (int(pbsc0_X[current_Idx]), int(pbsc0_Y[current_Idx])) )
	# print( (int(pbsc1_X[current_Idx]), int(pbsc1_Y[current_Idx])) )
	# print( (int(fix_pbsc0_X), int(fix_pbsc0_Y)) )
 
	#draw with raw labels
	cv2.circle(raw_PER_img,(int(pbsc0_X), int(pbsc0_Y)), 8, (0,0,255), -1)
	cv2.circle(raw_PER_img,(int(pbsc1_X[frame_idx]), int(pbsc1_Y[frame_idx])), 8, (0,255,0), -1)
	cv2.line(raw_PER_img, (int(pbsc0_X),int(pbsc0_Y)),(int(pbsc1_X[frame_idx]), int(pbsc1_Y[frame_idx])),(255,0,0),3)

	cv2.circle(smth_PER_img,(int(fix_pbsc0_X), int(fix_pbsc0_Y)), 8, (0,0,255), -1)
	cv2.circle(smth_PER_img,(int(smth_pbsc1_X[frame_idx]), int(smth_pbsc1_Y[frame_idx])), 8, (0,255,0), -1)
	cv2.line(smth_PER_img,(int(fix_pbsc0_X), int(fix_pbsc0_Y)),(int(smth_pbsc1_X[frame_idx]), int(smth_pbsc1_Y[frame_idx])),(255,0,0),3)

	cv2.circle(med_PER_img,(int(fix_pbsc0_X), int(fix_pbsc0_Y)), 8, (0,0,255), -1)
	cv2.circle(med_PER_img,(int(med_pbsc1_X[frame_idx]), int(med_pbsc1_Y[frame_idx])), 8, (0,255,0), -1)
	cv2.line(med_PER_img,(int(fix_pbsc0_X), int(fix_pbsc0_Y)),(int(med_pbsc1_X[frame_idx]), int(med_pbsc1_Y[frame_idx])),(255,0,0),3)

	cv2.circle(savgl_PER_img,(int(fix_pbsc0_X), int(fix_pbsc0_Y)), 8, (0,0,255), -1)
	cv2.circle(savgl_PER_img,(int(savgl_pbsc1_X[frame_idx]), int(savgl_pbsc1_Y[frame_idx])), 8, (0,255,0), -1)
	cv2.line(savgl_PER_img,(int(fix_pbsc0_X), int(fix_pbsc0_Y)),(int(savgl_pbsc1_X[frame_idx]), int(savgl_pbsc1_Y[frame_idx])),(255,0,0),3)

	cv2.circle(sarimax_PER_img,(int(fix_pbsc0_X), int(fix_pbsc0_Y)), 8, (0,0,255), -1)
	cv2.circle(sarimax_PER_img,(int(sarimax_pbsc1_X[frame_idx]), int(sarimax_pbsc1_Y[frame_idx])), 8, (0,255,0), -1)
	cv2.line(sarimax_PER_img,(int(fix_pbsc0_X), int(fix_pbsc0_Y)),(int(sarimax_pbsc1_X[frame_idx]), int(sarimax_pbsc1_Y[frame_idx])),(255,0,0),3)





	fontdict={
	'color':  'white',
	'size': 16,
	}




	ylim=[-10,130]
	yticks_setting=[0,50,100]
	data_ylabel_position=[-0.08,0.5]
	fontsize=23
	tickfontsize=int(0.8*fontsize)

	photo_x_span=4
	photo_y_span=2
	plot_span_x=4
	plot_span_y=1

	raw_x=0
	raw_y=0
	raw_plot_x=raw_x
	raw_plot_y=raw_y+photo_y_span

	smth_x=raw_x+photo_x_span
	smth_y=0
	smth_plot_x=smth_x
	smth_plot_y=smth_y+photo_y_span

	med_x=smth_x+photo_x_span
	med_y=0
	med_plot_x=med_x
	med_plot_y=med_y+photo_y_span

	savgl_x=raw_x
	savgl_y=raw_plot_y+plot_span_y
	savgl_plot_x=savgl_x
	savgl_plot_y=savgl_y+photo_y_span

	sarimax_x=smth_x
	sarimax_y=smth_plot_y+plot_span_y
	sarimax_plot_x=sarimax_x
	sarimax_plot_y=sarimax_y+photo_y_span	

	x_span_fig=photo_x_span*3
	y_span_fig=(photo_y_span+plot_span_y)*2

	# print('x_span_fig', x_span_fig)
	# print('y_span_fig', y_span_fig)


	fig=plt.figure(facecolor='black', figsize=(x_span_fig*3, y_span_fig*3 ), dpi=90)

	fig.subplots_adjust(wspace = 1.4, hspace=1, left=0.05, right = 0.97, bottom = 0.06, top = 0.96)
	 
	#raw


	raw_img = plt.subplot2grid((y_span_fig, x_span_fig),(raw_y, raw_x),rowspan=photo_y_span,colspan=photo_x_span) 
	raw_img.set_title(titles[0], fontdict, fontsize=fontsize)
	raw_img.imshow(raw_PER_img)
	frNum=plt.text(20,40,frame_idx,color='r',size=25)

	raw_plt = plt.subplot2grid((y_span_fig, x_span_fig),(raw_plot_y, raw_plot_x),rowspan=plot_span_y,colspan=plot_span_x) 
	raw_plt.plot(xax, PER_exten_len_flow, label = "raw", color='r',linewidth=1.4)
	raw_plt.plot(frame_idx, PER_exten_len[frame_idx], marker = 'o', markersize = 5, color='y', markeredgewidth=4, markerfacecolor='y', markeredgecolor='y', linewidth=0)
	#raw_plt.axvline(frame_idx, linestyle='dashed',color='white',linewidth=1.4)
	raw_plt.set_xlim(xaxislimit[0], xaxislimit[1])
	raw_plt.set_ylim(ylim[0], ylim[1])
	raw_plt.yaxis.set_major_locator(plt.MaxNLocator(3))
	raw_plt.spines['bottom'].set_color('white')
	raw_plt.spines['top'].set_visible(False)
	raw_plt.spines['right'].set_visible(False)
	raw_plt.spines['left'].set_color('white')
	raw_plt.get_xaxis().set_visible(True)
	raw_plt.get_xaxis().tick_bottom()
	raw_plt.get_yaxis().tick_left()
	raw_plt.tick_params(axis='both', colors='w',top=False,right=False,labelsize=tickfontsize, length=4)
	raw_plt.get_yaxis().set_label_coords(data_ylabel_position[0],data_ylabel_position[1])
	#raw_plt.tick_params(axis='y', colors='white',top='off',right='off', labelsize=15) 
	raw_plt.set_ylabel('PER length (px)',fontsize=fontsize,color='w')
	raw_plt.set_xlabel('Frames',fontsize=fontsize,color='w')
	


	#smth
	smth_img = plt.subplot2grid((y_span_fig, x_span_fig),(smth_y, smth_x),rowspan=photo_y_span,colspan=photo_x_span) 
	smth_img.set_title(titles[1], fontdict, fontsize=fontsize)
	smth_img.imshow(smth_PER_img)

	smth_plot = plt.subplot2grid((y_span_fig, x_span_fig),(smth_plot_y, smth_plot_x),rowspan=plot_span_y,colspan=plot_span_x) 
	smth_plot.plot(xax, smth_PER_exten_len_flow, label = "smth", color='r',linewidth=1.4)
	smth_plot.plot(frame_idx, smth_PER_exten_len[frame_idx], marker = 'o', markersize = 5, color='y', markeredgewidth=4, markerfacecolor='y', markeredgecolor='y', linewidth=0)
	#smth_plot.axvline(frame_idx, linestyle='dashed',color='white',linewidth=1.4)
	smth_plot.set_xlim(xaxislimit[0], xaxislimit[1])
	smth_plot.set_ylim(ylim[0], ylim[1])
	smth_plot.yaxis.set_major_locator(plt.MaxNLocator(3))
	smth_plot.spines['bottom'].set_color('white')
	smth_plot.spines['top'].set_visible(False)
	smth_plot.spines['right'].set_visible(False)
	smth_plot.spines['left'].set_color('white')
	smth_plot.get_xaxis().set_visible(True)
	smth_plot.tick_params(axis='both', colors='white',top=False,right=False,labelsize=tickfontsize, length=4)
	smth_plot.get_yaxis().set_label_coords(data_ylabel_position[0],data_ylabel_position[1])
	#smth_plot.tick_params(axis='y', colors='white',top='off',right='off', labelsize=15) 
	smth_plot.set_ylabel('PER length (px)',fontsize=fontsize,color='w')
	smth_plot.set_xlabel('Frames',fontsize=fontsize,color='w')


	#median
	med_img = plt.subplot2grid((y_span_fig, x_span_fig),(med_y, med_x),rowspan=photo_y_span,colspan=photo_x_span) 
	med_img.set_title(titles[2], fontdict, fontsize=fontsize)
	med_img.imshow(med_PER_img)

	med_plot = plt.subplot2grid((y_span_fig, x_span_fig),(med_plot_y, med_plot_x),rowspan=plot_span_y,colspan=plot_span_x) 
	med_plot.plot(xax, med_PER_exten_len_flow, label = "med", color='r',linewidth=1.4)
	med_plot.plot(frame_idx, med_PER_exten_len[frame_idx], marker = 'o', markersize = 5, color='y', markeredgewidth=4, markerfacecolor='y', markeredgecolor='y', linewidth=0)
	#med_plot.axvline(frame_idx, linestyle='dashed',color='white',linewidth=1.4)
	med_plot.set_xlim(xaxislimit[0], xaxislimit[1])
	med_plot.set_ylim(ylim[0], ylim[1])
	med_plot.yaxis.set_major_locator(plt.MaxNLocator(3))
	med_plot.spines['bottom'].set_color('white')
	med_plot.spines['top'].set_visible(False)
	med_plot.spines['right'].set_visible(False)
	med_plot.spines['left'].set_color('white')
	med_plot.get_xaxis().set_visible(True)
	med_plot.tick_params(axis='both', colors='white',top=False,right=False,labelsize=tickfontsize, length=4)
	med_plot.get_yaxis().set_label_coords(data_ylabel_position[0],data_ylabel_position[1])
	#med_plot.tick_params(axis='y', colors='white',top='off',right='off', labelsize=15) 
	med_plot.set_ylabel('PER length (px)',fontsize=fontsize,color='w')
	med_plot.set_xlabel('Frames',fontsize=fontsize,color='w')

	#savgl
	savgl_img = plt.subplot2grid((y_span_fig, x_span_fig),(savgl_y, savgl_x),rowspan=photo_y_span,colspan=photo_x_span) 
	savgl_img.set_title(titles[3], fontdict, fontsize=fontsize)
	savgl_img.imshow(savgl_PER_img)

	savgl_plot = plt.subplot2grid((y_span_fig, x_span_fig),(savgl_plot_y, savgl_plot_x),rowspan=plot_span_y,colspan=plot_span_x) 
	savgl_plot.plot(xax, savgl_PER_exten_len_flow, label = "savgl", color='r',linewidth=1.4)
	savgl_plot.plot(frame_idx, savgl_PER_exten_len[frame_idx], marker = 'o', markersize = 5, color='y', markeredgewidth=4, markerfacecolor='y', markeredgecolor='y', linewidth=0)
	#savgl_plot.axvline(frame_idx, linestyle='dashed',color='white',linewidth=1.4)
	savgl_plot.set_xlim(xaxislimit[0], xaxislimit[1])
	savgl_plot.set_ylim(ylim[0], ylim[1])
	savgl_plot.yaxis.set_major_locator(plt.MaxNLocator(3))
	savgl_plot.spines['bottom'].set_color('white')
	savgl_plot.spines['top'].set_visible(False)
	savgl_plot.spines['right'].set_visible(False)
	savgl_plot.spines['left'].set_color('white')
	savgl_plot.get_xaxis().set_visible(True)
	savgl_plot.tick_params(axis='both', colors='white',top=False,right=False,labelsize=tickfontsize, length=4)
	savgl_plot.get_yaxis().set_label_coords(data_ylabel_position[0],data_ylabel_position[1])
	#savgl_plot.tick_params(axis='y', colors='white',top='off',right='off', labelsize=15) 
	savgl_plot.set_ylabel('PER length (px)',fontsize=fontsize,color='w')
	savgl_plot.set_xlabel('Frames',fontsize=fontsize,color='w')
	

	#sarimax	
	plt.subplot(4,3,8)
	plt.title(titles[4], fontdict, fontsize=fontsize)
	plt.imshow(sarimax_PER_img)

	sarimax_img = plt.subplot2grid((y_span_fig, x_span_fig),(sarimax_y, sarimax_x),rowspan=photo_y_span,colspan=photo_x_span) 
	sarimax_img.set_title(titles[4], fontdict, fontsize=fontsize)
	sarimax_img.imshow(sarimax_PER_img)

	sarimax_plot = plt.subplot2grid((y_span_fig, x_span_fig),(sarimax_plot_y, sarimax_plot_x),rowspan=plot_span_y,colspan=plot_span_x) 
	sarimax_plot.plot(xax, sarimax_PER_exten_len_flow, label = "sarimax", color='r',linewidth=1.4)
	sarimax_plot.plot(frame_idx, sarimax_PER_exten_len[frame_idx], marker = 'o', markersize = 5, color='y', markeredgewidth=4, markerfacecolor='y', markeredgecolor='y', linewidth=0)
	#sarimax_plot.axvline(frame_idx, linestyle='dashed',color='white',linewidth=1.4)
	sarimax_plot.set_xlim(xaxislimit[0], xaxislimit[1])
	sarimax_plot.set_ylim(ylim[0], ylim[1])
	sarimax_plot.yaxis.set_major_locator(plt.MaxNLocator(3))
	sarimax_plot.spines['bottom'].set_color('white')
	sarimax_plot.spines['top'].set_visible(False)
	sarimax_plot.spines['right'].set_visible(False)
	sarimax_plot.spines['left'].set_color('white')
	sarimax_plot.get_xaxis().set_visible(True)
	sarimax_plot.tick_params(axis='both', colors='white',top=False,right=False,labelsize=tickfontsize)
	sarimax_plot.get_yaxis().set_label_coords(data_ylabel_position[0],data_ylabel_position[1])
	#sarimax_plot.tick_params(axis='y', colors='white',top='off',right='off', labelsize=15) 
	sarimax_plot.set_ylabel('PER length (px)',fontsize=fontsize,color='w')
	sarimax_plot.set_xlabel('Frames',fontsize=fontsize,color='w')

	print('saving frames ...')
	#plt.tight_layout()
	plt.savefig(Filt_PER_movie_dir+'VidFrame' + "%05d" % current_Idx + '.jpg', facecolor=fig.get_facecolor(), edgecolor='none', transparent=True)
	plt.clf()	
	plt.close(fig)

	return

## Main ##




for dlc_outputFile_dir in dlc_output_path_list:

	if not os.path.exists(dlc_outputFile_dir):
		print("/nThe output path doesn't exist.../n")
		sys.exit(0)

	CamDir=rawdatalist[0]
	dir_cont_temp=sorted(os.listdir(CamDir))
	dir_cont=[]
	for i, v in enumerate(dir_cont_temp):
		if v[-3:]=='jpg':
			dir_cont.append(v)

	video_start_number = dir_cont[0].split('.')[0].split('_')[-1]
	video_stop_number = dir_cont[-1].split('.')[0].split('_')[-1]


	print('video_stop_number', video_stop_number)



	PER_h5_Dir= dlc_outputFile_dir
	outputPERdir = PER_h5_Dir+'PE_classification_results/'

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



	# for i in range(int(video_start_number), int(video_stop_number)):
	# # for i in range(6000, 7440):
	# # for i in (0,1,150,1000,5000,7000,7430):
	# # for i in (1,774,775,776):
	#  	Plot_movie_frame(i)

	# pool=Pool()
	# #pool.map(Plot_movie_frame, (350, 5620, 5655, 1875, 7439))
	# # pool.map(plot_utils.Plot_movie_frame, range(0, len(pbsc1_X)))
	# #pool.map(Plot_movie_frame, (1,774,775,776))
	# # pool.map(Plot_movie_frame, range(774,776))

	# pool.map(Plot_movie_frame, range(int(video_start_number), int(video_stop_number)))
	
	# pool.close()
	# pool.join()
	# del pool




	os.chdir(Filt_PER_movie_dir)
	# os.system('ffmpeg -y -r 30 -start_number 00000 -i VidFrame%05d.jpg -vcodec libx264 -pix_fmt yuv420p -crf 32 '+ date+'-'+genotype+'-'+fly+'-'+recrd_num+'-_filtered_PER_labels.mp4')
	os.system('ffmpeg -y -r 30 -start_number '+"{:05d}".format(int(video_start_number))+' -i VidFrame%05d.jpg -vcodec libx264 -pix_fmt yuv420p -crf 32 '+ 'video-_filtered_PER_labels.mp4')


	print('removing frames in ', Filt_PER_movie_dir)
	os.system('rm *.jpg')
	















	


