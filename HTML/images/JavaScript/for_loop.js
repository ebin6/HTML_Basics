/*let num=4;
for(let i=1;i<=10;i++){
    console.log(`${i} * ${num} = ${i*num}`)
}*/



let counter=1

while(counter<=5){
    
    if(counter==3){
        counter++
        continue
    }
    console.log(counter)
    counter+=1
}


let num=1;
do{
    console.log(num)
    num++
}while(num<=10);