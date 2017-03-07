import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import MiniBatchKMeans, KMeans, SpectralClustering, DBSCAN, AgglomerativeClustering, AffinityPropagation
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import kneighbors_graph
from mpl_toolkits.mplot3d import Axes3D

def MultiDimensionalClusteringKmeans(Xmatrix, time, xdata, n_clusters=2, ax = None, show=False):

	seed = np.random.seed(0)
	colors = np.array([x for x in 'bgrcmykbgrcmykbgrcmykbgrcmyk'])
	colors = np.hstack([colors] * 20)

	#normalize dataset for easier parameter selection
	X = StandardScaler().fit_transform(Xmatrix)

	#algorithm KMeans
	kmeans = KMeans(n_clusters=n_clusters, random_state=seed)

	#Apply algorithm
	kmeans.fit(X)

	y_pred = kmeans.labels_.astype(np.int)
	centers = kmeans.cluster_centers_
	center_colors = colors[:len(centers)]

	#Representation

	if np.logical_and(show, ax != None):

		ax.set_title('Clustering Tech: ' + "KMEANS; " + 'Number of Clusters = ' + str(n_clusters), fontsize=15)

		ax.plot(time, xdata, color='lightgray', alpha=0.4)
		ax.scatter(time, xdata, color=colors[y_pred].tolist(), s=10)
		ax.set_xlabel("time (ms)")
		ax.set_ylabel("Amplitude")

		return X, y_pred, centers, center_colors

		# fig = plt.figure(5, figsize=(4, 3))
		# plt.clf()
		# ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)
		# plt.cla()
		#
		# ax.scatter(X[:, 2], X[:, 0], X[:, 1], color=colors[y_pred].tolist())

	elif np.logical_and(show, ax == None):
		fig, axis = plt.subplots(2,1)
		fig.tight_layout()
		axis[0].set_title('Clustering Tech: ' + "KMEANS; " + 'Number of Clusters = ' + str(n_clusters), fontsize=15)
		axis[0].plot(time, xdata, color='lightgray', alpha=0.4)
		axis[0].scatter(time, xdata, color=colors[y_pred].tolist(), s=10)
		axis[0].set_xlabel("time (ms)")
		axis[0].set_ylabel("Amplitude")
		axis[1].plot(y_pred)

		return X, y_pred, centers, center_colors

	else:

		return X, y_pred, centers, center_colors


def MultiDimensionalClusteringSPCL(Xmatrix, time, xdata, eigen_solver = 'arpack', n_clusters=2, ax = None, show=False):

	seed = np.random.seed(0)
	colors = np.array([x for x in 'bgrcmykbgrcmykbgrcmykbgrcmyk'])
	colors = np.hstack([colors] * 20)

	# normalize dataset for easier parameter selection
	X = StandardScaler().fit_transform(Xmatrix)
	# algorithm SpectralClustering
	SC = SpectralClustering(n_clusters=n_clusters, eigen_solver=eigen_solver, affinity="nearest_neighbors")

	# Apply algorithm
	fit = SC.fit(X)

	y_pred = fit.labels_.astype(np.int)

	# Representation
	if np.logical_and(show, ax == None):

		ax.set_title('Clustering Tech: ' + "SpectralClustering; " + 'Number of Clusters = ' + str(n_clusters), fontsize=15)
		ax.plot(time, xdata, color='lightgray', alpha=0.4)
		ax.scatter(time, xdata, color=colors[y_pred].tolist(), s=10)
		ax.set_xlabel("time (ms)")
		ax.set_ylabel("Amplitude")

		return X, y_pred

	elif np.logical_and(show, ax == None):

		fig, axis = plt.subplots(1, 1)
		fig.tight_layout()
		axis.plot(time, xdata, color='lightgray', alpha=0.4)
		axis.scatter(time, xdata, color=colors[y_pred].tolist(), s=10)
		axis.set_xlabel("time (ms)")
		axis.set_ylabel("Amplitude")

		return X, y_pred

	else:
		return X, y_pred

