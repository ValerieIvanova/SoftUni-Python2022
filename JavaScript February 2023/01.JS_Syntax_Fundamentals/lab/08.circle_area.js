function circleArea(inp){
    let result;
    let inpType = typeof(inp)
    if (inpType === 'number'){
        result = Math.pow(inp, 2) * Math.PI;
        console.log(result.toFixed(2));
    }
    else{
        console.log(`We can not calculate the circle area, because we receive a ${inpType}.`)
    }
}

circleArea(5)
circleArea('name')