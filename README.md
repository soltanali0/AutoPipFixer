# AutoPipFixer

AutoPipFixer is a Python script that automatically installs missing Python packages when a command fails due to `ModuleNotFoundError`. It continuously runs the command until all required packages are installed.

## Features

- Automatically detects missing Python packages.
- Installs missing packages using `pip`.
- Continuously runs the specified command until all dependencies are resolved.

## Installation

Clone the repository:

```sh
git clone https://github.com/soltanali0/AutoPipFixer
```
Navigate to the project directory:
```sh
cd AutoPipFixer
```

## Usage

Run the script with the command you want to execute:

```sh
python autopipfixer.py -c "your_command_here"
```

For example:

```sh
python pipfixer.py -c "objection --gadget 'infosecadventures.allsafe' device-type"
```

## Example

```sh
python pipfixer.py -c "python your_script.py"
```
If your_script.py has any missing dependencies, AutoPipFixer will detect them and install them automatically.

