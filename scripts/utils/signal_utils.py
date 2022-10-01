
import pandas as pd 
import glob
import os
import h5py
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import math
import scipy.signal
import statsmodels.api as sm
import pickle
from skimage import io
from scipy.fftpack import rfft, irfft, fftfreq



def fix_point(pt_x_series, pt_y_series):

	fix_pt_x = np.mean(pt_x_series)
	fix_pt_y = np.mean(pt_y_series)

	# print('fix_pt_x', fix_pt_x)
	# print('fix_pt_y', fix_pt_y)

	return fix_pt_x, fix_pt_y


def find_origin_position(pt_x_series, pt_y_series):

	template_x_series=[1]*len(pt_x_series)
	template_y_series=[1]*len(pt_y_series)

	#print('pt_y_series', pt_y_series)

	#norm_x_series ,_ ,_ = normalize_trace(pt_x_series, frame_window=100, mode='btwn_0and1')
	norm_y_series ,_ ,_ = normalize_trace(pt_y_series, frame_window=10, mode='btwn_0and1')

	print('len(norm_y_series)', len(norm_y_series))
	print('norm_y_series', norm_y_series)
	print('max norm_y_series', max(norm_y_series))
	print('min norm_y_series', min(norm_y_series))




	for i, val in enumerate(norm_y_series):
		if val>0.25:
			template_x_series[i]=np.nan
			template_y_series[i]=np.nan


	baseline_x=np.multiply(pt_x_series, template_x_series)
	baseline_y=np.multiply(pt_y_series, template_y_series)

	print('baseline_x', baseline_x)
	print('baseline_y', baseline_y)

	major_pt_x=np.nanmean(baseline_x)
	major_pt_y=np.nanmean(baseline_y)

	print('major_pt_x', major_pt_x)
	print('major_pt_y', major_pt_y)


	# fig=plt.figure(facecolor='black', figsize=(25, 17), dpi=200)
	# plt.subplot(311)
	# plt.plot(norm_y_series)
	# plt.subplot(312)
	# plt.plot(template_y_series)
	# plt.subplot(313)
	# plt.plot(baseline_y)


	# plt.tight_layout()
	# plt.savefig(outputPERdir+'bin_pbsc1.jpg')
	# plt.clf()
	# plt.close(fig)



	return major_pt_x, major_pt_y



def calc_length(pt0_x, pt0_y, pt1_x, pt1_y):

	return math.sqrt( ((pt0_x-pt1_x)**2)+((pt0_y-pt1_y)**2) )


def smooth_trace(trace, frame_window=9):

	window = np.ones(frame_window)/frame_window
	trace_smooth = np.convolve(trace, window, mode='same')
	trace_smooth[0] = trace[0]
	trace_smooth[-1] = trace[-1]

	return trace_smooth


def savgol_filter(trace, frame_window=9, polyorder=3):

	trace_hat = scipy.signal.savgol_filter(trace, frame_window, polyorder)

	return trace_hat


def butter_lowpass_filter(data, cutOff, fs, order=3):

    nyq = 0.5 * fs
    normalCutoff = cutOff / nyq
    b, a = scipy.signal.butter(order, normalCutoff, btype='low', analog = True)
    y = scipy.signal.filtfilt(b, a, data)
    return y


def median_filter(trace, frame_window=9):

	return scipy.signal.medfilt(trace,kernel_size=frame_window)


