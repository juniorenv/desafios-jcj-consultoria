import { ValidationError } from "../errors/ValidationError.js";

export class Task {
    constructor(id, title, description, completed) {
        this.id = id;
        this.title = title;
        this.description = description;
        this.completed = completed;
        this.createdAt = new Date();
    }
    
    update(data) {
        if (data.title === undefined) {
            throw new ValidationError('Title is required');
        }
        if (data.description === undefined) {
            throw new ValidationError('Description is required');
        }
        if (data.completed === undefined) {
            throw new ValidationError('Completed is required');
        }
        if (typeof data.completed !== "boolean") {
            throw new ValidationError('Completed must be a boolean value');
        }
        
        this.title = data.title;
        this.description = data.description;
        this.completed = data.completed;

        return this;
    }
}