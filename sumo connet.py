import traci

sumoCmd = ["sumo", "-c", "your_sumo_config_file.sumocfg"]
traci.start(sumoCmd)


traci.close()
