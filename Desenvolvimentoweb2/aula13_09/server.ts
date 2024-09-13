//npm i express
//npm i -D @types/express  @types/node (rodar na)
import express from 'express'
import Pessoa from'./Pessoa'

const app = express () //factory
const port = 3000 //configura a porta

app.get('/pessoas',(req, res)=>{ //end point da API
    const pessoa1 = new Pessoa ("Nome", 20, ["programar"])
    const pessoa2 = new Pessoa ("Teste2", 25, ["a","b"])
    const listaPessoas = [pessoa1, pessoa2]
    res.json(listaPessoas)
})
app.listen(port, ()=>{
    console.log (`API rodando em http://localhost:${port}`)
})
