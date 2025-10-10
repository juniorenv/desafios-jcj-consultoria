import express from "express";
import { TaskController } from "../controllers/taskController.js";

const router = express.Router();
const taskController = new TaskController();

router.get("/", taskController.findAll);
router.get("/:id", taskController.findById);
router.post("/", taskController.create);
router.put("/:id", taskController.update);
router.delete("/:id", taskController.delete);

export default router;