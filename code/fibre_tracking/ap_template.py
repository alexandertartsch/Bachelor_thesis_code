<<<<<<< HEAD
from signal_artifacts import ActionPotential
import numpy as np
from math import ceil
import matplotlib.pyplot as plt
=======
from typing import Union
from neo.core.analogsignal import AnalogSignal
from math import ceil
from typing import Iterable

>>>>>>> d9b68deaf6d8dd9f8ef1487207df0f1f5f80bb73

## Encapsulates creating and maintaining templates for action potentials, e.g., for correlation analysis to assign an AP to a fibre.
class ActionPotentialTemplate:

<<<<<<< HEAD
	## Signal values for this template.
	signal_template = None
	## The length of the signal template.
	length = None

	## Constructor for a template, given the raw values.
	# @param signal_template Signal values for this template.
	def __init__(self, signal_template):
		self.signal_template = signal_template
		self.length = len(signal_template)
		
	## Create a template from a list of action potentials as the "average" action potential from the list.
	# The APs are aligned by their maximum signal values.
	# TODO: make this alignment optional.
	# TODO: make plotting optional
	# @param aps List of action potentials from which the template should be created
	def from_ap_list(aps):
		
		num_aps = len(aps)
		
		plt.figure()
		
		for ap in aps:
			plt.plot(range(0, len(ap.raw_signal)), ap.raw_signal)
			
		plt.show()
		
		avg_len = ceil(np.sum([len(ap.raw_signal) for ap in aps]) / num_aps)
		avg_argmax = ceil(np.sum([np.argmax(ap.raw_signal) for ap in aps]) / num_aps)
		
		print("avg. len: " + str(avg_len) + " avg argmax: " + str(avg_argmax))
		
		template = np.zeros(avg_len)
		
		for ap in aps:
			signal = ap.raw_signal
			# how do we need to shift the signal (<0 left, >0 right)
			shift = (avg_argmax - np.argmax(signal))
			
			start_idx = max(0, shift)
			end_idx = min(len(template), len(signal) + shift) - 1
			
			# print("shift: " + str(shift))
			# print("start: " + str(start_idx) + " end: " + str(end_idx))
			
			if shift >= 0:
				template[start_idx : end_idx] += signal[0 : min(len(signal), len(template) - shift) - 1]
			else:
				# print(abs(shift))
				# print(len(signal))
				# print(len(template))
				template[start_idx : end_idx] += signal[abs(shift) : min(len(signal), len(template) - shift) - 1]
				
		template = (1 / num_aps) * template
		
		plt.figure()
		
		plt.plot(template)
			
		plt.show()
		
		return ActionPotentialTemplate(signal_template = template)
=======
    ## Signal values for this template.
    _signal_template: AnalogSignal = None

    ## Constructor for a template, given the raw values.
    # @param signal_template Signal values for this template.
    def __init__(self, signal_template: AnalogSignal):
        self._signal_template = signal_template
        
    def __len__(self):
        return len(self._signal_template)

    @property
    def duration(self):
        return (self._signal_template.t_stop - self._signal_template.t_start)

    @property
    def signal_template(self):
        return self._signal_template

    ## Create a template from a list of action potentials as the "average" action potential from the list.
    # The APs are aligned by their maximum signal values.
    # TODO: make this alignment optional.
    # TODO: make plotting optional
    # @param aps List of action potentials from which the template should be created
    @staticmethod
    def from_ap_list(aps: Iterable):
        # TODO re-implement
        pass

        # num_aps = len(aps)
        
        # plt.figure()
        
        # for ap in aps:
        #     plt.plot(range(0, len(ap.raw_signal)), ap.raw_signal)
            
        # plt.show()
        
        # avg_len = ceil(np.sum([len(ap.raw_signal) for ap in aps]) / num_aps)
        # avg_argmax = ceil(np.sum([np.argmax(ap.raw_signal) for ap in aps]) / num_aps)
        
        # print("avg. len: " + str(avg_len) + " avg argmax: " + str(avg_argmax))
        
        # template = np.zeros(avg_len)
        
        # for ap in aps:
        #     signal = ap.raw_signal
        #     # how do we need to shift the signal (<0 left, >0 right)
        #     shift = (avg_argmax - np.argmax(signal))
            
        #     start_idx = max(0, shift)
        #     end_idx = min(len(template), len(signal) + shift) - 1
            
        #     # print("shift: " + str(shift))
        #     # print("start: " + str(start_idx) + " end: " + str(end_idx))
            
        #     if shift >= 0:
        #         template[start_idx : end_idx] += signal[0 : min(len(signal), len(template) - shift) - 1]
        #     else:
        #         # print(abs(shift))
        #         # print(len(signal))
        #         # print(len(template))
        #         template[start_idx : end_idx] += signal[abs(shift) : min(len(signal), len(template) - shift) - 1]
                
        # template = (1 / num_aps) * template

        # return ActionPotentialTemplate(signal_template = template)
>>>>>>> d9b68deaf6d8dd9f8ef1487207df0f1f5f80bb73
