import {  useEffect, useState } from "react"
import axios from "axios"

function ToDo() {
  const [task,setTask] =useState("")
  const [loading,setLoading]=useState(false)
  const [todos,setTodos]=useState([]);

  useEffect(()=>{fetchTask()},[]);

  const fetchTask=async()=>{
    try{
        const response=await axios.get("http://127.0.0.1:8000/");
        setTodos(response.data)
    }catch{
        alert("Failed to fetch tasks")
    }
  }
  const addTask=async(e)=>{
    e.preventDefault();
    setLoading(true)
    if (!task.trim()){
        alert("Task Cannot be empty")
        return;
    };
    try{
        const response=await axios.post("http://127.0.0.1:8000/",{task})
        console.log(response.data)
        alert("New task added")
    }catch{
        alert("Failed to add task")
    }finally{
        setTask("");
        setLoading(false)
    }

  }

  const updateToDoStatus=async(todo)=>{
    const response=await axios.patch(`http://127.0.0.1:8000/edit-task/${todo.id}`,{is_completed:!todo.is_completed});
    fetchTask();
    alert("Task Updated");
  }
  return (
    <div>
        <h1>ToDo</h1>
        <form onSubmit={addTask}>
            <input type="text" value={task} onChange={(e)=>setTask(e.target.value)}/>
            <button type="submit">{loading?"Saving ...":"Add Task"}</button>
        </form>

        <ul>
            {
                todos.map((todo)=>(
                    <li key={todo.id}>
                        <input type="checkbox" checked={todo.is_completed}onChange={()=>updateToDoStatus(todo)}/>
                        {todo.task}
                    </li>
                )

                )
            }
        </ul>
    </div>
  )
}

export default ToDo