import os
import sys

def get_branch_name():

    # If not, try to get the branch name using git
    try:
        result = os.popen('git rev-parse --abbrev-ref HEAD').read().strip()
        return result
    except Exception as e:
        print(f"Error getting branch name: {e}")
        return None

def main():
    branch_name = get_branch_name()
    
    if branch_name:
        print(f"The branch name is: {branch_name}")
    else:
        print("Unable to determine the branch name.")

if __name__ == "__main__":
    main()
