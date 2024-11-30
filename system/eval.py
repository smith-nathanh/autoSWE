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

# import os

# for directory in os.listdir("system/output/v2"):
#     if os.path.isdir(directory):
#         os.chdir(directory)
#         os.system("conda create --name test_env --file requirements.txt")
#         os.system("conda activate test_env")
#         os.system("python examples/demo.py")
#         os.system("pytest tests/unit/test_module.py")
#         os.system("pytest tests/acceptance/test_features.py")
#         os.system("coverage run -m pytest tests/unit/test_module.py")
#         os.system("coverage report")
#         os.system("conda deactivate")
#         os.chdir("..")

# for each of the directories in "system/output/v3"
# cd into the directory
# use subprocess to execute the following commands and capture the stderr and stdout together and write to a json file for each directory
# Tasks that need their own key in the json file:
# environment_setup
    # build conda environment from requirements.txt
    # activate the conda environment
    # execute the repository's example code in each `examples` directory
# acceptance_tests
    # execute the repository's acceptance test by running `python -m unittest tests/acceptance/test_features.py`
# unit_tests
    # execute the repository's unit test by running `coverage run -m unittest tests/unit/test_module.py`
    # compute the coverage of the generated unit tests has on the reference repository by running `coverage report`
# remember to deactivate the conda environment after all the tasks are done
# write the json file to the f'system/output/v3/{directory}' directory, e.g., "system/output/v3/geotext/geotext_eval.json"

import os
import subprocess
import json
import argparse
import yaml

def run_command(command, env=None):
    result = subprocess.run(command, shell=True, capture_output=True, text=True, env=env)
    return {
        "stdout": result.stdout,
        "stderr": result.stderr,
        "returncode": result.returncode
    }

def is_installed(package_name):
    """Check if package can be imported in the conda environment."""
    check_script = f"""
import sys
try:
    __import__('{package_name}')
    print('Package successfully imported')
    sys.exit(0)
except ImportError as e:
    print(f'Import Error: {{e}}', file=sys.stderr)
    sys.exit(1)
"""
    with open('_check_import.py', 'w') as f:
        f.write(check_script)
    
    try:
        result = run_command(f"conda run -n myenv python _check_import.py")
        success = result["returncode"] == 0 and "successfully imported" in result["stdout"]
    except Exception as e:
        print(f"Error checking package {package_name}: {str(e)}")
        success = False
    finally:
        if os.path.exists('_check_import.py'):
            os.remove('_check_import.py')  # Cleanup
    
    print(f"Package {package_name} check results:")
    print(f"Return code: {result['returncode']}")
    print(f"Stdout: {result['stdout']}")
    print(f"Stderr: {result['stderr']}")
    print(f"Is installed: {success}")
    
    return success

