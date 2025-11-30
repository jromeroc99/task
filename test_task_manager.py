import unittest
from unittest.mock import patch, mock_open
import json
import os
from task_manager import TaskManager, Task

class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.tm = TaskManager()

    def test_add_task(self):
        """Test adding a task adds it to the list and tries to save."""
        with patch('builtins.open', mock_open()) as mocked_file:
            self.tm.add_task("Buy milk")
            self.assertEqual(len(self.tm.tasks), 1)
            self.assertEqual(self.tm.tasks[0].description, "Buy milk")
            self.assertEqual(self.tm.tasks[0].id, 1)
            self.assertFalse(self.tm.tasks[0].completed)
            
            # Verify file was opened for writing
            mocked_file.assert_called_with(Task.FILENAME, 'w')

    def test_complete_task(self):
        """Test completing a task updates its status."""
        with patch('builtins.open', mock_open()):
            self.tm.add_task("Walk dog")
            task_id = self.tm.tasks[0].id
            
            self.tm.complete_task(task_id)
            self.assertTrue(self.tm.tasks[0].completed)

    def test_delete_task(self):
        """Test deleting a task removes it from the list."""
        with patch('builtins.open', mock_open()):
            self.tm.add_task("Clean room")
            task_id = self.tm.tasks[0].id
            
            self.tm.delete_task(task_id)
            self.assertEqual(len(self.tm.tasks), 0)

    def test_list_tasks_empty(self):
        """Test listing tasks when empty prints correct message."""
        with patch('builtins.print') as mocked_print:
            self.tm.list_tasks()
            mocked_print.assert_called_with("No tasks available.")

    def test_load_tasks(self):
        """Test loading tasks from a JSON file."""
        mock_data = json.dumps([
            {'id': 1, 'description': 'Old Task', 'completed': True},
            {'id': 2, 'description': 'New Task', 'completed': False}
        ])
        
        with patch('builtins.open', mock_open(read_data=mock_data)):
            self.tm.load_tasks()
            self.assertEqual(len(self.tm.tasks), 2)
            self.assertEqual(self.tm.tasks[0].description, 'Old Task')
            self.assertTrue(self.tm.tasks[0].completed)
            self.assertEqual(self.tm.tasks[1].description, 'New Task')
            self.assertFalse(self.tm.tasks[1].completed)
            # Check next_id is updated correctly
            self.assertEqual(self.tm.next_id, 3)

    def test_load_tasks_file_not_found(self):
        """Test loading tasks handles FileNotFoundError gracefully."""
        with patch('builtins.open', side_effect=FileNotFoundError):
            self.tm.load_tasks()
            self.assertEqual(len(self.tm.tasks), 0)

if __name__ == '__main__':
    unittest.main()
