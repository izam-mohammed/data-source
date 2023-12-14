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

, "readme" : """

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
       }