def filter_requirements(requirements_file):
    """Filter requirements to only those that cannot be imported."""
    if not os.path.exists(requirements_file):
        return []
        
    filtered_packages = []
    with open(requirements_file, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            
            package_name = line.split('==')[0].split('>=')[0].split('<=')[0].strip()
            root_package = package_name.split('.')[0]
            
            if not is_installed(root_package):
                filtered_packages.append(root_package)
    
    return filtered_packages

def extract_python_command_from_shell_script(script_path):
    """Read shell script and extract Python commands with their arguments.
    Returns a list of commands."""
    if not os.path.exists(script_path):
        return []
        
    try:
        with open(script_path, 'r') as f:
            content = f.read()
            
        # Split into lines and remove comments
        lines = [line.split('#')[0].strip() for line in content.splitlines()]
        
        commands = []
        current_command = []
        in_command = False
        
        for line in lines:
            if not line:
                continue
                
            if line.startswith('python') or line.startswith('python3'):
                # If we were already in a command, save it first
                if in_command and current_command:
                    commands.append(' '.join(' '.join(current_command).split()))
                
                in_command = True
                current_command = [line.rstrip('\\').strip()]
            elif in_command and line.rstrip('\\').strip():
                current_command.append(line.rstrip('\\').strip())
            elif in_command and not line.rstrip('\\').strip():
                commands.append(' '.join(' '.join(current_command).split()))
                in_command = False
                current_command = []
        
        # Add final command if exists
        if in_command and current_command:
            commands.append(' '.join(' '.join(current_command).split()))
            
        return commands
        
    except Exception as e:
        print(f"Error reading script {script_path}: {str(e)}")
        return []

def process_directory(directory):
    result = {
        "environment_setup": {},
        "acceptance_tests": {},
        "unit_tests": {}
    }

    # Change to the directory
    original_dir = os.getcwd()
    os.chdir(directory)
    print('Changed to:', os.getcwd())

    # Environment setup
    result["environment_setup"]["create_conda_env"] = run_command("conda create -n myenv python=3.8 -y")
    result["environment_setup"]["activate_conda_env"] = run_command("conda activate myenv")

    # Filter requirements to exclude already installed packages
    filtered_packages = filter_requirements("requirements.txt")
    print(f"Filtered packages: {filtered_packages}")
    if filtered_packages:
        with open("filtered_requirements.txt", "w") as f:
            f.write("\n".join(filtered_packages))
        result["environment_setup"]["pip_install"] = run_command("conda run -n myenv pip install -r filtered_requirements.txt")
    else:
        result["environment_setup"]["pip_install"] = {"stdout": "No additional packages to install", "stderr": "", "returncode": 0}

    # Execute example code
    examples_dir = "examples"
    if os.path.exists(examples_dir):
        for example in os.listdir(examples_dir):
            example_path = os.path.join(examples_dir, example)
            if os.path.isfile(example_path) and example_path.endswith(".sh"):
                python_cmds = extract_python_command_from_shell_script(example_path)
                print(f"Python commands for {example}: {python_cmds}")
                result["environment_setup"][example] = []
                for i, python_cmd in enumerate(python_cmds):
                    if python_cmd:
                        cmd = f"conda run -n myenv {python_cmd}"
                        result["environment_setup"][example].append({
                            "command": python_cmd,
                            "result": run_command(cmd)
                        })

    # Acceptance tests
    result["acceptance_tests"] = run_command("conda run -n myenv python -m unittest tests/acceptance/test_features.py")

    # Unit tests
    result["unit_tests"]["run_tests"] = run_command("conda run -n myenv coverage run -m unittest tests/unit/test_module.py")
    result["unit_tests"]["coverage_report"] = run_command("conda run -n myenv coverage report")

    # Deactivate conda environment
    result["environment_setup"]["activate_conda_env"] = run_command("conda deactivate")

    # Write the result to a JSON file
    output_file = f"{os.path.basename(directory)}_eval.json"
    with open(output_file, "w") as f:
        json.dump(result, f, indent=4)

    # Change back to the original directory
    os.chdir(original_dir)
    print('Finished processing. Returned to:', os.getcwd())

def main():
    parser = argparse.ArgumentParser(description="Process directories and run tests.")
    parser.add_argument("--working_directory", required=True, help="The base directory containing subdirectories to process.")
    parser.add_argument("--config", required=True, help="The YAML configuration file.")
    parser.add_argument("--config_key", required=True, help="The key in the YAML file to read directory names from.")
    args = parser.parse_args()

    base_dir = args.working_directory
    config_file = args.config
    config_key = args.config_key

    # Load the YAML configuration file
    with open(config_file, "r") as f:
        config = yaml.safe_load(f)

    # Get the list of directories from the specified key
    directories = config.get(config_key, {})

    for directory in directories.keys():
        dir_path = os.path.join(base_dir, directory)
        if os.path.isdir(dir_path):
            print('Processing directory:', dir_path)
            process_directory(dir_path)
            run_command("conda env remove -n myenv -y")

if __name__ == "__main__":
    # example usage: python eval.py --working_directory outputs/v3 --config eval_config.yml --config_key prd_paths
    main()