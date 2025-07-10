from datetime import datetime
import sys

dates = [datetime.strptime(line.rstrip(), "%d.%m.%Y").date() for line in sys.stdin]
if dates:
    delta = (max(dates) - min(dates)).days
    print(delta)