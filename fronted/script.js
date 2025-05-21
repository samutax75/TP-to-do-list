
    <script src="script.js"></script>

    const API_URL = "http://127.0.0.1:5000/tasks";

async function loadTasks() {
    const response = await fetch(API_URL);
    const tasks = await response.json();
    
    const taskList = document.getElementById("taskList");
    taskList.innerHTML = "";
    tasks.forEach(task => {
        const li = document.createElement("li");
        li.innerHTML = `${task.title} <button onclick="deleteTask(${task.id})">❌</button>`;
        taskList.appendChild(li);
    });
}

async function addTask() {
    const taskInput = document.getElementById("taskInput");
    if (taskInput.value.trim() === "") return;

    await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title: taskInput.value })
    });

    taskInput.value = "";
    loadTasks();
}

async function deleteTask(id) {
    await fetch(`${API_URL}/${id}`, { method: "DELETE" });
    loadTasks();
}

document.addEventListener("DOMContentLoaded", loadTasks);


