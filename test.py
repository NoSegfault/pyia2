import pyia
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

desktop = pyia.getDesktop()
print str(desktop)

for window in desktop:
  if not window.accState(0) & pyia.STATE_SYSTEM_INVISIBLE:
     print repr(str(window))

# Need to get ia2.tlb
# create a module comptypes.client.GetModule(path to ia2.tlb)
