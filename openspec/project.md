# Project Context

## Purpose
Kinbank Website is a web application for exploring kinship terms and cultural data across languages. It provides interactive visualizations, search, and data browsing for researchers and the public.

## Tech Stack
- Python 3.9
- Django (web framework)
- Pandas (data manipulation)
- SQLite (database)
- HTML/CSS/JS (frontend)
- Docker (deployment)
- Gunicorn, Nginx (production server)
- R (for some scripts)

## Project Conventions

### Code Style
- PEP8 for Python
- 4-space indentation
- Descriptive variable and function names
- Django app structure
- Use of comments for clarity

### Architecture Patterns
- Django MVC (Model-View-Controller)
- Modular apps: kb, kinbank, mysite
- Static and template separation
- Use of helper functions for data processing

### Testing Strategy
- Django test framework (unit tests in tests.py)
- Manual testing for UI
- Data validation scripts

### Git Workflow
- Feature branches for new work
- Pull requests for review
- Commit messages: concise, imperative mood
- Main branch for production

## Domain Context
- Kinship terms, glottocode, language metadata
- CSV and database integration
- Visualizations for kinship diagrams

## Important Constraints
- Data privacy for unpublished datasets
- Compatibility with academic standards
- Dockerized deployment for reproducibility

## External Dependencies
- Django, Pandas, Gunicorn, Nginx
- SQLite database
- R scripts for data conversion
