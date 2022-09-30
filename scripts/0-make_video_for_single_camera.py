import os
import shutil
import sys



# output_Dir='/Users/clc/Documents/EPFL/NeLy/Data/ANproj/dlc/training_frames/'

# if not os.path.exists(output_Dir):
#     os.makedirs(output_Dir)


video_cam=6


rawdatalist=[
'../samples/',
]

#count_photo=0
for path in rawdatalist:
#for date, genotype, fly, recrd_num in experiments:
	

	input_Dir=path

	filename = 'video'
	print('filename', filename)

	output_Dir = '../outputs/'

	#output_Dir = '/Users/clc/Documents/EPFL/NeLy/Data/ANproj/'+date_genotype+'/'+Fly_num+'/'+CO2xzGG+'/'+recrd_num+'/'+'OptFlowData/'

	print('output_Dir', output_Dir)

	if not os.path.exists(output_Dir):
		print(output_Dir)
		os.makedirs(output_Dir)


	dir_cont_temp=sorted(os.listdir(input_Dir))
	dir_cont=[]
	for i, v in enumerate(dir_cont_temp):
		if v[-3:]=='jpg':
			dir_cont.append(v)

	video_start_number = dir_cont[0].split('.')[0].split('_')[-1]



	os.chdir(input_Dir)
	
	#os.system('/usr/local/Cellar/ffmpeg -r 30 -start_number 0 -i %d.jpg -vcodec libx264 -vf format=yuv420p -crf 0 output.mp4')
	#os.system('ffmpeg -y -r 30 -start_number 0 -i '+'camera_'+str(video_cam)+'_img_%d.jpg -vcodec libx264 -pix_fmt yuv420p -crf 10 '+filename+'.mp4')
	os.system('ffmpeg -y -r 30 -start_number '+str(video_start_number)+' -i '+'camera_'+str(video_cam)+'_img_%d.jpg -vcodec libx264 -pix_fmt yuv420p -crf 20 '+filename+'.mp4')
	os.system('cp -r '+ input_Dir+filename+'.mp4' + ' ' + output_Dir) # need to change into /mnt/


#output_Dir='/Users/clc/Documents/EPFL/NeLy/Data/ANproj/dlc/training_frames/'

#os.chdir(output_Dir)
#os.system('/usr/local/Cellar/ffmpeg -r 30 -start_number 0 -i %d.jpg -vcodec libx264 -vf format=yuv420p -crf 0 output.mp4')
#os.system('ffmpeg -y -r 30 -start_number 0 -i %d.jpg -vcodec libx264 -pix_fmt yuv420p -crf 10 output.mp4')
















