from datetime import datetime
from threading import Timer
from getMETAR import *

x = datetime.today()
y = x.replace(day=x.day+1, hour=4, minuote=0, second=0, microsecond=0)
delta_t = y-x

secs = delta_t.seconds+1

t = Timer(secs, archiveMETARs)
t.start()
