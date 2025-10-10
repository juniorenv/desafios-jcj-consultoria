import { Task } from "../models/Task.js";

export class TaskService {
    #tasks = [];
    #currentId = 1;
    
    findAll() {
        return this.#tasks;
    }
    
    findById(id) {
        return this.#tasks.find((task) => task.id === parseInt(id));
    }

    create(taskData) {
        const task = new Task(
            this.#currentId++,
            taskData.title,
            taskData.description,
            taskData.completed,
        )
        this.#tasks.push(task);
        return task;
    }
    
    update(id, taskData) {
        const foundTask = this.findById(id);
        
        if (!foundTask) return null;
        
        foundTask.update(taskData);
        
        return foundTask;
    }
    
    delete(id) {
        const taskIndex = this.#tasks.findIndex((task) => task.id === parseInt(id));
        
        if (taskIndex === -1) return null;
        
        const deletedTask = this.#tasks.splice(taskIndex, 1)[0];

        return deletedTask;
    }
}