import os
import json
import argparse

def check_command_results(command_list):
    """Check if all commands in a list were successful"""
    for cmd in command_list:
        if isinstance(cmd, dict):
            result = cmd.get('result', {})
            if result.get('returncode', 0) != 0 or 'ERROR' in result.get('stderr', ''):
                return 0
    return 1

def check_stderr_for_errors(value):
    """Check a value for errors, handling different data types"""
    if isinstance(value, dict):
        return 0 if ('ERROR' in value.get('stderr', '') or 
                    value.get('returncode', 0) != 0) else 1
    elif isinstance(value, str):
        return 0 if 'ERROR' in value else 1
    elif isinstance(value, list):
        return check_command_results(value)
    return 1

def extract_coverage_percentage(coverage_output):
    """Extract total coverage percentage from coverage report output"""
    try:
        lines = coverage_output.split('\n')
        for line in lines:
            if line.strip().startswith('TOTAL'):
                # Extract the last number before the % sign
                return int(line.split()[-1].rstrip('%'))
    except:
        return 0
    return 0

def analyze_eval_file(file_path):
    """Analyze a single evaluation JSON file for errors"""
    results = {}
    
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    for key, value in data.items():
        if isinstance(value, dict):
            if key == 'environment_setup':
                results[key] = {}
                for subkey, subval in value.items():
                    results[key][subkey] = check_stderr_for_errors(subval)
            elif key == 'unit_tests':
                results[key] = {}
                # Handle run_tests success/failure
                results[key]['run_tests'] = check_stderr_for_errors(value.get('run_tests', {}))
                # Extract coverage percentage
                coverage_report = value.get('coverage_report', {})
                if check_stderr_for_errors(coverage_report):
                    results[key]['coverage'] = extract_coverage_percentage(coverage_report.get('stdout', ''))
                else:
                    results[key]['coverage'] = 0
            else:
                results[key] = check_stderr_for_errors(value)
        else:
            results[key] = check_stderr_for_errors(value)

    return results

def analyze_eval_files(base_path):
    """Iterate through directories and analyze all *_eval.json files"""
    all_results = {}
    
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith('_eval.json'):
                file_path = os.path.join(root, file)
                all_results[file] = analyze_eval_file(file_path)
    
    return all_results

def json_to_dataframe(results):
    """Convert evaluation results JSON to pandas DataFrame"""
    import pandas as pd
    
    # Initialize lists to store data
    data = []
    projects = []
    
    for project, metrics in results.items():
        # Remove _eval.json suffix for cleaner project names
        project_name = project.replace('_eval.json', '')
        projects.append(project_name)
        
        # Check if all environment setup steps passed
        env_setup = metrics.get('environment_setup', {})
        env_success = 1 if env_setup and all(v == 1 for v in env_setup.values()) else 0
        
        # Get acceptance tests result
        acceptance = metrics.get('acceptance_tests', 0)
        
        # Get unit tests metrics
        unit_tests = metrics.get('unit_tests', {})
        run_tests = unit_tests.get('run_tests', 0)
        coverage = unit_tests.get('coverage', 0)
        
        data.append({
            'environment_setup': env_success,
            'acceptance_tests': acceptance,
            'unit_tests_run_tests': run_tests,
            'unit_tests_coverage': coverage
        })
    
    # Create DataFrame
    df = pd.DataFrame(data, index=projects)
    return df

def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Analyze evaluation JSON files for errors in the given directory.'
    )
    parser.add_argument(
        '--base_path',
        type=str,
        default='outputs/v3',
        help='Base directory path containing *_eval.json files (default: outputs/v3)'
    )
    return parser.parse_args()

if __name__ == "__main__":
    # usage: python eval_report.py --base_path outputs/v3
    args = parse_arguments()
    results = analyze_eval_files(args.base_path)
    #print(json.dumps(results, indent=2))
    df = json_to_dataframe(results)
    print(df)
    df.to_csv(f'{args.base_path}/evaluation_results.csv')
