function is_eligible(){
            let my_form=document.forms["reg_form"]
            let person_age=my_form["age"].value          
            let error=document.getElementById("error_msg")
  
            if (person_age>=18){
                return true
            }
            else{
                error.textContent="Age must be greater than or equal to 18"
                return false
            }
        }