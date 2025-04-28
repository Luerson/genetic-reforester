import numpy as np
import random
import copy
from .mutation import mutation

class mutation_A(mutation):

    def mut(self, curr_sol, forest_map, reforest_map):
        self._set_curr_sol_and_forest_map(curr_sol, forest_map, reforest_map)
        self._create_union_map()
        self._remove_reallocated_points()
        self._get_new_solution()
        
        return self.curr_sol

    def _set_curr_sol_and_forest_map(self, curr_sol, forest_map, reforest_map):
        self.curr_sol = np.array(curr_sol).astype(int)
        self.forest_map = np.array(forest_map).astype(int)
        self.reforest_map = np.array(reforest_map).astype(int)

    def _create_union_map(self):
        self.union_map = np.logical_or(self.curr_sol, self.forest_map)
        self.union_map = self.union_map.astype(int)

    def _get_valid_points(self, matrix):
        points = np.where(matrix == 1)
        points = list(zip(points[0], points[1]))

        return points
    
    def _get_weight_of_mask(self, mask):
        return np.sum(mask)
    
    def _get_probability_of_mask(self, mask):
        return  self._get_weight_of_mask(mask) / 24
    
    def _is_reforest_point_reallocated(self, mask) -> bool:
        reallocation_probability = random.random()
        return reallocation_probability > self._get_probability_of_mask(mask)
    
    def _get_extension_matrix(self, matrix):
        copy_matrix = copy.copy(matrix)
        return np.pad(copy_matrix, pad_width=2, mode='constant', constant_values=0)
    
    def _remove_reallocated_points(self):
        self.count = 0
        restorable_points = self._get_valid_points(self.curr_sol)
        extended_forest_map = self._get_extension_matrix(self.forest_map)

        for i, j in restorable_points:
            i_ext = i + 2
            j_ext = j + 2
            mask = extended_forest_map[i_ext-2:i_ext+3, j_ext-2:j_ext+3]

            if self._is_reforest_point_reallocated(mask):
                self.count += 1
                self.union_map[i][j] = 0
                self.curr_sol[i][j] = 0

        percentage = self.count / len(restorable_points)
        print(f'Porcentagem de realocação: {(percentage * 100):.2f}%')

    def _create_difference_map(self):
        return self.reforest_map * (self.curr_sol == 0)
    
    def _create_weights_matrix(self):
        return np.zeros_like(self.reforest_map)
    
    def _get_weights_of_reforest_points(self):
        weight_matrix = self._create_weights_matrix()

        reallocation_matrix = self._create_difference_map()
        reallocation_points = self._get_valid_points(reallocation_matrix)

        extended_union_map = self._get_extension_matrix(self.union_map)

        for i, j in reallocation_points:
            i_ext = i + 2
            j_ext = j + 2

            mask = extended_union_map[i_ext-2:i_ext+3, j_ext-2:j_ext+3]

            weight_matrix[i][j] = self._get_weight_of_mask(mask)

        return weight_matrix
    
    def _get_new_solution(self):
        weight_matrix = self._get_weights_of_reforest_points()
        weight_matrix = weight_matrix / weight_matrix.sum()

        weight_array = weight_matrix.flatten()

        random_index = np.random.choice(len(weight_array), size=self.count, p=weight_array)
        random_index = np.unravel_index(random_index, weight_matrix.shape)

        for num in range(self.count):
            i, j = random_index[0][num], random_index[1][num]
            self.curr_sol[i][j] = 1
            self.union_map[i][j] = 1
