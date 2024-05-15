#!/usr/bin/env python3
import os
import argparse

def create_admin(username, password):
    # Your logic for creating the admin goes here
    # For demonstration purposes, let's just print the admin info
    print(f"Admin created: Username = {username}, Password = {password}")

def main():
    parser = argparse.ArgumentParser(description="Create an admin user")
    parser.add_argument("--username", required=True, help="Admin username")
    parser.add_argument("--password", required=True, help="Admin password")

    args = parser.parse_args()

    # Call the function to create the admin
    create_admin(args.username, args.password)

    # Now you can write the admin info to a file next to your project files
    # For example:
    admin_info = f"Username: {args.username}\nPassword: {args.password}"
    project_dir = os.path.dirname(os.path.abspath(__file__))
    admin_file_path = os.path.join(project_dir, "admin_info.txt")

    with open(admin_file_path, "w") as admin_file:
        admin_file.write(admin_info)

    print(f"Admin info saved to {admin_file_path}")

if __name__ == "__main__":
    main()
