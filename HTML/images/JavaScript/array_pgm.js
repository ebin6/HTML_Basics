let fruits=["apple","orange","banana"]
fruits[1]="Pineapple"
fruits.push("blueberry")//add to end position

fruits.pop()//removes from end
fruits.unshift("grape") // add value to begining
console.log(fruits)

fruits.splice(0,1)//  0 specifies the index to start removing and 2 represents how many elements to be removed
console.log(fruits)

fruits.shift()// deletes value from starting position
console.log(fruits)

let arr=['Kochi',"OneTeam",'Python',"JavaScript",'React']

arr.splice(1,3,"Java")
console.log(arr)
