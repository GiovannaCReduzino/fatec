class Queue { //2. Criando a classe Queue
    constructor() {
      this.items = {};
      this.head = 0;
      this.tail = 0;
    }
  
    enqueue(element) { //adiciona um novo elemento no final da fila
          this.items[this.tail] = element;
          this.tail++;
    }
  
    dequeue() { //remove o primeiro elemento da fila (o item que está na frente). Também devolve o elemento removido
          if (this.isEmpty()) {
          return undefined;
          }
          const item = this.items[this.head];
          delete this.items[this.head];
          this.head++;
          return item;
    }
  
    peek() { //Devolve o 1º elemento da fila - é o 1º item adicionado e o primeiro que será removido, mas será devolvido apenas como informação
          if (this.isEmpty()) { 
          return undefined;
          }
          return this.items[this.head];
    }
    
    size (){ //devolve o número de elementos contidos na fila
        return this.count - this.lowestCount;
    }

    isEmpty (){ // isEmpty() = devolve 'true' se a fila não contiver nenhum elemento, e false se o tamanho for maior que 0
        return this.size() === 0;
    }
    
    clear() {
        this.itens = {}; 
        this.count = 0;
        this.lowestCount = 0;
    }
    
    toString(){
        if (this.isEmpty()) {
            return '';
        }
        let objString = `${this.items[this.lowestCount]}`;
        for (let i=this.lowestCount + 1; i <this.count; i++) {
            objString = `${objString},${this.items[i]}`;
        }
        return objString;
    }
       
}

const queue = new Queue();
console.log(queue.isEmpty()); //exibe true

queue.enqueue ('John');
queue.enqueue ('Jack');
console.log (queue.toString()); //John, Jack

queue.enqueue ('Camila');

console.log (queue.toString()); //John, Jack, Camila
console.log (queue.size()); //exibe 3
console.log (queue.isEmpty()); //exibe false

queue.dequeue(); //remove John
queue.dequeue(); //remove Jack
console.log (queue.toString()); //Camila
