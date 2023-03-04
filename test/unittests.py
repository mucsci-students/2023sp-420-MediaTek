import os
import sys
getPath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'mvc'))
sys.path.append(getPath)
from MVC.model import modelrefactor as mdl
from MVC.controller import controllerrefactor as ctrl

print(ctrl.controller.controllerGetLetters())