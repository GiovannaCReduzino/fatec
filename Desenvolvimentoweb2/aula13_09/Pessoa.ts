// npm init -y
//npm i -D typescript -->instala o pct (npm)
//npx tsc --init (tsconfig.json) --> usa o pct

export default class Pessoa { //exportação principal. Para dar mais export, tem que tirar ele 
    nome: string
    idade: number
    hobbies: string []

    constructor (nome: string, idade: number, hobbies: string[]){
        this.nome = nome
        this.idade = idade
        this.hobbies = hobbies 
    }
}
const pessoa1 = new Pessoa ("Pessoa1", 20, ["a", "b", "c"])
console.log (pessoa1)

//export default Pessoa (pode ser dessa maneira também, e aí passa o export para todos o que você quis exportar)