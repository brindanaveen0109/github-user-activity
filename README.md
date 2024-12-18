# github-user-activity
A command-line tool that fetches and displays recent activity for a specified GitHub user. This tool retrieves events such as commits, issues, pull requests, and more from a user's GitHub account and presents the information in a clean, readable format.
### Requirements
<li> Requirements
Python 3.x or any compatible environment. </li>
<li> Requests library for HTTP requests.</li>

### Installation
1. Clone the repository `git clone https://github.com/brindanaveen0109/github-user-activity.git`
2. Navigate into the project folder `cd github_user_activity`

### Usage
To run the script from command line:
1. Install and run nuitka, which is used to convert python script to executable script use `pip install nuitka`
2. Run the command  `nuitka --standalone --onefile --output-dir=dist github_user_activity.py` which is the command used to convert python script to executable script.
    Code breakdown: --standalone: Packages all the dependencies into a single folder.
                    --onefile: Creates a single executable .exe file.
                    --output-dir-dist: Specifies that the output has to be in a directory called "dist"
3. Navigate into github_user_activity.dist and find the executable file.
4. To run this executable file, run command in the format  `.\github_user_activity <username>`. 
