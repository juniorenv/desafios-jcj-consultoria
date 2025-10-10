import express from "express";
import TaskRoutes from "./routes/taskRoutes.js";

const app = express();

const PORT = 3000;

app.use(express.json());
app.use("/api/tasks", TaskRoutes);

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
    
})

export default app;