def FitSARIMAXModel(x,pcutoff=10,alpha=0.1,ARdegree=3,MAdegree=1,nforecast = 0, disp=False):
    # Seasonal Autoregressive Integrated Moving-Average with eXogenous regressors (SARIMAX)
    # see http://www.statsmodels.org/stable/statespace.html#seasonal-autoregressive-integrated-moving-average-with-exogenous-regressors-sarimax
    Y=x.copy()
    Y=np.asarray(Y)
    #Y[p<pcutoff]=np.nan # Set uncertain estimates to nan (modeled as missing data)
    if np.sum(np.isfinite(Y))>10:

        # SARIMAX implemetnation has better prediction models than simple ARIMAX (however we do not use the seasonal etc. parameters!)
        mod = sm.tsa.statespace.SARIMAX(Y.flatten(), order=(ARdegree,0,MAdegree),seasonal_order=(0, 0, 0, 0),simple_differencing=True)
        #Autoregressive Moving Average ARMA(p,q) Model
        #mod = sm.tsa.ARIMA(Y, order=(ARdegree,0,MAdegree)) #order=(ARdegree,0,MAdegree)
        try:
            res = mod.fit(disp=disp)
        except ValueError: #https://groups.google.com/forum/#!topic/pystatsmodels/S_Fo53F25Rk (let's update to statsmodels 0.10.0 soon...)
            startvalues=np.array([convertparms2start(pn) for pn in mod.param_names])
            res= mod.fit(start_params=startvalues,disp=disp)
        except np.linalg.LinAlgError:
            # The process is not stationary, but the default SARIMAX model tries to solve for such a distribution...
            # Relaxing those constraints should do the job.
            mod = sm.tsa.statespace.SARIMAX(Y.flatten(), order=(ARdegree, 0, MAdegree),
                                            seasonal_order=(0, 0, 0, 0), simple_differencing=True,
                                            enforce_stationarity=False, enforce_invertibility=False,
                                            use_exact_diffuse=False)
            res = mod.fit(disp=disp)

        predict = res.get_prediction(end=mod.nobs + nforecast-1)
        predict.predicted_mean[0]=Y[0]

        return predict.predicted_mean,predict.conf_int(alpha=alpha)

    else:
        return np.nan*np.zeros(len(Y)),np.nan*np.zeros((len(Y),2))


def fft_filter(trace, lf=2.5,hf=1.5, filename='fft_space.png'):

	fps=30
	start_time=0
	end_time=int(len(trace)/fps)
	time=np.linspace(start_time,end_time,len(trace))
	trace_copy=trace.copy()
	signal=np.asarray(trace_copy)

	

	W = fftfreq(signal.size, d=time[1]-time[0])
	f_signal = rfft(signal)
	f_signal[(W<0.1)] = 0

	# print('W',W)
	# print('len W', len(W))

	# If our original signal time was in seconds, this is now in Hz    
	band_f_signal = f_signal.copy()
	band_f_signal[(W<hf)] = 0
	band_f_signal[(W>lf)] = 0
	band_signal = irfft(band_f_signal)

	high_f_signal = f_signal.copy()
	high_f_signal[(W<7)] = 0
	high_f_signal[(W>15)] = 0
	high_signal = irfft(high_f_signal)

	low_f_signal = f_signal.copy()
	low_f_signal[(W<0)] = 0
	low_f_signal[(W>0.6)] = 0
	low_signal = irfft(low_f_signal)

	# Substract raw signal from low and high signals
	#Sub_raw_signal=signal-high_signal-low_signal
	Sub_raw_signal=signal-high_signal

	# #Plot fft
	# print('Plotting f-space of fft filter')
	# fig=plt.figure(facecolor='black', figsize=(25, 17), dpi=200)
	
	# plt.subplot(911)
	# plt.title('raw_signal')
	# plt.plot(time,signal)
	
	# plt.subplot(912)
	# plt.title('raw_f_signal')
	# plt.plot(W,f_signal)

	# plt.subplot(913)
	# plt.title('band_signal, '+str(lf)+'hz > W > '+str(hf)+' hz')
	# plt.plot(time, band_signal)

	# plt.subplot(914)
	# plt.title('band_f_signal, '+str(lf)+'hz > W > '+str(hf)+' hz')
	# plt.plot(W, band_f_signal)

	# plt.subplot(915)
	# plt.title('high_signal, 15 hz > W > 7 hz')
	# plt.plot(time, high_signal)

	# plt.subplot(916)
	# plt.title('high_f_signal, 15 hz > W > 7 hz')
	# plt.plot(W, high_f_signal)	

	# plt.subplot(917)
	# plt.title('low_signal, 0.6 hz > W > 0 hz')
	# plt.plot(time, low_signal)

	# plt.subplot(918)
	# plt.title('low_f_signal, 0.6 hz > W > 0 hz')
	# plt.plot(W, low_f_signal)

	# plt.subplot(919)
	# plt.title('raw_signal-high_signal')
	# plt.plot(time, Sub_raw_signal)



	# plt.tight_layout()
	# plt.savefig(outputPERdir+filename)
	# plt.clf()
	# plt.close(fig)



	return Sub_raw_signal