def MultiDimensionalClusteringAGG(Xmatrix, time, xdata, n_clusters=2, Linkage = 'ward', Affinity = 'euclidean', ax = None, show=False):

	# normalize dataset for easier parameter selection
	X = StandardScaler().fit_transform(Xmatrix)

	# connectivity matrix for structured Ward
	connectivity = kneighbors_graph(X, n_neighbors=10, include_self=False)
	# make connectivity symmetric
	connectivity = 0.5 * (connectivity + connectivity.T)

	seed = np.random.seed(0)
	colors = np.array([x for x in 'bgrcmykbgrcmykbgrcmykbgrcmyk'])
	colors = np.hstack([colors] * 20)


	if(Linkage is 'ward'):
		ward = AgglomerativeClustering(n_clusters=n_clusters, linkage='ward', connectivity=connectivity)
		# Apply algorithm
		fit = ward.fit(X)
	else:
		Agg = AgglomerativeClustering(n_clusters=n_clusters, linkage=Linkage, connectivity=connectivity, affinity=Affinity)
		# Apply algorithm
		fit = Agg.fit(X)

	y_pred = fit.labels_.astype(np.int)

	# Representation
	if np.logical_and(show, ax != None):

		ax.set_title('Clustering Tech: ' + "Agglomerative Clustering " + 'Number of Clusters = ' + str(n_clusters), fontsize=15)
		ax.plot(time, xdata, color='lightgray', alpha=0.4)
		ax.scatter(time, xdata, color=colors[y_pred].tolist(), s=10)
		ax.set_xlabel("time (ms)")
		ax.set_ylabel("Amplitude")

		return X, y_pred

	elif np.logical_and(show, ax == None):

		fig, axis = plt.subplots(1, 1)
		fig.tight_layout()
		axis.set_title('Clustering Tech: ' + "Agglomerative Clustering " + 'Number of Clusters = ' + str(n_clusters), fontsize=15)
		axis.plot(time, xdata, color='lightgray', alpha=0.4)
		axis.scatter(time, xdata, color=colors[y_pred].tolist(), s=10)
		axis.set_xlabel("time (ms)")
		axis.set_ylabel("Amplitude")

	else:

		return X, y_pred

def MultiDimensionalClusteringDBSCAN(Xmatrix, time, xdata, eps, ax=None, show=False):

	# normalize dataset for easier parameter selection
	X = StandardScaler().fit_transform(Xmatrix)

	colors = np.array([x for x in 'bgrcmykbgrcmykbgrcmykbgrcmyk'])
	colors = np.hstack([colors] * 20)

	# normalize dataset for easier parameter selection
	dbscan = DBSCAN(eps=eps)

	# Apply algorithm
	fit = dbscan.fit(X)

	y_pred = fit.labels_.astype(np.int)

	# Representation
	if np.logical_and(show, ax != None):

		ax.set_title('Clustering Tech: ' + "DBSCAN", fontsize=15)

		ax.plot(time, xdata, color='lightgray', alpha=0.4)
		ax.scatter(time, xdata, color=colors[y_pred].tolist(), s=10)
		ax.set_xlabel("time (ms)")
		ax.set_ylabel("Amplitude")

		return X, y_pred

	elif np.logical_and(show, ax == None):
		fig, axis = plt.subplots(1, 1)
		fig.tight_layout()
		axis.set_title('Clustering Tech: ' + "DBSCAN", fontsize=15)

		axis.plot(time, xdata, color='lightgray', alpha=0.4)
		axis.scatter(time, xdata, color=colors[y_pred].tolist(), s=10)
		axis.set_xlabel("time (ms)")
		axis.set_ylabel("Amplitude")

	else:

		return X, y_pred


# def MultidimensionalClustering(FeaturesMatrix, Xarray, Yarray, n_clusters = 2, ClusteringMethod = 'kmeans', ax= None, show = False):
# 	"""
# 	    @brief: Cluster multidimensional data.
# 	    The Clustering methods are based in the examples given by sklearn toolkit.
# 	    @param: FeaturesMatrix: Array or Matrix with features. Each features will be an array, and the matrix will be oriented column wise
# 	                   Xarray: The X axis of your data
# 	                   Yarray: The Y axis of your data
# 	                   n_clusters: number of clusters (applicable to some methods)
# 	                   ClusteringMethod: Method used for clustering.
# 	                        Applicable Methods: 'kmeans', 'minibatchkmeans', 'agg1', 'agg2', 'dbscan', 'affinity', 'spectral'
# 						for mor information about the methods: http://scikit-learn.org/stable/modules/clustering.html
# 	    @return: ClusteredData:
# 	    @example:
# 	                time = linspace(-2,2,0.1)
# 	                input_signal = sin(t)+randn(len(t))*0.1
# 	                signal_filt = smooth(x)
# 	    @see also:  numpy.hanning, numpy.hamming, numpy.bartlett, numpy.blackman,
# 	                numpy.convolve, scipy.signal.lfilter
# 	    @todo: the window parameter could be the window itself if an array instead
# 	    of a string
# 	    @bug: if window_len is equal to the size of the signal the returning
# 	    signal is smaller.
# 	    """
#
# 	# normalize dataset for easier parameter selection
# 	X = StandardScaler().fit_transform(FeaturesMatrix)