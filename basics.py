import os, pickle

class rock_info(object):
        """this class contains:
                - basic rock information
                - method to load and updated rock info
                """ 
        
        def __init__(self, labutils_path = './', rock_dict_file = 'rock_dict.pkl'):
                super(rock_info, self).__init__()
                # load pickle file
                filepath = os.path.join(labutils_path, '_helpers', rock_dict_file)
                with open(filepath, 'rb') as f:
                        self.rock_dict = pickle.load(f)
                return

        def add_sample_to_dict(self, tag, classification = '', 
        family = '', genus = '', long_name = '', origin = '', provenance = 'outcrop'):
                self.rock_dict[tag] = {
                        'class':classification,
                        'family':family, 
                        'genus':genus, 
                        'long_name':long_name,
                        'origin'  :origin, 
                        'provenance':provenance,  
                        'code':tag
                        }
                return

        def update_sample_file(self, filename = 'rock_dict', filepath = './'):
                filepath = os.path.join(filepath,filename+'.pkl')
                with open(filepath,'wb') as f:
                        pickle.dump(rock_dict, f, protocol=pickle.HIGHEST_PROTOCOL)
                return