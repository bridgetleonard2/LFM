#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 21:28:56 2022

@author: bridget
"""

import actr

actr.load_act_r_model("ACT-R:tutorial;project;read-model.lisp")

# Create variables to hold model's response times, the time of that response,
# the possible stimuli, and the data from the behavioral task

response = False
response_time = False

pairs = list(zip(['adventure', 'bagel', 'candle', 'direction', 'home',
                  'octopus', 'potato', 'stack', 'wreck'],
                 ['trip', 'butter', 'wick', 'arrow', 'sick', 'ocean',
                  'mash', 'build', 'ship']))

# behavioral_data_here =


# respond_to_key_press is set to monitor the output-key command
# and records the time and key that was pressed by the model.
 

def respond_to_space_press (model,key):
    global response_time
    
    response_time = actr.get_time()

def respond_to_key_press (model,key):
    global response

    response = key
    
    
# study function runs a simple singular trial in which a cue and target are presented on the
# screen for the model to encode

def study(cue, target):
    
    window = actr.open_exp_window("Retrieval Experiment", visible=False)

    actr.install_device(window)

    actr.add_text_to_exp_window(window, cue)
    actr.add_text_to_exp_window(window, target)
    
    actr.run(10)

# test function runs a simple singular trial in which a cue, target, and result (whether cue and target pair
# if T or F) is entered

def test(cue, target):

    window = actr.open_exp_window("Retrieval Experiment", visible=False)

    actr.install_device(window)

    actr.add_command("cue-response", respond_to_space_press, "Retrieval experiment model response to cue")
    actr.monitor_command("output-key","cue-response")

    actr.add_text_to_exp_window(window, cue)

    global response_time

    response_time = 0
    start = actr.get_time()

    # cue is presented -- retrieval of target begins, once some chunnk retrieved -- press key ?

    actr.run(30)
    
    actr.remove_command_monitor("output-key", "cue-response")
    actr.remove_command("cue-response")

    actr.clear_exp_window(window)
    
    actr.add_command("feedback-response", respond_to_key_press, "Retrieval experiment model response to feedback")
    actr.monitor_command("output-key","feedback-response")

    actr.add_text_to_exp_window(window, target)

    global response

    response = ''

    actr.run(30)
    
    actr.remove_command_monitor("output-key", "feedback-response")
    actr.remove_command("feedback-response")
    
    rt = response_time - start
    
    if response == 'f':
        return (cue, True, rt / 1000)
    elif response == 'j':
        return (cue, False, rt / 1000)

    # feedback provided in form of correct target -- if match response: press f, if no match press j
    
# make a function that runs an experiment given two parameters.
# the first indicates the number of pairs to use. the second
# indicates the number of trials to run.



def study_phase():
     
     result = []
            
     for cue,target in [('adventure', 'trip'),
                        ('bagel', 'butter'), 
                        ('candle', 'wick'), 
                        ('direction', 'arrow'),
                        ('home','sick'), 
                        ('octopus', 'ocean'),  
                        ('potato', 'mash'),
                        ('stack', 'build'),
                        ('wreck', 'ship')]:
             
             result.append(study(cue,target))
         
     return result 
 
    
def test_phase():
     
     result = []
            
     for cue,target in [('adventure', 'trip'),
                        ('bagel', 'butter'), 
                        ('candle', 'wick'), 
                        ('direction', 'arrow'),
                        ('home','sick'), 
                        ('octopus', 'ocean'),  
                        ('potato', 'mash'),
                        ('stack', 'build'),
                        ('wreck', 'ship')]:
             
             result.append(test(cue,target))
         
     return result 