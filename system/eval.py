# software design
# use the APPROVE_DESIGN_PROMPT to approve the design
# DevBench has a pretty complicated process for this - need to understand how it works

# environment setup
# execute the repository's example code in each `examples` directory

# implementation
# execute the reference repository's acceptance and unit tests on the generated codebase

# acceptance tests
# execute the generated acceptance tests on the reference repository

# unit tests
# execute the generated unit tests on the reference repository
# compute the coverage of the generated unit tests has on the reference repository


# for each directory in "system/output/v2"
# cd into the directory
# create a new conda environment (or virtualenv if easier?) from the requirements.txt
# execute the repository's example code in each `examples` directory
# 
import os

for directory in os.listdir("system/output/v2"):
    if os.path.isdir(directory):
        os.chdir(directory)
        os.system("conda create --name test_env --file requirements.txt")
        os.system("conda activate test_env")
        os.system("python examples/demo.py")
        os.system("pytest tests/unit/test_module.py")
        os.system("pytest tests/acceptance/test_features.py")
        os.system("coverage run -m pytest tests/unit/test_module.py")
        os.system("coverage report")
        os.system("conda deactivate")
        os.chdir("..")