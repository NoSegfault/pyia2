import pyia2

def event_cb(event):
	print(event)


event_id = pyia2.IA2_EVENT_DOCUMENT_LOAD_COMPLETE
pyia2.Registry.registerEventListener(event_cb, event_id )

event_id = pyia2.EVENT_OBJECT_FOCUS
pyia2.Registry.registerEventListener(event_cb, event_id )

pyia2.Registry.start()