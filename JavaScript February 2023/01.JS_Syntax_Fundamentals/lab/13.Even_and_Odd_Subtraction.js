function solve(arr){
    for (let i=0; i <arr.length; i++){
        arr[i] = Number(arr[i])
    }

    let evenSum=0;
    let oddSum=0;

    for (i=0; i<arr.length; i++){
        if (arr[i] % 2 == 0){
            evenSum += arr[i]
        }else{
            oddSum += arr[i]
        }
    }

    console.log(evenSum - oddSum)
}

solve([3,5,7,9])