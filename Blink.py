from TOSSIM import*
import sys
t=Tossim([]);
t.addChannel("BlinkC",sys.stdout)
t.getNode(1).bootAtTime(10000);
for i in range (0,100):
 t.runNextEvent()
