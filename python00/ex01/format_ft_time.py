import time
import datetime

seconds_from_epoch = time.time()

print(f"Seconds since January 1, 1970: {seconds_from_epoch:,.4f} or {seconds_from_epoch:,.2e} in scientific notation")
print(datetime.datetime.now().strftime('%b %d %Y'))