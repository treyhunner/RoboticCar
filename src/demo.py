from Landscape import Landscape
from Simulator import Simulator


world = Landscape(
    terrain=[
        [200, 200, 400, 400],
        [400, 400, 600, 600],
        [600, 100, 800, 400]])
demo = Simulator(world)
demo.interactive()
