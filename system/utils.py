import subprocess
import sys
import os
import shutil
import copy
from typing import Dict, List, Union

def check_and_install_packages(packages: List[str]) -> Dict[str, Dict[str, Union[bool, str]]]:
    """Check if packages are installed and install if needed"""
    results = {}
    
    for package in packages:
        if not package:  # Check for empty package names
            continue
            
        base_package = package.split('.')[0]  # Get root package name
        
        if not base_package:
            results[package] = {
                'installed': False,
                'message': 'Invalid package name'
            }
            continue
            
        try:
            module = __import__(base_package)
            results[package] = {
                'installed': True,
                'message': 'Already installed'
            }
        except ImportError:
            try:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
                results[package] = {
                    'installed': True,
                    'message': 'Successfully installed'
                }
            except subprocess.CalledProcessError:
                results[package] = {
                    'installed': False,
                    'message': 'Installation failed'
                }
    
    return results

def write_files(base_path: str, files_content: Dict[str, str]) -> None:
    """Write files based on dictionary input"""
    for file_path, content in files_content.items():
        # Strip leading slash to ensure relative path
        clean_path = file_path.lstrip('/')
        full_path = os.path.join(base_path, clean_path)
        
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        
        # Write file content
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)

def create_repository(base_path: str, documents: Dict) -> None:
    """Create repository structure and write files including test files"""
    # Create base directory if it doesn't exist
    os.makedirs(base_path, exist_ok=True)

    # If base_path exists, delete all its contents
    for filename in os.listdir(base_path):
        file_path = os.path.join(base_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')

    files = copy.deepcopy(documents['code'])

    # Get first directory name, handling paths with leading slash
    root_dir = next(name for name in next(iter(files)).split('/') if name)
    
    coverage = "[run]\nomit =\n    */__init__.py\n    tests/*\n"
    
    files.update({
        f'{root_dir}/tests/unit/test_module.py': documents['unit_tests']['test_module'],
        f'{root_dir}/tests/unit/__init__.py': '',
        f'{root_dir}/tests/acceptance/test_features.py': documents['acceptance_tests']['test_features'],
        f'{root_dir}/tests/acceptance/__init__.py': '',
        f'{root_dir}/docs/PRD.md': documents['PRD'],
        f'{root_dir}/docs/UML_class.md': documents['UML_class'],
        f'{root_dir}/docs/UML_sequence.md': documents['UML_sequence'],
        f'{root_dir}/docs/architecture_design.md': documents['architecture_design'],
        f'{root_dir}/requirements.txt': documents['requirements'],
        f'{root_dir}/.coveragerc': coverage,
    })
    
    # Write files  
    write_files(base_path, files)




# Example usage
if __name__ == "__main__":
    packages = ["numpy", "xml.etree.ElementTree", "nonexistent_package"]
    status = check_and_install_packages(packages)
    for pkg, result in status.items():
        print(f"{pkg}: {result['message']}")

    # Example usage
        structure = """geotext/
            __init__.py
            geotext.py
            data_file/
                citypatches.txt
                countryInfo.txt
                nationalities.txt
                cities15000.txt
            examples/
                demo.py
            tests/
                test_geotext.py
            utils/
                data_loader.py
                text_processor.py"""
                
        files_content = {
            "geotext/__init__.py": "# Initialize package",
            "geotext/geotext.py": "# Main implementation",
            "geotext/examples/demo.py": "# Demo code"
            # Add more files as needed
        }
    
    create_repository("architecture_design", structure, files_content, "# Unit test content", "# Acceptance test content")
