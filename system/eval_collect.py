import os
import json
import argparse
from typing import Dict, List
from pathlib import Path

def collect_stderr_messages(base_dir: str) -> Dict[str, List[str]]:
    stderr_collections = {
        'environment_setup': [],
        'acceptance_tests': [],
        'unit_tests': []
    }
    
    for eval_file in Path(base_dir).rglob('*_eval.json'):
        try:
            with open(eval_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            # Environment setup
            if 'environment_setup' in data:
                env = data['environment_setup']
                for key in ['create_conda_env', 'activate_conda_env', 'pip_install']:
                    if key in env and env[key].get('stderr'):
                        stderr_collections['environment_setup'].append(
                            f"[{eval_file.parent.name}] {key}: {env[key]['stderr']}"
                        )
                
                # Example usage errors
                if 'example_usage.sh' in env:
                    for cmd in env['example_usage.sh']:
                        if 'result' in cmd and cmd['result'].get('stderr'):
                            stderr_collections['environment_setup'].append(
                                f"[{eval_file.parent.name}] example_usage: {cmd['result']['stderr']}"
                            )

            # Acceptance tests
            if 'acceptance_tests' in data and data['acceptance_tests'].get('stderr'):
                stderr_collections['acceptance_tests'].append(
                    f"[{eval_file.parent.name}]: {data['acceptance_tests']['stderr']}"
                )

            # Unit tests
            if 'unit_tests' in data:
                unit = data['unit_tests']
                for key in ['run_tests', 'coverage_report']:
                    if key in unit and unit[key].get('stderr'):
                        stderr_collections['unit_tests'].append(
                            f"[{eval_file.parent.name}] {key}: {unit[key]['stderr']}"
                        )
                        
        except Exception as e:
            print(f"Error processing {eval_file}: {str(e)}")
            continue

    return stderr_collections

def main():
    parser = argparse.ArgumentParser(description='Collect stderr messages from _eval.json files')
    parser.add_argument('--base_dir', help='Base directory to search for _eval.json files')
    parser.add_argument('--output', '-o', help='Output file (optional)')
    args = parser.parse_args()

    results = collect_stderr_messages(args.base_dir)
    
    output = []
    for category, errors in results.items():
        if errors:
            output.append(f"\n{'='*20} {category.upper()} {'='*20}")
            for error in errors:
                output.append(f"\n{error}")
                output.append('-' * 80)

    output_text = '\n'.join(output)
    
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(output_text)
        print(f"Results written to {args.output}")
    else:
        print(output_text)

if __name__ == "__main__":
    main()