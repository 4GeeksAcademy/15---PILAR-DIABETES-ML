from dotenv import load_dotenv  # hh
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import db_connect

engine = db_connect()
load_dotenv()
print = print(os.getenv("Diabetes-ML-DB-URI"))
