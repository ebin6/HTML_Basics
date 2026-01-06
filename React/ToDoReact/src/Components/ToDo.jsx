import { useState } from "react"
import axios from "axios"

function ToDo() {
  const [task,setTask] =useState("")
  const [loading,setLoading]=useState(false)

  const addTask=async(e)=>{
    e.preventDefault();
    const response=await axios.post("http://127.0.0.1:8000/",{task})
    console.log(response.data)
  }
  return (
    <div>
        <h1>ToDo</h1>
        <form onSubmit={addTask}>
            <input type="text" value={task} onChange={(e)=>setTask(e.target.value)}/>
            <button type="submit">Add Task</button>
        </form>
    </div>
  )
}

export default ToDo