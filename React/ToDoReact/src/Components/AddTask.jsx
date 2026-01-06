import { useState } from "react"
import axios from "axios";

function AddTask() {
  const [task,setTask]=useState("");
  const [loading,setLoading]=useState(false);

  const addtask=async(e)=>{
    e.preventDefault();
    setLoading(true)
    try{
        if(!task.trim()){
            alert("Task cannot be empty")
            return;
        }
        const response=await axios.post("http://127.0.0.1:8000/",{task})
        console.log(response.data)
        setTask("");
        alert("New task added")
    }catch(err){
        console.error(err)
    }finally{
        setLoading(false)
    }

    

  }
  return (
    <div>
        <h1>Add Task</h1>
        <form onSubmit={addtask}>
            <label>Enter your task : </label>
            <input type="text" value={task} onChange={(e)=>setTask(e.target.value)}/>
            <button type="submit">{loading?"Saving..":"Add Task"}</button>
        </form>
    </div>
  )
}

export default AddTask