def filtered_traces(trace, filtermode='median', **kwargs):

	trace_copy=trace.copy()


	if filtermode == 'running_window':
		trace_filt=smooth_trace(trace_copy, frame_window=3)

	elif filtermode == 'median':
		trace_filt=median_filter(trace_copy, frame_window=9)

	elif filtermode=='savgol_filter':
		trace_filt=savgol_filter(trace_copy, frame_window=13, polyorder=2)

	elif filtermode=='sarimax':
		trace_filt, CI=FitSARIMAXModel(trace_copy)

	elif filtermode=='butter_lowpass':
		trace_filt = butter_lowpass_filter(trace_copy, cutOff=0.03, fs=30, order=2) # cutoff frequency in rad/s; sampling frequency in rad/s; order of filter
	
	elif filtermode=='fft_filter':
		trace_filt=fft_filter(trace_copy, lf=7,hf=-0.01, filename='fft_space.png')

	return trace_filt
	


def normalize_trace(trace, frame_window=100, mode=None):


	if mode == 'btwn_0and1':

		max_val=max(trace)

		print('max_val', max_val)

		smth_trace=smooth_trace(trace,frame_window)
		#print('smth_trace', smth_trace)
		print('min smth_trace', min(smth_trace))
		print('max smth_trace', max(smth_trace))


		#baseline = np.nanmin(smth_trace[int((1/7)*len(trace)):int((6/7)*len(trace))])


		temp_trace=[1]*len(trace)
		mean_trace = np.nanmean(smth_trace) 
		for i, val in enumerate(trace):
			if val>1.3*mean_trace:
				temp_trace[i]=np.nan
		
		baseline=np.nanmean(np.multiply(trace, temp_trace))



		print('baseline', baseline)

		range_trace=max_val-baseline
		print('range_trace', range_trace)
		
		# plt.plot(smth_trace)
		# plt.show()
		# plt.pause(3)
		# plt.clf()

		#print('min(np.asarray(trace)-baseline)' , min(np.asarray(trace)-baseline))
		norm_0and1_trace=(np.asarray(trace)-baseline)/range_trace

		# norm_0and1_trace=[]
		# for val in trace:
		# 	norm_val=(val-baseline)/range_trace
		# 	norm_0and1_trace.append(norm_val)

		return norm_0and1_trace, range_trace, baseline


	elif mode == 'fold_of_baseline':

		smth_trace=smooth_trace(trace,frame_window)
		if len(trace)>5000:
			baseline = min(smth_trace[int((1/7)*len(trace)):int((6/7)*len(trace))])
		else:
			baseline = min(smth_trace) 


		norm_trace = (np.asarray(trace)-baseline)/baseline



		return norm_trace



	


