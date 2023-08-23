import time

from snowpiercer.simulation import PopulationPlotter
from snowpiercer.simulation import Simulation
from snowpiercer.world import World

# main script
if __name__ == '__main__':
    simulation: Simulation = Simulation(number_of_timesteps=200, world=World.create_appletree_world_with_few_lumberjacks())
    simulation.run()
    PopulationPlotter().plot(simulation.get_data_log())
    time.sleep(5)
    PopulationPlotter().plot_wood_resources(simulation.get_data_log())
