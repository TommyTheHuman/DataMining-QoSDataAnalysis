n_fold_split = 6

# Resampling configuration parameters
under_sampling_c1 = 2000
under_sampling_c2 = 2000
under_sampling_c3 = 635

over_sampling_c1 = 40924
over_sampling_c2 = 20000
over_sampling_c3 = 10000

# Feature selection
feature_selection = 0

# Classifier parameters
knn_neighbors = 5
bdt_max_depth = 6
rf_max_depth = 6

# Choose the rebalancing method
entire = 1
undersampling = 0
oversampling = 0
SMOTE = 0

# Choose classifier
KNN = 1
BDT = 0
naiveGaussian = 0
RF = 0

# Graph Construction
graph = 0

import time
from matplotlib.legend_handler import HandlerBase
import numpy as np
import matplotlib.pyplot as plt
import Classifier.BinaryDecisionTree as bdt
import Classifier.KNN as knn
import Classifier.NaiveGaussianBayes as naive_gaus
import Classifier.RandomForest as rf

if __name__ == '__main__':

    if feature_selection == 1:
        print("feature selection")
    if entire == 1:
        print("entire")
    if undersampling == 1:
        print("undersampling " + str(under_sampling_c1) + " " + str(under_sampling_c2) + " " + str(under_sampling_c3))
    if oversampling == 1:
        print("oversampling " + str(over_sampling_c1) + " " + str(over_sampling_c2) + " " + str(over_sampling_c3))
    if SMOTE == 1:
        print("SMOTE")

#   Binary Tree Decision Classifier
    if BDT == 1:
        startBDT = time.perf_counter()
        print("BDT")
        if feature_selection == 1:
            if entire == 1:
                bdt.tree_on_entire_dataset_feature_selection()
            if undersampling == 1:
                bdt.tree_with_undersampling_feature_selection()
            if oversampling == 1:
                bdt.tree_with_oversampling_feature_selection()
            if SMOTE == 1:
                bdt.tree_with_SMOTENN_feature_selection()
        else:
            if entire == 1:
                bdt.tree_on_entire_dataset()
            if undersampling == 1:
                bdt.tree_with_undersampling()
            if oversampling == 1:
                bdt.tree_with_oversampling()
            if SMOTE == 1:
                bdt.tree_with_SMOTENN()
        endBDT = time.perf_counter()
        print("TOT time execution BDT: " + str(endBDT-startBDT))

#   KNN Classifier
    if KNN == 1:
        print("KNN")
        startKNN = time.perf_counter()
        if feature_selection == 1:
            if entire == 1:
                knn.knn_on_entire_dataset_feature_selection()
            if undersampling == 1:
                knn.knn_on_undersampled_dataset_feature_selection()
            if oversampling == 1:
                knn.knn_on_oversampled_dataset_feature_selection()
            if SMOTE == 1:
                knn.knn_with_SMOTENN_feature_selection()
        else:
            if entire == 1:
                knn.knn_on_entire_dataset()
            if undersampling == 1:
                knn.knn_on_undersampled_dataset()
            if oversampling == 1:
                knn.knn_on_oversampled_dataset()
            if SMOTE == 1:
                knn.knn_with_SMOTENN()
        endKNN = time.perf_counter()
        print("TOT time execution KNN: " + str(endKNN - startKNN))


#   Naive Gaussian Bayes Classifier
    if naiveGaussian == 1:
        print("NaiveGaussian")
        startNG = time.perf_counter()
        if feature_selection == 1:
            if entire == 1:
                naive_gaus.naive_GaussianBayesClassifier_on_entire_dataset_feature_selection()
            if undersampling == 1:
                naive_gaus.naive_GaussianBayesClassifier_on_undersampled_dataset_feature_selection()
            if oversampling == 1:
                naive_gaus.naive_GaussianBayesClassifier_on_oversampled_dataset_feature_selection()
            if SMOTE == 1:
                naive_gaus.naive_GaussianBayesClassifier_with_SMOTENN_feature_selection()
        else:
            if entire == 1:
                naive_gaus.naive_GaussianBayesClassifier_on_entire_dataset()
            if undersampling == 1:
                naive_gaus.naive_GaussianBayesClassifier_on_undersampled_dataset()
            if oversampling == 1:
                naive_gaus.naive_GaussianBayesClassifier_on_oversampled_dataset()
            if SMOTE == 1:
                naive_gaus.naive_GaussianBayesClassifier_with_SMOTENN()
        endNG = time.perf_counter()
        print("TOT time execution NG: " + str(endNG - startNG))

#    Random Forest Classifier
    if RF == 1:
        print("RF")
        startRF = time.perf_counter()
        if feature_selection == 1:
            if entire == 1:
                rf.RandomForest_on_entire_dataset_feature_selection()
            if undersampling == 1:
                rf.RandomForest_on_undersampled_dataset_feature_selection()
            if oversampling == 1:
                rf.RandomForest_on_oversampled_dataset_feature_selection()
            if SMOTE == 1:
                rf.randomForest_with_SMOTENN_feature_selection()
        else:
            if entire == 1:
                rf.RandomForest_on_entire_dataset()
            if undersampling == 1:
                rf.RandomForest_on_undersampled_dataset()
            if oversampling == 1:
                rf.RandomForest_on_oversampled_dataset()
            if SMOTE == 1:
                rf.randomForest_with_SMOTENN()
        endRF = time.perf_counter()
        print("TOT time execution RF: " + str(endRF - startRF))

# Graph Construction
    if graph == 1:
        N = 6

        # x = recall, y = precision

        # Original dataset
        # Mild
        x = [0.6935, 0.7136, 0.2197, 0.1422, 0.1837, 0.7370]
        y = [0.7588, 0.7646, 0.3674, 0.4347, 0.2707, 0.8249]
        # Severe
        x = [0.3993, 0.5719, 0.6041, 0.1422, 0.8980, 0.5429]
        y = [0.7599, 0.6490, 0.3592, 0.4001, 0.2199, 0.8681]

        # SMOTE
        # Mild
        x = [0.8310, 0.8494, 0.6620, 0.6570, 0.1970, 0.8692]
        y = [ 0.5287, 0.5518, 0.2988, 0.2990, 0.2673, 0.6211]


        # Under 6000
        # Mild
        x = [0.8335, 0.8252, 0.5619, 0.5274, 0.1907, 0.8647]
        y = [0.6280, 0.6079, 0.3174, 0.3559, 0.2697, 0.6921]

        # Severe
        x = [0.6675, 0.6474, 0.2027, 0.1901, 0.9042, 0.6538]
        y = [0.5518, 0.5103, 0.1391, 0.1689, 0.2195, 0.7404]


        color = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
        markers = np.repeat(["o", "s", "D", ">", "P", "p"], N / 6)
        label = ["BDT-6", "BDT-11", "KNN-5", "KNN-10", "GaussianBayes", "RF"]

        fig, ax = plt.subplots()
        ax.legend()

        scatter = mscatter(x, y, c=color, m=markers, ax=ax)
        plt.xlabel("Recall")
        plt.ylabel("Precision")


        class MarkerHandler(HandlerBase):
            def create_artists(self, legend, tup, xdescent, ydescent,
                               width, height, fontsize, trans):
                return [plt.Line2D([width / 2], [height / 2.], ls="",
                                   marker=tup[1], color=tup[0], transform=trans)]


        ax.legend(list(zip(color, markers)), label,bbox_to_anchor=(1.05, 1.0), loc='upper left',
                  handler_map={tuple: MarkerHandler()})
        plt.tight_layout()
        plt.grid()
        plt.show()
