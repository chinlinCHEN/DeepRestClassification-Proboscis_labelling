import numpy as np
import matplotlib.pyplot as plt
from skimage import io
import cv2
import os




def Plot_traces(series_set=None, savepath=None):

	if series_set==None:
		print('No data series to plot ...')
		pass

	else:
		print('Plotting '+savepath)

		keys_series_set=list(series_set.keys())
		values_series_set=list(series_set.values())

		fig=plt.figure(facecolor='black', figsize=(25, 10), dpi=200)
		for i in range(0, len(series_set)):
			plt.subplot(int(str(len(series_set))+'1'+str(i+1)))
			plt.plot(values_series_set[i], linewidth=1)
			plt.title(keys_series_set[i])
		plt.tight_layout()
		plt.savefig(savepath)
		plt.clf()
		plt.close(fig)


	return



def get_FlowTrace(trace, current_idx, flowrange_s=10):

	fps=30
	frames_per_flow=flowrange_s*fps
	flow_end_Idx=current_idx+int(frames_per_flow/2)
	frames_series=np.arange(0,len(trace),1)

	# print('frames_per_flow', frames_per_flow)
	# print('current_idx', current_idx)
	# print('flow_end_Idx', flow_end_Idx)
	# print('len(trace[0:flow_end_Idx])', len(trace[0:flow_end_Idx]))

	#The begining of data for video
	if len(trace[0:flow_end_Idx])<frames_per_flow:
		trace_flow = trace[0:flow_end_Idx]
		# x range for plotting against y
		xax=frames_series[0:flow_end_Idx]
		# x range for setting x-axis limit
		xaxislimit=[frames_series[current_idx]-frames_per_flow/2, frames_series[current_idx]+frames_per_flow/2]

	#The end of data for video
	elif len(trace[current_idx:-1])<frames_per_flow/2:
		trace_flow = trace[current_idx-(flow_end_Idx-current_idx):-1]
		# x range for plotting against y
		xax = frames_series[current_idx-(flow_end_Idx-current_idx):-1]
		# x range for setting x-axis limit
		xaxislimit=[frames_series[current_idx]-frames_per_flow/2, frames_series[current_idx]+frames_per_flow/2]

	else:
		trace_flow = trace[current_idx-(flow_end_Idx-current_idx):flow_end_Idx]
		# x range for plotting against y
		xax = frames_series[current_idx-(flow_end_Idx-current_idx):flow_end_Idx]
		# x range for setting x-axis limit
		xaxislimit=[frames_series[current_idx]-frames_per_flow/2, frames_series[current_idx]+frames_per_flow/2]

	return trace_flow, xax, xaxislimit






