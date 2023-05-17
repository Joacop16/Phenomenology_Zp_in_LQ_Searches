import os
import subprocess
import numpy as np

# Function to run Madgraph
def run_mg5_file(proc_file_path, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL):
    MG5_Path = os.path.join(os.sep, 'Collider', 'MG5_aMC_v3_1_0', 'bin', 'mg5_aMC')
    MG5_Path = os.path.relpath(MG5_Path, os.getcwd())
    try :    
        subprocess.run([MG5_Path, proc_file_path], stdout=stdout, stderr=stderr,check=True)
        return True
    except :
        print("Madgraph is not installed in {}".format(MG5_Path))
        return False
    


# function to generate different random seeds
def semilla(seeds, max_seed = 5000):
    seed = np.random.randint(1, max_seed)
    if len (seeds) == max_seed:
        raise Exception("No more seeds available")
    while seed in seeds:
        seed = np.random.randint(1, max_seed)
    seeds.append(seed)
    return seeds[-1]