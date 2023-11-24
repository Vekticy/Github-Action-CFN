import os
import sys

def get_branch_name():

    # try to get the branch name using git
    try:
        result = os.popen('git rev-parse --abbrev-ref HEAD').read().strip()
        return result
    except Exception as e:
        print(f"Error getting branch name: {e}")
        return None

def main():
    branch_name = get_branch_name()
    
    if branch_name == "main":
        account_id = os.getenv("AWS_ACCOUNT_PRD")
        print(f"Deploying cloudformation to {account_id} ")
    else:
        account_id = os.getenv("AWS_ACCOUNT_NPD")
        print(f"Deploying cloudformation to {account_id} ")

if __name__ == "__main__":
    main()
