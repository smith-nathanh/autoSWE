import argparse
import os
import shutil

def relocate_directory(temp_dir: str, dest_dir: str, new_name: str) -> None:
    """Relocate and rename a directory"""
    if not os.path.isdir(temp_dir):
        raise FileNotFoundError(f"Source directory '{temp_dir}' does not exist.")
    
    new_path = os.path.join(dest_dir, new_name)
    
    # Create destination directory if it doesn't exist
    os.makedirs(new_path, exist_ok=True)
    
    # Move and rename the directory
    for directory in os.listdir(temp_dir):
        if os.path.isdir(os.path.join(temp_dir, directory)):
            for file in os.listdir(os.path.join(temp_dir, directory)):
                shutil.move(os.path.join(temp_dir, directory, file), os.path.join(new_path, file))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Relocate and rename a directory")
    parser.add_argument("--temp_dir", type=str, required=True, help="The temporary directory to relocate")
    parser.add_argument("--dest_dir", type=str, required=True, help="The destination directory")
    parser.add_argument("--new_name", type=str, required=True, help="The new name for the directory")
    args = parser.parse_args()
    relocate_directory(args.temp_dir, args.dest_dir, args.new_name)