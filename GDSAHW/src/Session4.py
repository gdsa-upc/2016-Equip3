import os
import sys
# Add the root path (the path above this one) to the pythonpath.
sys.path.insert(0,'../')
from utils.params import get_params
from  import build_database

ruta1=os.path.dirname(os.path.abspath(__file__))+'\\TerrassaBuildings900\\val\\images'
ruta2=os.path.dirname(os.path.abspath(__file__))+'\\TerrassaBuildings900\\train\\images'
savepath1=os.path.dirname(os.path.abspath(__file__))+'\\TerrassaBuildings900\\val'
savepath2=os.path.dirname(os.path.abspath(__file__))+'\\TerrassaBuildings900\\train'

build_database(ruta1,savepath1);
build_database(ruta2,savepath2);