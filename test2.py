
from datetime import datetime, timedelta
from variables import appVars


chanel_id = 123
now = datetime.now()
dat = now.strftime("%Y%m%d")
#creacion id file
root = dat + '/' + str(chanel_id)
#appVars["file"] = root + '/img/'
loco = appVars["file"]
loco["id"] = root + '/img/'
loco["log"] = root + '/img/'
print(appVars)

