import math 
from tensorflow.keras.initializers import lecun_uniform
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GRU, Dense

class BuildModel:
    def __init__(self, model_name, num_epochs, batch_size):
        self.model_name = model_name 
        self.num_epochs = num_epochs
        self.batch_size = batch_size
    
    def build(self):
        if self.model_name == 'theilsen':
            print('theilsen')
        
        if self.model_name == 'huber':
            print('huber')
        
        if self.model_name == 'lstm':
            print('lstm')
        
        if self.model == 'gru':
            print('gru')


    
