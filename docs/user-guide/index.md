# User Guide

This is where you explain the "what" and "how" of your project's features.

## Configuration:

Explain how users can configure the project, including examples of the pyproject.toml or config.toml file.

## CLI Commands:

If your project has a command-line interface, document each command, its arguments, and options. Using a tool like mkdocs-typer2 can automate this.

```
::: mkdocs-typer2
    :module: jm_python_template.main
    :name: mkdocs-typer2
    :pretty: true
```

::: mkdocs-typer2
:module: jm_python_template.main # Use the source code where the root element is defined
:name: app # Use the real-name from the root Typer-Object
:pretty: true

## Advanced Usage:

Describe more complex use cases or features.
