

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
