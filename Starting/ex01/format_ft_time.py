import time
from datetime import date


timestamp = time.time()
today = date.today()

print("Seconds since January 1, 1970:" ,f"{timestamp:,.4f}","or", f"{timestamp:.4e}", "in scientific notation")
print(today.strftime("%b %d %Y"))


