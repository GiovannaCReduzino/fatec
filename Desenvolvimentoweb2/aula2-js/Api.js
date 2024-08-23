//APIs
/*
- Um contrato de serviço entre duas aplicações
    lugar onde tem dados e o código faz as requisições

- Api entra como JSON ou XML
*/

import express from 'express' // importanto express

const app = express() // inicializando na variável app
const port = 3000 //qual porta vai rodar meu servidor

app.use(express.json()) //Função pronta do express | Avisou que vai receber JSON

app.get('/', (requisicao, resposta) => { //qual o caminho de rota > () definir função
    resposta.send ('Olá mundo!')
})

app.get('/teste', (requisicao, resposta) => { //qual o caminho de rota > () definir função
    resposta.json ({msg: "Teste"})
}) //Devolveu uma resposta formatada como JSON

/*node api.js - Rodar a API */
app.listen(port, () => {
    console.log (`API rodando em http://localhost:${port}`)
})

//Prática
app.get('/tabuada', (requisicao, resposta) => { //qual o caminho de rota > () definir função
    const numero = 4
    let tabuadaPronta = ''
    for (let i = 1; i <=10; i++){
        tabuadaPronta += `<p>${numero}X${i}=${numero*i}</p>`   
    } 
    resposta.send (tabuadaPronta)
})