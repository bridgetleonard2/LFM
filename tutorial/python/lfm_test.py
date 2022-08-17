import actr

actr.load_act_r_model("ACT-R:tutorial;project;test-model.lisp")

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

def respond_to_key_press (model,key):
    global response,response_time

    response_time = actr.get_time()
    response = key

# sentence function runs a simple singular trial in which a cue, target, and result (whether cue and target pair
# if T or F) is entered

def sentence(cue, target, result):

    actr.reset()

    window = actr.open_exp_window("Retrieval Experiment", visible=False)

    actr.install_device(window)

    actr.add_command("pair-response", respond_to_key_press, "Retrieval experiment model response")
    actr.monitor_command("output-key","pair-response")

    actr.add_text_to_exp_window(window, cue)

    global response_time

    response_time = 0

    # cue is presented -- retrieval of target begins, once some chunnk retrieved -- press key ?

    actr.run(30)

    actr.clear_exp_window(window)

    actr.add_text_to_exp_window(window, target)

    global response

    response = ''

    actr.run(30)

    return response,response_time


    # feedback provided in form of correct target -- if match response: press _, if no match press _
