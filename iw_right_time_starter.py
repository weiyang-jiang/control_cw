"""
CMU 48721 Fall 2019
Assignment 3 part 1: "The right time"
Note:
1: Never use "print" function, it will block the code,
    use "logger.info()" instead.
2: ob is a python list with the following items:
    0: hour (0-23)
    1: min (0-59)
    2: weekday (0-7, 0 is Monday)
    3: outdoor air temperature (C)
    4: outdoor air RH (%)
    5: diffuse dolar radiation (W/m2)
    6: direct solar radiation (W/m2)
    7: IW IAT setpoint (C)
    8: IW IAT (C)
    9: IW average PMV (-999 if no occupied)
    10: IW occupants first-come predicted time (updated at 0:05)
    11: IW occupants last-leave predicted time (updated at 0:05)
    12: IW calculated heating demand (kW)
    13-36: Hourly outdoor air temperature forecast (provided at 0:00,
        for all other time, the values are -999)
"""
import gym, eplus_env, logging

from plot_data import analysis_data
logger = logging.getLogger('Ctrl-Tester')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
logger.addHandler(ch)
logger.info('Running the simulation test...')
logger.info('Environment warm-up may take time.')
env = gym.make('IW-right-time-v3')  # !!! Change according to your group
ob, is_terminal, path_name = env.reset()
logger.info('Environment warm-up is done.')
total_steps = 8928
step_i = 0
last_perct = 0


while is_terminal == False:
    # !!DO NOT change the above lines
    # The following lines are the baseline control strategy
    #  You should implement your control strategy here
    weekday = ob[2]
    hour = ob[0]

    # For all the weekends
    if weekday >= 5:
        # Step down the setpoint
        act = 1
    # For all the weekdays
    else:
        # Before 7:00 AM or after 8:00 PM, step down the setpoint
        if hour < 7 or hour >= 20:
            act = 1
        # For other time, step up the setpoint
        else:
            act = 0
    # logger.info('This observation is: %s'%ob);
    ob, is_terminal, path_name = env.step([act])
    # Control strategy ends
    #######################################################
    # !!DO NOT change the following lines
    step_i += 1
    this_perct = (step_i / total_steps) * 100
    if this_perct // 10 != last_perct // 10:
        logger.info('%.1f%% simulation is done...' % (this_perct))
    last_perct = this_perct

env.end_env()
logger.info('Simulation completed!')

data = analysis_data(path_name)
data.plot_data()
logger.info("plotting completed!")
data.save_power()
logger.info("power sum completed!")