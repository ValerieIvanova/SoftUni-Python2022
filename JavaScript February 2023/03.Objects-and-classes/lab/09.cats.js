function solve(input) {
    let cats = []
    class Cat {
        constructor(name, age) {
            this.name = name
            this.age = age
        }
        meow (){
            console.log(`${this.name}, age ${this.age} says Meow`);
        }
    }

    for (const line of input) {
        let [name,age] = line.split(' ')
        age = Number(age)
        cats.push(new Cat(name, age))
    }

    for (const cat of cats) {
        cat.meow();
    }
}

solve(['Mellow 2', 'Tom 5'])