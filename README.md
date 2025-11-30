# Task Manager Application

A simple yet powerful command-line Task Manager application written in Python. This application helps you organize your daily tasks and features an AI-powered assistant to break down complex tasks into simpler, actionable sub-tasks.

## Features

- **Task Management**:
  - Add new tasks.
  - List all tasks with status indicators (✓ for completed, ✗ for pending).
  - Mark tasks as completed.
  - Delete tasks.
- **AI Integration**: Uses OpenAI to automatically generate a list of simple sub-tasks from a single complex task description.
- **Persistence**: Automatically saves and loads tasks from a `tasks.json` file, so you never lose your data.

## Project Structure

- `main.py`: The entry point of the application, handling the user interface and menu loop.
- `task_manager.py`: Core logic for managing tasks, including adding, completing, deleting, and saving/loading from disk.
- `ai_service.py`: Handles the integration with the OpenAI API to generate sub-tasks.
- `test_task_manager.py`: Unit tests to ensure the reliability of the task manager logic.
- `requirements.txt`: Lists the Python dependencies required for the project.

## Prerequisites

- Python 3.x
- An OpenAI API Key (required for the AI sub-task generation feature)

## Installation

1. **Clone the repository** (if applicable) or download the source code.

2. **Install dependencies**:
   Navigate to the project directory and run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**:
   Create a `.env` file in the root directory of the project and add your OpenAI API key:
   ```env
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

Run the application using Python:

```bash
python main.py
```

### Menu Options

1. **Add Task**: Enter a description to create a new task.
2. **List Tasks**: View all your current tasks and their status.
3. **Complete Task**: Mark a task as done by entering its ID.
4. **Delete Task**: Remove a task permanently by entering its ID.
5. **Create Simple Tasks using AI**: Enter a complex task (e.g., "Plan a birthday party"), and the AI will generate a list of sub-tasks for you.
6. **Exit**: Close the application.

## Testing

To run the unit tests and verify the application logic:

```bash
python -m unittest test_task_manager.py
```

## License

This project is open-source and available for personal and educational use.