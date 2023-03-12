// Get the DOM elements
const form = document.querySelector('form');
const input = document.querySelector('input');
const list = document.querySelector('ul');

// Load the tasks from local storage
const tasks = JSON.parse(localStorage.getItem('tasks')) || [];

// Render the tasks
function renderTasks() {
  // Clear the list
  list.innerHTML = '';

  // Add each task to the list
  for (let i = 0; i < tasks.length; i++) {
    const task = tasks[i];

    const li = document.createElement('li');
    li.textContent = task.text;

    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.checked = task.completed;

    checkbox.addEventListener('click', function() {
      task.completed = checkbox.checked;
      saveTasks();
    });

    const button = document.createElement('button');
    button.textContent = 'Delete';

    button.addEventListener('click', function() {
      tasks.splice(i, 1);
      saveTasks();
      renderTasks();
    });

    li.appendChild(checkbox);
    li.appendChild(button);
    list.appendChild(li);
  }
}

// Save the tasks to local storage
function saveTasks() {
  localStorage.setItem('tasks', JSON.stringify(tasks));
}

// Add a new task
form.addEventListener('submit', function(event) {
  event.preventDefault();
  
  const task = {
    text: input.value,
    completed: false
  };

  tasks.push(task);
  saveTasks();
  renderTasks();

  input.value = '';
});

// Render the tasks on page load
renderTasks();