def find_nearest(ori_array, ori_value, condition=None, height_cond=None):
    

	array = np.asarray(ori_array)
	# print('array', array)
	# print('len array', len(array))

	if condition==None:
		idx = (np.abs(ori_array - ori_value)).argmin()

		return ori_array[idx]

	elif condition=='over_max':

		array, range_trace, baseline=normalize_trace(ori_array,frame_window=1, mode='btwn_0and1')
		value=(ori_value-baseline)/range_trace

		if len(array)<10:
			
			print('Skip detecting end point of this event! It is too short!')
			return ori_array[1]

		else:

			peak_idx_array, _ = scipy.signal.find_peaks(array, height=0.5)
			if len(peak_idx_array)==0:
				max_idx=array.argmax()
			else:
				max_idx=peak_idx_array[0]

			# print('max_idx', max_idx)
			# print('array', array)
			# print('len array', len(array))
			#print('array[max_idx:-1]', array[max_idx:-1])

			# if the array is too short, then skip



			Similarity_with_value = 1 - np.abs(array[max_idx:-1] - value) 
			similarity_to_startVal=0.8
			local_max_idx, _ = scipy.signal.find_peaks(Similarity_with_value, height=similarity_to_startVal)

			similarity_grid=sorted(np.arange(0.5, 0.9, step=0.05), reverse = True)
			#print('similarity_grid',similarity_grid)

			for i, similarity in enumerate(similarity_grid):
				local_max_idx, _ = scipy.signal.find_peaks(Similarity_with_value, height=similarity)
				# print('similarity',similarity,'local_max_idx',local_max_idx)
				if len(local_max_idx)==0:
					if i==len(similarity_grid)-1:
						print('	no local maximum found ... ')
						print('	Instead looking for closet value  ... ')
						print('similarity', similarity)
						print('Similarity_with_value', Similarity_with_value)
						Similarity_with_value_thres=np.asarray(list(Similarity_with_value).copy())
						Similarity_with_value_thres[(np.asarray(Similarity_with_value)<similarity)]=0

						if np.sum(Similarity_with_value_thres)==0:
							if max_idx==len(array)-1:
								print('	max_idx')
								idx=max_idx
							else:
								print('	all values < threshold...')
								print('	take last value as the end of the event...')
								idx_temp=len(Similarity_with_value_thres)-1
								idx=max_idx+idx_temp
								# print('idx_temp',idx_temp)

						else:
							idx_temp=Similarity_with_value_thres.argmax()
							idx=max_idx+idx_temp 
							# print('idx_temp',idx_temp)

							# plt.title('similarity ='+str(similarity)+' frame# ='+str(idx))
							# plt.plot(Similarity_with_value_thres)
							# plt.plot(idx_temp, Similarity_with_value_thres[idx_temp], 'ro')
							# plt.savefig(outputPERdir+'local_evt_no_local_max.png')
							# plt.clf()


					else:
						continue

				else:
					idx=max_idx+local_max_idx[0]


					# plt.title('similarity ='+str(similarity)+' frame# ='+str(idx))
					# plt.plot(0-max_idx,value,'x')
					# plt.plot(array[max_idx:-1],'r') 
					# plt.plot(np.abs(array[max_idx:-1] - value),'g')
					# plt.plot(Similarity_with_value,'b')
					# plt.plot(local_max_idx, Similarity_with_value[local_max_idx], "x")
					# plt.plot(idx-max_idx, array[idx], "v")

					# plt.savefig(outputPERdir+'local_evt.png')
					# plt.clf()

					break			

			##Normalize y-value with x-value for detecting distance between start point and end point
			# scaling_factor_for_fair_dist_cal=int(len(array[max_idx:-1])/max(array[max_idx:-1]))
			# slope_list=[]
			# dist_list=[]
			# for i, val in enumerate(array[max_idx:-1]):
			# 	dist=calc_length(0, value*scaling_factor_for_fair_dist_cal, max_idx+i, array[max_idx+i]*scaling_factor_for_fair_dist_cal)
			# 	dist_list.append(dist)
			# 	slope=np.abs((array[max_idx+i]-value)/(max_idx+i-0))
			# 	slope_list.append(slope)
			
			# print('len slope_list', len(slope_list))
			# print('len dist_list', len(dist_list))

			# min_slope_idx=np.asarray(slope_list).argmin()
			# min_dist_idx=np.asarray(dist_list).argmin()
			# print('min_slope_idx', min_slope_idx)
			# print('min_dist_idx', min_dist_idx)
			# idx=min_dist_idx


			return ori_array[idx]




