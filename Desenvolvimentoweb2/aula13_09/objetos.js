// objeto literal

const pessoa1 = {
    nome: "Pessoa1", //atributo
    idade: 20,
    hobbies: ["Jogar", "assistir tv", "programar"]
}

console.log (pessoa1.nome) //imprime o atributo de um objeto
pessoa1.cpf = 123456

pessoa1.hobbies.push ("outra atividade")
console.log(pessoa1)

//funções

function criaPessoas (nome, idade, hobbies){ //pode fazer checagens dentro e não deixa a pessoa criar os dados de qualquer jeito
    return {
        nome,
        idade,
        hobbies
    }
}

const pessoa2 = criaPessoas ("Nome2", 25, ["a","b","c"])

//transforma pessoa2 em uma string em JSON
console.log (JSON.stringify(pessoa2))
/*caminho inverso "JSON.parse()"
const pessoaJSON = JSON.parse ('{"nome": "Nome2", "idade:25", "hobbies": ["a", "b", "c"]}')
console.log(pessoaJSON)*/

// --> Classes
/*obs: Classe sempre começa com uma letra maiúscula*/

class Pessoa {
    //cria método constructor
    constructor (nome, idade, hobbies) {
        this.nome = nome
        this.idade = idade
        this.hobbies = hobbies
        this.cpf = ''
    }
    //cria um método personalizado
    meApresentar () {
        console.log ('Olá meu nome é ${this.nome}!')
    }

    anoNascimento (){
        return 2024 - this.idade
    }
}
const pessoa3 = new Pessoa ("Pessoa3", 70, ['a', 'b'])
//chamando os métodos
pessoa3.meApresentar()
pessoa3.anoNascimento()

