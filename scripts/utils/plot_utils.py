

import matplotlib.pyplot as plt




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
	frames_series=np.arange(0,7440,1)

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





def Plot_movie_frame(current_Idx):

	print(Filt_PER_movie_dir)
	print('Frame:', current_Idx)

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


	PER_exten_len_flow, xax, xaxislimit = get_FlowTrace(PER_exten_len, current_Idx)
	smth_PER_exten_len_flow, xax, xaxislimit = get_FlowTrace(smth_PER_exten_len, current_Idx)
	med_PER_exten_len_flow, xax, xaxislimit = get_FlowTrace(med_PER_exten_len, current_Idx)
	savgl_PER_exten_len_flow, xax, xaxislimit = get_FlowTrace(savgl_PER_exten_len, current_Idx)
	sarimax_PER_exten_len_flow, xax, xaxislimit = get_FlowTrace(sarimax_PER_exten_len, current_Idx)


	titles=['Raw_deeplabcut_lables', 'Running_window (kernel=3 frames)', 'Median_filter (kernel=3 frames)', 'Savitzky–Golay_filter (kernel=3 frames)', 'Sarimax_filter_from_Deeplabcut']

	# print( (int(pbsc0_X[current_Idx]), int(pbsc0_Y[current_Idx])) )
	# print( (int(pbsc1_X[current_Idx]), int(pbsc1_Y[current_Idx])) )
	# print( (int(fix_pbsc0_X), int(fix_pbsc0_Y)) )
 
	#draw with raw labels
	cv2.circle(raw_PER_img,(int(pbsc0_X), int(pbsc0_Y)), 8, (0,0,255), -1)
	cv2.circle(raw_PER_img,(int(pbsc1_X[current_Idx]), int(pbsc1_Y[current_Idx])), 8, (0,255,0), -1)
	cv2.line(raw_PER_img, (int(pbsc0_X),int(pbsc0_Y)),(int(pbsc1_X[current_Idx]), int(pbsc1_Y[current_Idx])),(255,0,0),3)

	cv2.circle(smth_PER_img,(int(fix_pbsc0_X), int(fix_pbsc0_Y)), 8, (0,0,255), -1)
	cv2.circle(smth_PER_img,(int(smth_pbsc1_X[current_Idx]), int(smth_pbsc1_Y[current_Idx])), 8, (0,255,0), -1)
	cv2.line(smth_PER_img,(int(fix_pbsc0_X), int(fix_pbsc0_Y)),(int(smth_pbsc1_X[current_Idx]), int(smth_pbsc1_Y[current_Idx])),(255,0,0),3)

	cv2.circle(med_PER_img,(int(fix_pbsc0_X), int(fix_pbsc0_Y)), 8, (0,0,255), -1)
	cv2.circle(med_PER_img,(int(med_pbsc1_X[current_Idx]), int(med_pbsc1_Y[current_Idx])), 8, (0,255,0), -1)
	cv2.line(med_PER_img,(int(fix_pbsc0_X), int(fix_pbsc0_Y)),(int(med_pbsc1_X[current_Idx]), int(med_pbsc1_Y[current_Idx])),(255,0,0),3)

	cv2.circle(savgl_PER_img,(int(fix_pbsc0_X), int(fix_pbsc0_Y)), 8, (0,0,255), -1)
	cv2.circle(savgl_PER_img,(int(savgl_pbsc1_X[current_Idx]), int(savgl_pbsc1_Y[current_Idx])), 8, (0,255,0), -1)
	cv2.line(savgl_PER_img,(int(fix_pbsc0_X), int(fix_pbsc0_Y)),(int(savgl_pbsc1_X[current_Idx]), int(savgl_pbsc1_Y[current_Idx])),(255,0,0),3)

	cv2.circle(sarimax_PER_img,(int(fix_pbsc0_X), int(fix_pbsc0_Y)), 8, (0,0,255), -1)
	cv2.circle(sarimax_PER_img,(int(sarimax_pbsc1_X[current_Idx]), int(sarimax_pbsc1_Y[current_Idx])), 8, (0,255,0), -1)
	cv2.line(sarimax_PER_img,(int(fix_pbsc0_X), int(fix_pbsc0_Y)),(int(sarimax_pbsc1_X[current_Idx]), int(sarimax_pbsc1_Y[current_Idx])),(255,0,0),3)





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
	frNum=plt.text(20,40,current_Idx,color='r',size=25)

	raw_plt = plt.subplot2grid((y_span_fig, x_span_fig),(raw_plot_y, raw_plot_x),rowspan=plot_span_y,colspan=plot_span_x) 
	raw_plt.plot(xax, PER_exten_len_flow, label = "raw", color='r',linewidth=1.4)
	raw_plt.plot(current_Idx, PER_exten_len[current_Idx], marker = 'o', markersize = 5, color='y', markeredgewidth=4, markerfacecolor='y', markeredgecolor='y', linewidth=0)
	#raw_plt.axvline(current_Idx, linestyle='dashed',color='white',linewidth=1.4)
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
	smth_plot.plot(current_Idx, smth_PER_exten_len[current_Idx], marker = 'o', markersize = 5, color='y', markeredgewidth=4, markerfacecolor='y', markeredgecolor='y', linewidth=0)
	#smth_plot.axvline(current_Idx, linestyle='dashed',color='white',linewidth=1.4)
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
	med_plot.plot(current_Idx, med_PER_exten_len[current_Idx], marker = 'o', markersize = 5, color='y', markeredgewidth=4, markerfacecolor='y', markeredgecolor='y', linewidth=0)
	#med_plot.axvline(current_Idx, linestyle='dashed',color='white',linewidth=1.4)
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
	savgl_plot.plot(current_Idx, savgl_PER_exten_len[current_Idx], marker = 'o', markersize = 5, color='y', markeredgewidth=4, markerfacecolor='y', markeredgecolor='y', linewidth=0)
	#savgl_plot.axvline(current_Idx, linestyle='dashed',color='white',linewidth=1.4)
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
	sarimax_plot.plot(current_Idx, sarimax_PER_exten_len[current_Idx], marker = 'o', markersize = 5, color='y', markeredgewidth=4, markerfacecolor='y', markeredgecolor='y', linewidth=0)
	#sarimax_plot.axvline(current_Idx, linestyle='dashed',color='white',linewidth=1.4)
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

	#plt.tight_layout()
	plt.savefig(Filt_PER_movie_dir+'VidFrame' + "%05d" % current_Idx + '.jpg', facecolor=fig.get_facecolor(), edgecolor='none', transparent=True)
	plt.clf()	
	plt.close(fig)

	return