def detect_kinx(trace, peaks_idx, mode='forward', srch_range=0.4, no_after_these_idx=None, height_cond=None):

	print(mode+' detecting ...')

	thrsld_facotor=0.2 # % of peak as event starting threshold
	data_samplerate=30



	evt_kinx_idx_series=[]




	for i, peak_idx in enumerate(peaks_idx):

		ajst_thrsld = trace[peak_idx]*thrsld_facotor

		if mode=='forward':
			
			if int(peak_idx-data_samplerate*srch_range)>0:
				nearest_value=find_nearest(trace[int(peak_idx-data_samplerate*srch_range):int(peak_idx)], ajst_thrsld)
			elif int(peak_idx-data_samplerate*srch_range)<=0:
				nearest_value=find_nearest(trace[0:int(peak_idx)], ajst_thrsld)

			nearest_value_idx = np.where(trace == nearest_value)
		# print('ddata_series searching range:', int(peak_idx-data_samplerate*srch_range), int(peak_idx))
		# print('nearest_value_idx', nearest_value_idx)

		elif mode=='backward':

			height_cond_val=height_cond[i]*0.7

			# Not touch trace end
			
			if int(peak_idx+data_samplerate*srch_range)<len(trace)-1:
				print('Evt# '+str(i)+' at frame# '+str(peak_idx)+': '+'backward not touch trace end')
				
				# Not last start idx
				if i+1<len(no_after_these_idx):
					# print('Not last start idx')
					# Not touch next start idx
					if int(peak_idx+data_samplerate*srch_range)<no_after_these_idx[i+1]:
						print('Evt# '+str(i)+' at frame# '+str(peak_idx)+': '+'Not touch next start idx')
						nearest_value=find_nearest(trace[int(peak_idx):int(peak_idx+data_samplerate*srch_range)], trace[peak_idx], condition='over_max', height_cond=height_cond_val)
						#print('int(peak_idx', int(peak_idx), 'int(peak_idx+data_samplerate*srch_range)',int(peak_idx+data_samplerate*srch_range))
					#Touch next start idx
					else:
						# print('touch next start idx')
						# print('i',i)
						# print('peak_idx', peak_idx)
						# print('peaks_idx', peaks_idx)
						# print('no_after_these_idx', no_after_these_idx)
						# print('no_after_these_idx[i+1]-1', no_after_these_idx[i+1]-1)
						nearest_value=find_nearest(trace[int(peak_idx):no_after_these_idx[i+1]], trace[peak_idx], condition='over_max', height_cond=height_cond_val)
				
				# Last start idx
				else:		
					print('Evt# '+str(i)+' at frame# '+str(peak_idx)+': '+'Last start idx')		
					nearest_value=find_nearest(trace[int(peak_idx):int(peak_idx+data_samplerate*srch_range)], trace[peak_idx], condition='over_max', height_cond=height_cond_val)

			# Touch trace end
			else:
				print('Evt# '+str(i)+' at frame# '+str(peak_idx)+': '+'backward touch trace end')
				if i+1<len(no_after_these_idx):
					print('Evt# '+str(i)+' at frame# '+str(peak_idx)+': '+'Not last start idx')
					# Not touch next start idx
					if int(peak_idx+data_samplerate*srch_range)<no_after_these_idx[i+1]:
						print('Evt# '+str(i)+' at frame# '+str(peak_idx)+': '+'Not touch next start idx')
						nearest_value=find_nearest(trace[int(peak_idx):-1], trace[peak_idx], condition='over_max', height_cond=height_cond_val)
					#Touch next start idx
					else:
						print('Evt# '+str(i)+' at frame# '+str(peak_idx)+': '+'touch next start idx')
						nearest_value=find_nearest(trace[int(peak_idx):no_after_these_idx[i+1]], trace[peak_idx], condition='over_max', height_cond=height_cond_val)
				
				# Last start idx
				else:		
					print('Evt# '+str(i)+' at frame# '+str(peak_idx)+': '+'Last start idx')		
					nearest_value=find_nearest(trace[int(peak_idx):-1], trace[peak_idx], condition='over_max', height_cond=height_cond_val)

			#print('nearest_value', nearest_value)

			nearest_value_idx = np.where(trace == nearest_value)

			#if i == 17:
			#if i == 21:
			# if i == len(peaks_idx)-2:
			# if i == len(peaks_idx)-6:
			# # if i == 7:
			# # if i == 12:
			#  	sys.exit(0)


		evt_kinx_idx_series.append(nearest_value_idx[0][0])
		evt_kinx_idx_series.sort()


	return evt_kinx_idx_series



