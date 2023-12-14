data = { "contributing" : """

# Contributing Guidelines

Thank you for considering contributing to the **{project_name}** project! We welcome contributions from the community to make this project even better. Whether you're a developer, designer, tester, or just an enthusiast, your help is highly valued. Please take a moment to read through the guidelines outlined below to ensure a smooth collaboration process.

## Contributing

### Reporting Issues

If you encounter any bugs or have suggestions for improvements, please feel free to [create an issue](https://github.com/izam-mohammed/{repo_name}/issues/new/choose) in the GitHub repository. When creating an issue, please provide detailed steps to reproduce the problem.

### Feature Requests

We're open to new ideas and features! If you have a feature request, please [create an issue](https://github.com/izam-mohammed/{repo_name}/issues/new/choose) with a clear description of the feature and its use case. We'll discuss it and decide on the best way to proceed.

### Pull Requests

We welcome pull requests! To contribute code:

1. Fork the repository and create a new branch for your feature or bug fix.

2. Make your changes and ensure the code follows our [coding guidelines](#coding-guidelines).

3. Write tests if applicable and make sure all existing tests pass.

4. Submit a pull request, explaining your changes and the problem they solve. Reference any related issues.

## Coding Guidelines

- Follow the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide for Python code.

- Format all files with [black](https://github.com/psf/black) code formatting

- Write clear and concise code with meaningful variable and function names.

- Add docstrings and comments to explain complex logic or functionality.

- Use version control effectively. Each commit should represent a logical unit of work.

## Code of Conduct

Please note that by participating in this project, you are expected to abide by our [Code of Conduct](CODE_OF_CONDUCT.md). We aim to maintain a friendly and welcoming community for everyone.

## License

By contributing to this project, you agree that your contributions will be licensed under the [project's license](LICENSE).

---

We appreciate your interest in contributing to **{project_name}**! Your involvement helps us create a better product for everyone. If you have any questions, feel free to reach out to us through issues or discussions. Happy coding!"""

, 




        
"readme" : """

# {project_name}

<p>
<img src="https://img.shields.io/badge/Python-239120?logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/html5-E34F26?logo=html5&logoColor=white" />
<img src="https://img.shields.io/badge/css3-1572B6?logo=css3&logoColor=white" />
<img src="https://img.shields.io/badge/bootstrap-563D7C?logo=bootstrap&logoColor=white" />
<img src="https://img.shields.io/badge/Github-181717?logo=github&logoColor=white" />
<img src="https://img.shields.io/badge/GIT-E44C30?logo=git&logoColor=white" />
<img src="https://img.shields.io/badge/prettier-1A2C34?logo=prettier&logoColor=white" />
<img src="https://img.shields.io/badge/docker-1572B6?logo=docker&logoColor=white" />
<img src="https://img.shields.io/badge/GitHub_Actions-563D7C?logo=github-actions&logoColor=white"/>
</p>

![PyPI v0.5](https://img.shields.io/badge/PyPI-v0.5-blue.svg)
![MIT License](https://img.shields.io/badge/License-MIT-lightgray.svg)
![build](https://img.shields.io/badge/Build-passing-green.svg)

{short_description}

### Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py

## Contributing

Contributions are welcome! If you'd like to contribute to the project, feel free to submit issues or pull requests. Please ensure your contributions align with the project's coding standards and guidelines.

## Repository Code Formatting

This repository follows a consistent code formatting approach to enhance readability and maintainability.

### Python Files

Python files in this repository are formatted using [Black](https://github.com/psf/black). Black is an opinionated code formatter that automatically formats your Python code to adhere to the PEP 8 style guide.

To ensure that your Python code is formatted correctly, you can install Black and format the code by running the following command in your terminal:

```bash
pip install black
black .
```

### HTML Files

HTML files in this repository are formatted using [Prettier](https://prettier.io/). Prettier is a code formatter that supports multiple languages, including HTML.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- The project utilizes the [Django Framework](https://www.djangoproject.com/) for web development.
- UI styling is based on [Bootstrap](https://getbootstrap.com/) for a responsive design.
- Icons are provided by [Font Awesome](https://fontawesome.com/).

---

Feel free to customize this `README.md` template to suit your project's specific details and add any additional sections you find relevant.

*Thanks !* """





        
, "docker" : """

FROM python:3.8-slim-buster

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]
"""
,




        
"bug_report":"""
---
name: Bug Report 🐛
about: Create a report to help us improve
title: 'Short but Descriptive Bug Title'
labels: 'bug'
assignees: ''

---

## Bug Description 📄

**Describe the bug**
A clear and concise description of what the bug is. Include details about the unexpected behavior you observed.

## Steps to Reproduce 🔄

**To Reproduce**
Provide detailed steps to reproduce the behavior:

1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. Describe the error or unexpected behavior you encountered.

**Expected behavior**
A clear and concise description of what you expected to happen. Explain the correct or intended behavior.

## Screenshots 📸

**Screenshots**
If applicable, add screenshots or screen recordings to help visualize the problem. Annotate the images if necessary.

## Environment Details 🖥️

**Desktop (if applicable):**
- **OS:** [e.g. Windows 10, macOS]
- **Browser:** [e.g. Chrome, Firefox]
- **Browser Version:** [e.g. 98.0.4758.102]

**Smartphone (if applicable):**
- **Device:** [e.g. iPhone 12]
- **OS:** [e.g. iOS 15]
- **Browser:** [e.g. Safari, Chrome]
- **Browser Version:** [e.g. 98.0.4758.102]

## Additional Context 🌐

**Additional context**
Add any other relevant information about the problem here. Include details about your environment, network conditions, or any recent changes that might be related to the issue.

## Checklist ✅

- [ ] I have searched for existing bug reports to confirm that this is a new issue.
- [ ] I have provided clear and detailed information to help diagnose the bug.
- [ ] I have attached screenshots or other media, if applicable.
- [ ] I have mentioned the environment details to help with debugging.
- [ ] I have added relevant labels and assigned the appropriate stakeholders.

Feel free to adjust this template based on your specific project requirements. Providing detailed information helps developers understand and address the bug more efficiently. If you have any questions or need further clarification on any section, let me know!
"""
, 





        
"feature_request":"""
---
name: Feature Request 🚀
about: Suggest an enhancement or new feature for this project
title: 'Brief but Descriptive Title'
labels: 'enhancement'
assignees: ''

---

## Problem Statement 🤔

**Is your feature request related to a problem? Please describe.**
A clear and concise description of the problem or limitation you've encountered. Be specific about the scenario or user experience that led to this feature request.

## Proposed Solution 💡

**Describe the solution you'd like**
A clear and concise description of the enhancement or new feature you are suggesting. Provide details on how this solution will address the identified problem or limitation.

**Benefits and Impact**
Explain the benefits of implementing this feature and the positive impact it will have on users, workflow, or overall project goals.

## Alternatives Considered 🔄

**Describe alternatives you've considered**
If you've explored other solutions or features, please share them. Discuss the pros and cons of each alternative, and explain why you believe the proposed solution is the best approach.

## Additional Context 📚

**Additional context**
Add any other relevant information, context, or screenshots about the feature request here. Include links to related discussions, documents, or external resources that support your proposal.

**User Stories**
If applicable, provide one or more user stories that illustrate how users would benefit from this feature.

**Impact on Existing Functionality**
Discuss any potential impact on existing functionality, workflows, or integrations that should be considered.

## Checklist ✅

- [ ] I have searched for existing feature requests and confirmed that this is a new suggestion.
- [ ] I have provided clear and detailed information to support my feature request.
- [ ] I have considered and discussed alternative solutions.
- [ ] I have added relevant labels and assigned the appropriate stakeholders.

Feel free to customize this template further based on your project's specific needs. If you have any questions or need clarification on any section, let me know!
."""

,



        
"greetings":"""
name: Greetings

on: [pull_request_target, issues]

jobs:
  greeting:
    runs-on: ubuntu-latest
    permissions:
      issues: write
      pull-requests: write
    steps:
    - uses: actions/first-interaction@v1
      with:
        repo-token: ${{ secrets.GITHUB_TOKEN }}
        issue-message: "Thanks a lot for the first issue posting"
        pr-message: "Thanks a lot for your first Pull Request"
        """
, 
       


"funding": """github: [izam-mohammed]"""



, "gitignore":"""
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
.python-version

# dotenv
.env

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# Django development
db.sqlite3
manage.py

# VSCode settings
.vscode/

# Sublime Text settings
*.sublime-project
*.sublime-workspace

# PyCharm settings
.idea/

# Environments
.env/
env/
venv/
ENV/

# Miscellaneous
*.log
*.pot
*.pyc
*.swp
._*
.DS_Store


# Jupyter Notebooks
.ipynb_checkpoints/

# Model files
*.model
*.h5

# Compiled Python files
__pycache__/

# Distribution/installation
dist/
build/

# Ignore any saved models or checkpoints
model_checkpoints/

# Ignore system-specific files
.DS_Store
Thumbs.db

# artifacts
artifacts/

#catboost
catboost_info/
reports/"""








,"licence":"""
MIT License

Copyright (c) 2023 Izam Mohammed

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""




,"404":"""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-geWF76RCwLtnZ8qwWowPQNguL3RmwHVBC9FhGdlKrxdiJJigb/j/68SIy3Te4Bkz"
        crossorigin="anonymous"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css"
        integrity="sha512-z3gLpd7yknf1YoNbCzqRKc4qyor8gaKU1qmn+CShxbuBusANI9QpRohGBreCFkKxLhei6S9CQXFEbbKuqLg0DA=="
        crossorigin="anonymous" referrerpolicy="no-referrer" />
</head>

<body>



    <div class="container d-flex" style="flex-direction: column; align-items:center; justify-content:center">
        <h1 style="margin-top: 40px;">Oops!</h1>
        <h1></h1>
        <h1 class="text-danger" style="z-index: 3;">404 Error Occurred</h1>
        <p style="z-index: 3;">Unfortunately the page you are looking for has been moved or deleted</p>
        <img style="height: 20rem; margin-top:-60px; z-index:0"
            src="https://cdn.dribbble.com/users/252114/screenshots/3840347/mong03b.gif" alt="">
        <div style="margin-top: -50px; z-index:2"
            class="text-center text-lg-start pt-2 d-flex justify-content-center align-items-center ">
            <a href="/" type="submit" class="btn add-btn btn-lg"
                style="padding-left: 2.5rem; padding-right: 2.5rem; margin-top:-20px">bach to home</a>
        </div>
    </div>


</body>

</html>"""






,
"code_of_conduct":"""

# Code of Conduct

The Django Note Taking Website project is committed to creating a welcoming and inclusive community for all participants. This Code of Conduct outlines our expectations for behavior and interactions within the project's community, both online and offline. We value diversity and respect for each other's opinions, and we encourage all participants to contribute to a positive and supportive environment.

As a contributor or participant in this project, you agree to abide by this Code of Conduct. If you observe any violations or have concerns about the behavior of any community member, please report it to the project maintainers or administrators.

### Expected Behavior

- **Be Respectful:** Treat all participants with respect and kindness, regardless of their background, experience level, gender, sexual orientation, race, religion, or any other personal attributes.

- **Inclusive Language:** Use language that is inclusive, non-discriminatory, and respectful of all individuals and groups.

- **Open-Mindedness:** Be open to constructive criticism and diverse opinions. Engage in discussions and disagreements in a professional and considerate manner.

- **Collaboration:** Collaborate and communicate in a way that fosters a positive and productive atmosphere for everyone. Help others learn and grow through shared knowledge and experiences.

### Unacceptable Behavior

The following behaviors are considered unacceptable within the Django Note Taking Website community:

- **Harassment:** Any form of harassment, including but not limited to offensive comments, intimidation, or unwelcome advances, is not tolerated.

- **Discrimination:** Discrimination based on personal attributes, including but not limited to gender, race, sexual orientation, religion, and disability, is strictly prohibited.

- **Hate Speech:** Any form of hate speech, including slurs, derogatory language, and offensive jokes, is not allowed.

- **Bullying:** Bullying or any behavior that creates an intimidating, hostile, or uncomfortable environment for others will not be tolerated.

- **Trolling:** Deliberate provocation or incitement of arguments or conflicts, without any intention of meaningful contribution, is unacceptable.

- **Inappropriate Content:** Sharing or promoting explicit, violent, or otherwise inappropriate content is prohibited.

### Reporting and Enforcement

If you believe that someone has violated this Code of Conduct, please report it to the project maintainers or administrators. All reports will be kept confidential, and appropriate actions will be taken based on the severity of the violation. Enforcement actions may include warnings, temporary bans, or permanent bans from participating in the project's community spaces.

### Attribution

This Code of Conduct is adapted from the [Contributor Covenant](https://www.contributor-covenant.org/), version 2.0. We value the principles of this code and believe that it fosters a positive and inclusive community environment.

### Conclusion

By participating in the {project_name}, you acknowledge and agree to abide by this Code of Conduct. We are committed to creating a safe, respectful, and collaborative environment where all participants can learn, share, and contribute. Thank you for being a part of our community.

_Last updated: August 12, 2023_"""





,"security":"""
# Security Policy

## Reporting Security Issues

**DO NOT** file a public issue to report a security vulnerability, as it could put the security of the project and its users at risk. Instead, please follow the instructions below.

To report a security issue, please send an email to [mail](izamdeveloper1@gmail.com) with the following details:

- Your name and affiliation (if applicable).
- A detailed description of the vulnerability, including steps to reproduce (if possible).
- Any relevant logs, error messages, or screenshots that can help understand and assess the issue.
- Any other relevant information that might help us understand and address the vulnerability.

We will acknowledge your email within 48 hours and strive to provide a timeline for a resolution or further steps within 72 hours of acknowledgment. 

Please note that this email is for reporting security vulnerabilities only. For general inquiries or support requests, please contact us through the appropriate channels mentioned in the project's documentation.


## Security Updates

We are committed to addressing security vulnerabilities and will provide security updates for supported versions. Please make sure to always use a supported version of the project to receive these updates.

## Vulnerability Disclosure Process

1. **Report**: Send an email to the official mail. to report the vulnerability. Include all necessary information for us to understand and reproduce the issue.

2. **Assessment**: We will triage and assess the reported vulnerability. We may request additional information or clarifications from you.

3. **Fix & Validation**: If the vulnerability is confirmed, we will work on a fix. Once the fix is ready, we will validate it to ensure it effectively addresses the vulnerability without introducing new issues.

4. **Security Update**: A security update will be released containing the fix. This update will be made available for all supported versions.

5. **Public Disclosure**: We will wait for a reasonable period of time to allow users to update to the patched versions. After this period, we will publicly disclose the vulnerability, along with information about the fix.

## Best Practices for Users

- Keep your project dependencies updated to ensure you have the latest security patches.

- Star the repository.

- If you're using third-party packages, regularly check for their security advisories and updates.

## Responsible Disclosure

We appreciate the security community's efforts in disclosing vulnerabilities responsibly and will acknowledge your contributions. We are committed to addressing security issues promptly and providing appropriate credit to reporters.

Thank you for your collaboration in making our project safe and secure.

## Disclaimer

This document may be subject to changes and updates. It's your responsibility to stay informed about the latest version and content."""

}

config_files={
"CONTRIBUTING.md":{
       "data":data["contributing"],
       "dependency":["project_name", "repo_name"]
       },
"README.md":{
       "data":data["readme"],
       "dependency":["project_name", "short_description"]
       },
"Dockerfile":{
       "data":data["docker"],
       "dependency":[]
       },
".github/ISSUE_TEMPLATE/bug_report.md":{
       "data":data["bug_report"],
       "dependency":[]
       },
".github/ISSUE_TEMPLATE/feature_request.md":{
       "data":data["feature_request"],
       "dependency":[]
       },
".github/wordflows/greetings.yml":{
       "data":data["greetings"],
       "dependency":[]
       },
".github/FUNDING.yml":{
       "data":data["funding"],
       "dependency":[]
       },
".gitignore":{
       "data":data["gitignore"],
       "dependency":[]
       },
"LICENCE":{
       "data":data["licence"],
       "dependency":[]
       },
"templates/404.html":{
       "data":data["404"],
       "dependency":[]
       },
"CODE_OF_CONDUCT.md":{
       "data":data["code_of_conduct"],
       "dependency":["project_name"]
       },
"SECURITY.md":{
       "data":data["security"],
       "dependency":[]
       }
}

import os
import sys
try:
        pargv = sys.argv[1:]
        project_config = ["", "", ""]
        k = 0
        for i in argv:
                if i=="__":
                        k += 1
                else:
                        project_config[k] += i
        project_name, repo_name, shortdescription = project_config
        for file_path in config_files:
            if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
                with open(filepath, "w") as f:
                        if filepath == "CODE_OF_CONDUCT.md":
                                f.write(config_files[file_path].format(project_name))
                        elif filepath == "README.md":
                                f.write(config_files[file_path].format(project_name=project_name, short_description=shortdescription))
                        elif filepath == "CONTRIBUTING.md":
                                f.write(config_files[file_path].format(project_name=project_name, repo_name=repo_name))
                        f.write(config_files[file_path])
            else:
                    print(f"{filename} is already exists")
except Exception as e:
        print(f"error - {e}")
