import os
import subprocess
import numpy as np

# Function to run Madgraph
def run_mg5_file(proc_file_path, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL):
    """
    Function to run Madgraph

    Description:
    ------------
    This function runs Madgraph with the proc_file_path as argument

    Parameters:
    ----------
        proc_file_path: path to the proc file
        stdout (optional): standard output (default: subprocess.DEVNULL)
        stderr (optional): standard error (default: subprocess.DEVNULL)

    return:
    -------
    True if Madgraph is installed, False otherwise
    """

    MG5_Path = os.path.join(os.sep, 'Collider', 'MG5_aMC_v3_1_0', 'bin', 'mg5_aMC')
    MG5_Path = os.path.relpath(MG5_Path, os.getcwd())
    try :    
        subprocess.run([MG5_Path, proc_file_path], stdout=stdout, stderr=stderr,check=True)
        return True
    except :
        print("Madgraph is not installed in {}".format(MG5_Path))
        return False
    


# function to generate different random seeds
def semilla(seeds, max_seed = 10000):
    """
    Function to generate different random seeds

    Description:
    ------------
    This function generates a random seed that is not in the list of seeds that 
    are passed as an argument.

    Parameters:
    ----------
        seeds: list of seeds
        max_seed: maximum seed value

        
    return: 
    -------
    new seed
    """
    if len (seeds) == max_seed:
        raise Exception("No more seeds available")
    while True:
        seed = np.random.randint(1, max_seed+1)
        if not(seed in seeds): break
    seeds.append(seed)
    return seeds[-1]

def get_seed_from_banner(banner_file_path: str) -> int:
    """
    Function to get the seed from the banner file

    Description:
    ------------
    This function gets the seed from the banner file
    example of line in the banner file:
      4160 = iseed ! rnd seed (0=assigned automatically=default))
    which must be returned as 4160

    Parameters:
    ----------
        banner_file_path: path to the banner file

    return: 
    -------
    seed
    """
    with open(banner_file_path, "r") as f:
        seed_line = [line for line in f.readlines() if "iseed" in line][0]
    seed = int(seed_line.split("=")[0].strip())
    return seed

from pathlib import Path

def get_seeds_from_mg5_output_folder(mg5_output_folder: str) -> list:
    """
    Function to get the seeds from the mg5 output folder

    Description:
    ------------
    This function gets the seeds from the mg5 output folder,
    all the banner files are in Events subfolder, and have the subfix *banner.txt
    We use glob to get all the banner files and then we get the seed from each 
    banner file.

    Parameters:
    ----------
        mg5_output_folder: path to the mg5 output folder

    return: 
    -------
    list of seeds
    """
    banner_files = list(Path(mg5_output_folder).glob("Events/run_*/*banner.txt"))
    return [get_seed_from_banner(banner_file_path) for banner_file_path in banner_files]