def diff_trace(trace, samplerate=1, diff_window_s=0.2 ):

	intvl_dif=int(samplerate*diff_window_s)
	ddata_series=[]
	for i in range(0,len(trace)-intvl_dif):
		ddatapoint = trace[i+intvl_dif]-trace[i]
		ddata_series.append(ddatapoint) 

    
	# put 0 to the place where there is no derivative
	for i in range(0,len(trace)-len(ddata_series)):
		ddata_series.append(0)   

	return ddata_series



def detect_PER_event(trace, outputPERdir, event_max_dur=2, event_min_dur=0.27):

	print('Detecting events...')

	fps=30
	
	diff_thrsld=0.03

	evt_min_dur=int(event_min_dur*fps)
	raw_thrsld=0.2
	raw_change_thrsld=0.1


	#grad_trace = np.gradient(trace,0.25)
	grad_trace = diff_trace(trace, samplerate=fps, diff_window_s=0.1)
	grad_trace = filtered_traces(grad_trace, filtermode='running_window')



	peaks_idx_rawTrace, _ = scipy.signal.find_peaks(trace, height = raw_thrsld, distance=25)
	peaks_idx_gradTrace, _ = scipy.signal.find_peaks(grad_trace, height = diff_thrsld, distance=25)
	#peaks_idx_gradTrace_cwt = scipy.signal.find_peaks_cwt(grad_trace, np.arange(1,20), max_distances=np.arange(1, 30)*2)
	#print('peaks_idx', peaks_idx)
	

	peaks_of_rawTrace_on_rawTrace = np.array(trace)[peaks_idx_rawTrace]

	peaks_of_gradTrace_on_rawTrace = np.array(trace)[peaks_idx_gradTrace]
	peaks_of_gradTrace_on_gradTrace = np.array(grad_trace)[peaks_idx_gradTrace]

	# peaks_idx_gradTrace_cwt_on_rawTrace = np.array(trace)[peaks_idx_gradTrace_cwt]
	# peaks_idx_gradTrace_cwt_on_gradTrace = np.array(grad_trace)[peaks_idx_gradTrace_cwt]

	# Find start kinx of event
	kinx_idx_rawTrace=detect_kinx(grad_trace, peaks_idx_gradTrace, mode='forward', srch_range=0.4)
	
	# Backward find nearest point of kinx as for the end of the event
	end_idx_rawTrace=detect_kinx(trace, kinx_idx_rawTrace, mode='backward', srch_range=event_max_dur, no_after_these_idx=kinx_idx_rawTrace, height_cond=peaks_of_gradTrace_on_rawTrace)

	# print('kinx_idx_rawTrace', kinx_idx_rawTrace)
	# print('len kinx_idx_rawTrace', len(kinx_idx_rawTrace))

	# print('end_idx_rawTrace', end_idx_rawTrace)
	# print('len end_idx_rawTrace', len(end_idx_rawTrace))	

	startIdx_rawTrace, endIdx_rawTrace=clean_FalsePositive_detection(kinx_idx_rawTrace, end_idx_rawTrace, trace, mode='remove_short_period', threshold=evt_min_dur)
	startIdx_rawTrace, endIdx_rawTrace=clean_FalsePositive_detection(startIdx_rawTrace, endIdx_rawTrace, trace, mode='remove_small_value',threshold=raw_thrsld)
	startIdx_rawTrace, endIdx_rawTrace=clean_FalsePositive_detection(startIdx_rawTrace, endIdx_rawTrace, trace, mode='remove_small_change',threshold=raw_change_thrsld)

	start_idx_rawTrace_on_rawTrace = np.array(trace)[startIdx_rawTrace]
	start_idx_rawTrace_on_gradTrace = np.array(grad_trace)[startIdx_rawTrace]	
	end_idx_rawTrace_on_rawTrace = np.array(trace)[endIdx_rawTrace]

	evt_bin_trace=[0]*len(trace)
	for i, evt_startIdx in enumerate(startIdx_rawTrace):
		evt_endIdx=endIdx_rawTrace[i]
		for j in range(evt_startIdx, evt_endIdx+1):
			evt_bin_trace[j]=1




	print('==Plot preview of PER event detection==')
	fig=plt.figure(facecolor='black', figsize=(25, 10), dpi=200)
	
	plt.subplot(311)
	plt.title('PER_trace')
	plt.plot(trace, color='k', linewidth=1)
	#plt.plot(trace_med, color='r', linewidth=1)
	#plt.plot(peaks_idx_rawTrace, peaks_of_rawTrace_on_rawTrace, marker='x', color='r',linestyle = 'None')
	#plt.plot(peaks_idx_gradTrace, peaks_of_gradTrace_on_rawTrace, marker='o', color='g',linestyle = 'None')
	plt.plot(startIdx_rawTrace, start_idx_rawTrace_on_rawTrace, marker='^', color='b',linestyle = 'None')
	plt.plot(endIdx_rawTrace, end_idx_rawTrace_on_rawTrace, marker='v', color='r',linestyle = 'None')
	for i, evt_startIdx in enumerate(startIdx_rawTrace):
		evt_endIdx=endIdx_rawTrace[i]
		plt.axvspan(evt_startIdx, evt_endIdx, color='k', alpha=0.25, linewidth=0)
	
	plt.subplot(312)
	plt.title('grad_PER_trace')
	plt.plot(grad_trace, color='k',linewidth=1)
	plt.plot(peaks_idx_gradTrace, peaks_of_gradTrace_on_gradTrace, marker='o', color='g',linestyle = 'None')
	plt.plot(startIdx_rawTrace, start_idx_rawTrace_on_gradTrace, marker='^', color='b',linestyle = 'None')
	for i, evt_startIdx in enumerate(startIdx_rawTrace):
		evt_endIdx=endIdx_rawTrace[i]
		plt.axvspan(evt_startIdx, evt_endIdx, color='k', alpha=0.25, linewidth=0)
	

	plt.subplot(313)
	plt.title('Binary PER event trace')
	plt.plot(evt_bin_trace, color='k',linewidth=1)

	
	plt.tight_layout()
	plt.savefig(outputPERdir+'PER_event.png')
	plt.clf()
	plt.close(fig)



	# PER_event_for_plot={
	# 'PER_trace':trace,
	# 'grad_PER_trace':grad_PER_trace,
	# #'PER_event':PER_event, 
	# }
	# Plot_traces(series_set=PER_event_for_plot, savepath=outputPERdir+'PER_event.png')


	return evt_bin_trace, startIdx_rawTrace, endIdx_rawTrace


