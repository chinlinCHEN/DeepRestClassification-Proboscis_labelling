
import glob
import os
import sys
import numpy as np
import matplotlib.pyplot as plt




import utils.os_utils as os_utils
import utils.plot_utils as plot_utils
import utils.signal_utils as signal_utils
# import utils.params_utils as params_utils



dlc_output_path_list = [
'../samples/',

]



event_max_dur=2
event_min_dur=0.27





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


	h5_file = os_utils.read_latest_h5(PER_h5_Dir)
	pbsc0_X, pbsc0_Y, pbsc1_X, pbsc1_Y = os_utils.extract_coord(h5_file)

	fix_pbsc0_X, fix_pbsc0_Y = signal_utils.fix_point(pbsc0_X, pbsc0_Y)
	print('fix_pbsc0_X', fix_pbsc0_X)
	print('fix_pbsc0_Y', fix_pbsc0_Y)




	smth_pbsc1_X=signal_utils.filtered_traces(pbsc1_X, filtermode='running_window')
	smth_pbsc1_Y=signal_utils.filtered_traces(pbsc1_Y, filtermode='running_window')

	med_pbsc1_X=signal_utils.filtered_traces(pbsc1_X, filtermode='median')
	med_pbsc1_Y=signal_utils.filtered_traces(pbsc1_Y, filtermode='median')

	savgl_pbsc1_X=signal_utils.filtered_traces(pbsc1_X, filtermode='savgol_filter')
	savgl_pbsc1_Y=signal_utils.filtered_traces(pbsc1_Y, filtermode='savgol_filter')

	sarimax_pbsc1_X=signal_utils.filtered_traces(pbsc1_X, filtermode='sarimax')
	sarimax_pbsc1_Y=signal_utils.filtered_traces(pbsc1_Y, filtermode='sarimax')

	butter_pbsc1_X=signal_utils.filtered_traces(pbsc1_X, filtermode='butter_lowpass')
	butter_pbsc1_Y=signal_utils.filtered_traces(pbsc1_Y, filtermode='butter_lowpass')

	fft_pbsc1_X=signal_utils.filtered_traces(pbsc1_X, filtermode='fft_filter')
	fft_pbsc1_Y=signal_utils.filtered_traces(pbsc1_Y, filtermode='fft_filter')


	origin_pbsc1_X, origin_pbsc1_Y=signal_utils.find_origin_position(pbsc1_X, pbsc1_Y)
	origin_smth_pbsc1_X, origin_smth_pbsc1_Y=signal_utils.find_origin_position(smth_pbsc1_X, smth_pbsc1_Y)
	origin_med_pbsc1_X, origin_med_pbsc1_Y=signal_utils.find_origin_position(med_pbsc1_X, med_pbsc1_Y)
	origin_savgl_pbsc1_X, origin_savgl_pbsc1_Y=signal_utils.find_origin_position(savgl_pbsc1_X, savgl_pbsc1_Y)
	origin_sarimax_pbsc1_X, origin_sarimax_pbsc1_Y=signal_utils.find_origin_position(sarimax_pbsc1_X, sarimax_pbsc1_Y)
	origin_butter_pbsc1_X, origin_butter_pbsc1_Y=signal_utils.find_origin_position(butter_pbsc1_X, butter_pbsc1_Y)
	origin_fft_pbsc1_X, origin_fft_pbsc1_Y=signal_utils.find_origin_position(fft_pbsc1_X, fft_pbsc1_Y)


	print('origin_pbsc1_X', origin_pbsc1_X)
	print('origin_pbsc1_Y', origin_pbsc1_Y)


	PER_exten_len=[]
	for i in range(0, len(pbsc1_X)):
		dist=signal_utils.calc_length(origin_pbsc1_X, origin_pbsc1_Y, pbsc1_X[i], pbsc1_Y[i])
		PER_exten_len.append(dist)

	smth_PER_exten_len=[]
	for i in range(0, len(pbsc1_X)):
		dist=signal_utils.calc_length(origin_smth_pbsc1_X, origin_smth_pbsc1_Y, smth_pbsc1_X[i], smth_pbsc1_Y[i])
		smth_PER_exten_len.append(dist)

	med_PER_exten_len=[]
	for i in range(0, len(pbsc1_X)):
		dist=signal_utils.calc_length(origin_med_pbsc1_X, origin_med_pbsc1_Y, med_pbsc1_X[i], med_pbsc1_Y[i])
		med_PER_exten_len.append(dist)

	savgl_PER_exten_len=[]
	for i in range(0, len(pbsc1_X)):
		dist=signal_utils.calc_length(origin_savgl_pbsc1_X, origin_savgl_pbsc1_Y, savgl_pbsc1_X[i], savgl_pbsc1_Y[i])
		savgl_PER_exten_len.append(dist)
	
	sarimax_PER_exten_len=[]
	for i in range(0, len(pbsc1_X)):
		dist=signal_utils.calc_length(origin_sarimax_pbsc1_X, origin_sarimax_pbsc1_Y, sarimax_pbsc1_X[i], sarimax_pbsc1_Y[i])
		sarimax_PER_exten_len.append(dist)

	butter_PER_exten_len=[]
	for i in range(0, len(pbsc1_X)):
		dist=signal_utils.calc_length(origin_butter_pbsc1_X, origin_butter_pbsc1_Y, butter_pbsc1_X[i], butter_pbsc1_Y[i])
		butter_PER_exten_len.append(dist)

	fft_PER_exten_len=[]
	for i in range(0, len(pbsc1_X)):
		dist=signal_utils.calc_length(origin_fft_pbsc1_X, origin_fft_pbsc1_Y, fft_pbsc1_X[i], fft_pbsc1_Y[i])
		fft_PER_exten_len.append(dist)



	


	PER_length_for_plot={
	'PER_exten_len':PER_exten_len, 
	'smth_PER_exten_len (kernel=3 frames)':smth_PER_exten_len,
	'med_PER_exten_len (kernel=9 frames)':med_PER_exten_len,
	'savgl_PER_exten_len (kernel=13 frames)':savgl_PER_exten_len,
	'sarimax_PER_exten_len (default setting in Deeplabcut)':sarimax_PER_exten_len,
	'butter_PER_exten_len':butter_PER_exten_len,
	'fft_PER_exten_len (raw_trace - highpass trace (7-15 hz))':fft_PER_exten_len,
	}
	plot_utils.Plot_traces(series_set=PER_length_for_plot, savepath=outputPERdir+'Filtered_PER_length.png')



	# normalize entension length to baseline as baseline at 1 and fold of length

	norm_baseFold_PER_exten_len = signal_utils.normalize_trace(PER_exten_len, frame_window=300, mode='fold_of_baseline')
	norm_baseFold_smth_PER_exten_len = signal_utils.normalize_trace(smth_PER_exten_len, frame_window=300, mode='fold_of_baseline')
	norm_baseFold_med_PER_exten_len = signal_utils.normalize_trace(med_PER_exten_len, frame_window=300, mode='fold_of_baseline')
	norm_baseFold_savgl_PER_exten_len = signal_utils.normalize_trace(savgl_PER_exten_len, frame_window=300, mode='fold_of_baseline')
	norm_baseFold_sarimax_PER_exten_len = signal_utils.normalize_trace(sarimax_PER_exten_len, frame_window=300, mode='fold_of_baseline')
	norm_baseFold_fft_PER_exten_len = signal_utils.normalize_trace(fft_PER_exten_len, frame_window=300, mode='fold_of_baseline')


	PER_length_for_plot={
	'norm_baseFold_PER_exten_len':norm_baseFold_PER_exten_len, 
	'norm_baseFold_smth_PER_exten_len (kernel=3 frames)':norm_baseFold_smth_PER_exten_len,
	'norm_baseFold_med_PER_exten_len (kernel=9 frames)':norm_baseFold_med_PER_exten_len,
	'norm_baseFold_savgl_PER_exten_len (kernel=13 frames)':norm_baseFold_savgl_PER_exten_len,
	'norm_baseFold_sarimax_PER_exten_len (default setting in Deeplabcut)':norm_baseFold_sarimax_PER_exten_len,
	'norm_baseFold_fft_PER_exten_len':norm_baseFold_fft_PER_exten_len,
	}
	plot_utils.Plot_traces(series_set=PER_length_for_plot, savepath=outputPERdir+'Filtered_PER_length_baselineFold.png')


	norm_range_PER_exten_len ,_ ,_ = signal_utils.normalize_trace(PER_exten_len, frame_window=300, mode='btwn_0and1')
	norm_range_smth_PER_exten_len ,_ ,_ = signal_utils.normalize_trace(smth_PER_exten_len, frame_window=300, mode='btwn_0and1')
	norm_range_med_PER_exten_len ,_ ,_ = signal_utils.normalize_trace(med_PER_exten_len, frame_window=300, mode='btwn_0and1')
	norm_range_savgl_PER_exten_len ,_ ,_ = signal_utils.normalize_trace(savgl_PER_exten_len, frame_window=300, mode='btwn_0and1')
	norm_range_sarimax_PER_exten_len ,_ ,_ = signal_utils.normalize_trace(sarimax_PER_exten_len, frame_window=300, mode='btwn_0and1')
	norm_range_fft_PER_exten_len ,_ ,_ = signal_utils.normalize_trace(fft_PER_exten_len, frame_window=300, mode='btwn_0and1')


	norm_range_PER_length_for_plot={
	'norm_range_PER_exten_len':norm_range_PER_exten_len, 
	'norm_range_smth_PER_exten_len (kernel=3 frames)':norm_range_smth_PER_exten_len,
	'norm_range_med_PER_exten_len (kernel=9 frames)':norm_range_med_PER_exten_len,
	'norm_range_savgl_PER_exten_len (kernel=13 frames)':norm_range_savgl_PER_exten_len,
	'norm_range_sarimax_PER_exten_len':norm_range_sarimax_PER_exten_len,
	'norm_range_fft_PER_exten_len (raw_trace - highpass trace (7-15 hz))':norm_range_fft_PER_exten_len,
	}
	plot_utils.Plot_traces(series_set=norm_range_PER_length_for_plot, savepath=outputPERdir+'Filtered_PER_length_norm_0and1.png')



	# norm_med_PER_exten_len = np.gradient(norm_med_PER_exten_len,0.5)
	# smth_norm_dPER_exten_len=filtered_traces(norm_med_PER_exten_len, filtermode='running_window')
	# med_norm_dPER_exten_len=filtered_traces(norm_med_PER_exten_len, filtermode='median')
	# savgl_norm_dPER_exten_len=filtered_traces(norm_med_PER_exten_len, filtermode='savgol_filter')
	# sarimax_norm_dPER_exten_len=filtered_traces(norm_med_PER_exten_len, filtermode='sarimax')
	# fft_dPER_exten_len=filtered_traces(norm_med_PER_exten_len, filtermode='fft_filter')

	# dPER_for_plot={
	# 'norm_med_PER_exten_len':norm_med_PER_exten_len,
	# 'smth_norm_dPER_exten_len':smth_norm_dPER_exten_len,
	# 'med_norm_dPER_exten_len':med_norm_dPER_exten_len,
	# 'savgl_norm_dPER_exten_len':savgl_norm_dPER_exten_len,
	# 'sarimax_norm_dPER_exten_len':sarimax_norm_dPER_exten_len,
	# 'fft_dPER_exten_len':fft_dPER_exten_len,
	# }
	# plot_utils.Plot_traces(series_set=dPER_for_plot, savepath=outputPERdir+'Filtered_dPER_length_norm_0and1.png')


	evt_bin_trace, evt_startIdx_list, evt_endIdx_list = signal_utils.detect_PER_event(norm_range_med_PER_exten_len)
	print('max evt_bin_trace', max(evt_bin_trace))
	print('min evt_bin_trace', min(evt_bin_trace))
	print('evt_startIdx_list', evt_startIdx_list)
	print('len evt_startIdx_list', len(evt_startIdx_list))
	print('evt_endIdx_list', evt_endIdx_list)
	print('len evt_endIdx_list', len(evt_endIdx_list))




	for i, startidx in enumerate(evt_startIdx_list):
		endIdx=evt_endIdx_list[i]
		if endIdx<startidx:
			print('Evt_Start_Idx#'+str(startidx)+' has conflict with Evt_end_Idx#'+str(endIdx) + '... Please check again...')
			sys.exit(0)



	os_utils.save_PER_dic(filename='PER_labels_camera_6.p')











