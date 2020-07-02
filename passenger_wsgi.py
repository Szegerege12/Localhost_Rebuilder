import sys, os
sys.path.append(os.getcwd())
os.environ['enviroment'] = "development"
from app import app as application