import pickle
import warnings
import numpy as np
from FeaturesExtractor import FeaturesExtractor

warnings.filterwarnings("ignore")

GMM_female_model_path = 'model/females.gmm'
GMM_male_model_path = 'model/males.gmm'
HMM_female_model_path = 'model/females.hmm'
HMM_male_model_path = 'model/males.hmm'


class GenderIdentifier:

    def __init__(self, file_path, model):
        self.audio2test         = file_path
        self.features_extractor = FeaturesExtractor()
        self.model2use          = model

        if self.model2use == 'GMM':
            self.females_gmm = pickle.load(open(GMM_female_model_path, 'rb'))
            self.males_gmm   = pickle.load(open(GMM_male_model_path, 'rb'))
        elif self.model2use == 'HMM':
            self.females_gmm = pickle.load(open(HMM_female_model_path, 'rb'))
            self.males_gmm   = pickle.load(open(HMM_male_model_path, 'rb'))

    def process(self):
        file = self.audio2test
        vector = self.features_extractor.extract_features(file)
        winner = self.identify_gender(vector)
        return self.model2use, winner

    def identify_gender(self, vector):
        is_female_scores         = np.array(self.females_gmm.score(vector))
        is_female_log_likelihood = is_female_scores.sum()
        is_male_scores         = np.array(self.males_gmm.score(vector))
        is_male_log_likelihood = is_male_scores.sum()
        if is_male_log_likelihood > is_female_log_likelihood: winner = "male"
        else                                                : winner = "female"
        return winner


if __name__== "__main__":
    gender_identifier = GenderIdentifier("1.wav", "HMM")
    gender_identifier.process()
