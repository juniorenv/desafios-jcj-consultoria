import { ValidationError } from "../errors/ValidationError.js";
import { TaskService } from "../services/taskService.js";

export class TaskController {
    constructor(taskService = new TaskService()) {
        this.taskService = taskService;
    }

    findAll = async (req, res) => {
        try {
            const tasks = this.taskService.findAll();
            res.status(200).json({ success: true, data: tasks });
        } catch (error) {
            res.status(500).json({ success: false, error: error.message });
        }
    }
    
    findById = async (req, res) => {
        try {
            const task = this.taskService.findById(req.params.id);
            
            if (!task) {
                return res.status(404).json({ success: false, error: 'Task not found' });
            }
            
            res.status(200).json({ success: true, data: task });
        } catch (error) {
            res.status(500).json({ success: false, error: error.message });
        }
    }

    create = async (req, res) => {
        try {
            const { title, description, completed = false } = req.body;

            if (!title) {
                return res.status(400).json({ success: false, error: 'Title is required' });
            }

            if (!description) {
                return res.status(400).json({ success: false, error: 'Description is required' });
            }
            
            if (typeof completed !== "boolean") {
                return res.status(400).json({ success: false, error: 'Completed must be a boolean value' });
            }

            const createdTask = this.taskService.create({ title, description, completed });

            res.status(201).json({ success: true, data: createdTask });
        }
        catch (error) {
            res.status(500).json({ success: false, error: error.message });
        }
    }
    
    update = async (req, res) => {
        try {
            const task = this.taskService.update(req.params.id, req.body);

            if (!task) {
                return res.status(404).json({ success: false, error: 'Task not found' });
            }
            
            res.status(200).json({ success: true, data: task });
        }
        catch (error) {
            if (error instanceof  ValidationError) {
                return res.status(400).json({ success: false, error: error.message });
            }
            res.status(500).json({ success: false, error: error.message });
        }
    }

    delete = async (req, res) => {
        try {
            const deletedTask = this.taskService.delete(req.params.id);
            
            if (!deletedTask) {
                return res.status(404).json({ success: false, error: 'Task not found' });
            }
            
            res.status(200).json({ success: true, data: deletedTask });
        }
        catch (error) {
            res.status(500).json({ success: false, error: error.message });
        }
    }
}