def clean_FalsePositive_detection(startIdx_series, stopIdx_series, ref_trace, mode='remove_small', threshold=0.5):

	if mode=='remove_small_change':

		new_startIdx_series=[]
		new_stopIdx_series=[]
		for i, evt_startIdx in enumerate(startIdx_series):
			evt_endIdx=stopIdx_series[i]

			startVal=ref_trace[evt_startIdx]
			pealVal=max(ref_trace[evt_startIdx:evt_endIdx])

			if (pealVal-startVal)>threshold:
				new_startIdx_series.append(evt_startIdx)
				new_stopIdx_series.append(evt_endIdx)


	elif mode=='remove_small_value':

		new_startIdx_series=[]
		new_stopIdx_series=[]
		for i, evt_startIdx in enumerate(startIdx_series):
			evt_endIdx=stopIdx_series[i]

			pealVal=max(ref_trace[evt_startIdx:evt_endIdx])
			if pealVal>threshold:
				new_startIdx_series.append(evt_startIdx)
				new_stopIdx_series.append(evt_endIdx)		


	elif mode=='remove_short_period':
		new_startIdx_series=[]
		new_stopIdx_series=[]		
		for i, evt_startIdx in enumerate(startIdx_series):
			evt_endIdx=stopIdx_series[i]

			if (evt_endIdx-evt_startIdx)>threshold:
				new_startIdx_series.append(evt_startIdx)
				new_stopIdx_series.append(evt_endIdx)

	return new_startIdx_series, new_stopIdx_series




# def detect_PER_cluster():

# 	return















