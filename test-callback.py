import pyia

def event_cb(event):
	print(event)


event_id = pyia.IA2_EVENT_DOCUMENT_LOAD_COMPLETE
pyia.Registry.registerEventListener(event_cb, event_id )

event_id = pyia.EVENT_OBJECT_FOCUS
pyia.Registry.registerEventListener(event_cb, event_id )

pyia.Registry.start()