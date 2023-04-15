from pyamaze import maze,agent
m=maze(20,20)
m.CreateMaze(loopPercent=0)
a=agent(m,filled=True,footprints=True)
m.tracePath({a:m.path})
m.run()