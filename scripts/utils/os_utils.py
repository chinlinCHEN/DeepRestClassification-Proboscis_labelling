
import pandas as pd 
import glob
import os
import h5py
import sys
import numpy as np
import pickle




def read_latest_h5(PER_h5_Dir):

	list_of_filenames = glob.glob(PER_h5_Dir+'*.h5')
	#print('list_of_filenames', list_of_filenames)

	File_create_time=[]
	for f in list_of_filenames:
		## Mac: stat.st_birthtime
		## Linux: No easy way to get creation time as in Mac, so we settle for modified time where the content is last modified: stat.st_mtime
		ctime=os.stat(f).st_mtime
		File_create_time.append(ctime)
	print('File_create_time', File_create_time)

	index_max=np.argmax(File_create_time)
	latest_h5_filename = list_of_filenames[index_max]
	print('latest_h5_filename', latest_h5_filename)

	latest_h5_file = h5py.File(latest_h5_filename,'r')




	return latest_h5_file


def extract_coord(h5File):

	table=h5File['df_with_missing']['table'][:]


	table_list=table


	Pbsc0_x=[]
	Pbsc0_y=[]
	Pbsc1_x=[]
	Pbsc1_y=[]
	for i in range(0,len(table_list)):
		Pbsc0_x.append(table_list[i][1][0])
		Pbsc0_y.append(table_list[i][1][1])
		Pbsc1_x.append(table_list[i][1][3])
		Pbsc1_y.append(table_list[i][1][4])




	return Pbsc0_x, Pbsc0_y, Pbsc1_x, Pbsc1_y








def save_PER_dic(filename='PER_camera_6.p'):


	dicData={}

	# Proboscis original coordinate
	dicData.update({'pbsc0_X':origin_med_pbsc1_X})
	dicData.update({'pbsc0_Y':origin_med_pbsc1_Y})
	
	dicData.update({'pbsc1_X':pbsc1_X})
	dicData.update({'pbsc1_Y':pbsc1_Y})

	# Proboscis fix coordinate of Pbsc0
	dicData.update({'fix_pbsc0_X':fix_pbsc0_X})
	dicData.update({'fix_pbsc0_Y':fix_pbsc0_Y})

	# Proboscis filtered coordinate of Pbsc0
	dicData.update({'smth_pbsc1_X':smth_pbsc1_X})
	dicData.update({'smth_pbsc1_Y':smth_pbsc1_Y})	

	dicData.update({'med_pbsc1_X':med_pbsc1_X})
	dicData.update({'med_pbsc1_Y':med_pbsc1_Y})	

	dicData.update({'savgl_pbsc1_X':savgl_pbsc1_X})
	dicData.update({'savgl_pbsc1_Y':savgl_pbsc1_Y})	

	dicData.update({'sarimax_pbsc1_X':sarimax_pbsc1_X})
	dicData.update({'sarimax_pbsc1_Y':sarimax_pbsc1_Y})

	# raw PER extension length
	dicData.update({'PER_exten_len':PER_exten_len})
	dicData.update({'smth_PER_exten_len':smth_PER_exten_len})		
	dicData.update({'med_PER_exten_len':med_PER_exten_len})
	dicData.update({'savgl_PER_exten_len':savgl_PER_exten_len})
	dicData.update({'sarimax_PER_exten_len':sarimax_PER_exten_len})	
	dicData.update({'fft_PER_exten_len':fft_PER_exten_len})	


	# PER extension normalized between 0 and 1
	dicData.update({'norm_range_PER_exten_len':norm_range_PER_exten_len})
	dicData.update({'norm_range_smth_PER_exten_len':norm_range_smth_PER_exten_len})		
	dicData.update({'norm_range_med_PER_exten_len':norm_range_med_PER_exten_len})
	dicData.update({'norm_range_savgl_PER_exten_len':norm_range_savgl_PER_exten_len})
	dicData.update({'norm_range_sarimax_PER_exten_len':norm_range_sarimax_PER_exten_len})
	dicData.update({'norm_range_fft_PER_exten_len':norm_range_fft_PER_exten_len})

	# PER extension (fold of baseline)
	dicData.update({'norm_baseFold_PER_exten_len':norm_baseFold_PER_exten_len})
	dicData.update({'norm_baseFold_smth_PER_exten_len':norm_baseFold_smth_PER_exten_len})		
	dicData.update({'norm_baseFold_med_PER_exten_len':norm_baseFold_med_PER_exten_len})
	dicData.update({'norm_baseFold_savgl_PER_exten_len':norm_baseFold_savgl_PER_exten_len})
	dicData.update({'norm_baseFold_sarimax_PER_exten_len':norm_baseFold_sarimax_PER_exten_len})
	dicData.update({'norm_baseFold_fft_PER_exten_len':norm_baseFold_fft_PER_exten_len})



	# PER events evt_bin_trace, evt_startIdx_list, evt_endIdx_list
	dicData.update({'evt_bin_trace':evt_bin_trace})
	dicData.update({'evt_startIdx_list':evt_startIdx_list})		
	dicData.update({'evt_endIdx_list':evt_endIdx_list})




	pickle.dump( dicData, open( outputPERdir + filename, "wb" ) ) 

	return





