class Greeter{
  constructor(name){
    this.name=name
  }

  getGreeting(){
    if (this.name===undefined){
      return "Hello, no name"
    }
    return "Hello "+ this.name
  }

  showGreeting(greetingMessage){
    console.log(greetingMessage)
  }

  greet(){
    this.showGreeting(this.getGreeting())
  }
}



class DelayGreeter extends Greeter{
  delay=2000
  constructor(name, delay){
    super(name)
    if(delay !==undefined){
      this.delay=delay
    }
  }

  greet(){
    setTimeout(
      ()=>{
        this.showGreeting(this.getGreeting())
      }, this.delay)
  }
}
const g= new DelayGreeter("Chinonso")
g.greet()

const mac= new DelayGreeter("Macson", 1000)
mac.greet()