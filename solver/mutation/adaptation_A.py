from .mut_process_A import mut_process_A
import numpy as np

class adaptation_A(mut_process_A):

    def _get_weight_of_mask(self, mask):
        return np.sum(mask)