def openDicData(PER_output_dir):

	if os.path.exists(PER_output_dir+"/PER_labels_camera_6.p"):
		dicData = pickle.load( open( PER_output_dir+"/PER_labels_camera_6.p", "rb" ) )
		# Proboscis original coordinate
		pbsc0_X=dicData['pbsc0_X']
		pbsc0_Y=dicData['pbsc0_Y']
		
		pbsc1_X=dicData['pbsc1_X']
		pbsc1_Y=dicData['pbsc1_Y']

		# Proboscis fix coordinate of Pbsc0
		fix_pbsc0_X=dicData['fix_pbsc0_X']
		fix_pbsc0_Y=dicData['fix_pbsc0_Y']

		# Proboscis filtered coordinate of Pbsc0
		smth_pbsc1_X=dicData['smth_pbsc1_X']
		smth_pbsc1_Y=dicData['smth_pbsc1_Y']

		med_pbsc1_X=dicData['med_pbsc1_X']
		med_pbsc1_Y=dicData['med_pbsc1_Y']

		savgl_pbsc1_X=dicData['savgl_pbsc1_X']
		savgl_pbsc1_Y=dicData['savgl_pbsc1_Y']	

		sarimax_pbsc1_X=dicData['sarimax_pbsc1_X']
		sarimax_pbsc1_Y=dicData['sarimax_pbsc1_Y']	

		# PER extension length
		PER_exten_len=dicData['PER_exten_len']
		smth_PER_exten_len=dicData['smth_PER_exten_len']		
		med_PER_exten_len=dicData['med_PER_exten_len']
		savgl_PER_exten_len=dicData['savgl_PER_exten_len']
		sarimax_PER_exten_len=dicData['sarimax_PER_exten_len']	

		# norm PER extension length
		norm_PER_exten_len=dicData['norm_range_PER_exten_len']
		norm_smth_PER_exten_len=dicData['norm_range_smth_PER_exten_len']		
		norm_med_PER_exten_len=dicData['norm_range_med_PER_exten_len']
		norm_savgl_PER_exten_len=dicData['norm_range_savgl_PER_exten_len']
		norm_sarimax_PER_exten_len=dicData['norm_range_sarimax_PER_exten_len']			

	else:
		print ("File not found - PER_camera_6.p not analysed yet")
		sys.exit(0) 


	return pbsc0_X, pbsc0_Y, pbsc1_X, pbsc1_Y,\
			fix_pbsc0_X, fix_pbsc0_Y,\
			smth_pbsc1_X, smth_pbsc1_Y, med_pbsc1_X, med_pbsc1_Y, savgl_pbsc1_X, savgl_pbsc1_Y, sarimax_pbsc1_X, sarimax_pbsc1_Y,\
			PER_exten_len, smth_PER_exten_len, med_PER_exten_len, savgl_PER_exten_len, sarimax_PER_exten_len, \
			norm_PER_exten_len, norm_smth_PER_exten_len, norm_med_PER_exten_len, norm_savgl_PER_exten_len, norm_sarimax_PER_exten_len














