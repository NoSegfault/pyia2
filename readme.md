# Python Interface to MSAA+IAccessible2

This project builds on top of the work of Eitan Isaacson [pyia](https://github.com/eeejay/pyia) project to build a python library to Microsoft Active Accessibility (MSAA) and IAccessible2 interfaces for Windows Operating system.
This project extends the pyia project to support the IAccessible2 interfaces. 
The purpose of the project is to support ARIA and HTML implementation testing as part of the activities of the W3C WAI ARIA working group.

## Installation Requirements

* Install python 2.7.x
* Insall comtypes library
  
  pip install comtypes
  
* Clone this repository

## References
* [pyia project](https://github.com/eeejay/pyia)
* [W3C Accessible Technology Test Adapter (ATTA) API Specification](https://spec-ops.github.io/atta-api/)
* [Spec-Ops: ATTA tools](https://github.com/Spec-Ops/web-platform-tests/tree/atk-atspi-atta/wai-aria/tools)
* [Microsoft Active Accessibility: Architecture](https://msdn.microsoft.com/en-us/library/ms971310.aspx?f=255&MSPPError=-2147217396)
* [The Linux Foundation: IAccessible2](https://wiki.linuxfoundation.org/accessibility/iaccessible2/start)
* [IAccessible2 COM proxy stub DLL](https://wiki.linuxfoundation.org/accessibility/iaccessible2/comproxydll)
