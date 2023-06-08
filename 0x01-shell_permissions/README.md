# Shell Scripting Tasks

This repository contains a set of shell scripts that perform various tasks related to file permissions and ownership. Each script is designed to fulfill specific requirements and follows the guidelines mentioned below.

## Requirements
- Allowed editors: vi, vim, emacs
- All scripts are tested on Ubuntu 20.04 LTS
- All scripts should be exactly two lines long (`$ wc -l file` should print 2)
- All files should end with a new line
- The first line of all files should be `#!/bin/bash`
- A README.md file should be present at the root of the project, describing each script's purpose
- Backticks, `&&`, `||`, or `;` are not allowed in the scripts
- All files must be executable

## Scripts

1. `0-iam_betty`: This script switches the current user to the user "betty" by executing the command `su betty`.
2. `1-who_am_i`: This script prints the effective username of the current user by executing the command `whoami`.
3. `2-groups`: This script prints all the groups the current user is part of by executing the command `groups`.
4. `3-new_owner`: This script changes the owner of the file "hello" to the user "betty" using the command `chown betty hello`.
5. `4-empty`: This script creates an empty file called "hello" in the working directory using the command `touch hello`.
6. `5-execute`: This script adds execute permission to the owner of the file "hello" using the command `chmod u+x hello`.
7. `6-multiple_permissions`: This script adds execute permission to the owner and group owner, and read permission to other users, to the file "hello" using the command `chmod u+x,g+r,o+r hello`.
8. `7-everybody`: This script adds execution permission to the owner, group owner, and other users for the file "hello" using the command `chmod ugo+x hello`.
9. `8-James_Bond`: This script sets the permission of the file "hello" to have no permission for the owner and group owner, and all permissions for other users using the command `chmod o+rwx hello`.
10. `9-John_Doe`: This script sets the mode of the file "hello" to match the mode of the file "olleh" using the command `chmod --reference=olleh hello`.
11. `10-mirror_permissions`: This script adds execute permission to all subdirectories of the current directory for the owner, group owner, and all other users using the command `chmod -R +x */`.
12. `11-directories_permissions`: This script creates a directory called "my_dir" with permissions 751 in the working directory using the command `mkdir my_dir && chmod 751 my_dir`.
13. `12-change_group`: This script changes the group owner of the file "hello" to "school" using the command `chgrp school hello`.

Please note that the file permissions and ownership may vary depending on the system and user executing the scripts. Make sure to run the scripts with appropriate permissions and in the desired working directory.

For any questions or additional information, please reach out to the repository owner.


