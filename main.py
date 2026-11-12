import os
import shutil
os.makedirs("/output", exist_ok=True)
shutil.copyfile(os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png"), "/output/entry.png")
