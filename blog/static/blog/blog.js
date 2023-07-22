function resolvedCallback(data){
  console.log("Resolved with data: "+data)
}

function rejectedCallback(message){
  console.log('Rejected with message: '+message)
}

const lazyAdd = function(a, b){
  const doAdd = (resolve, reject)=>{
    if (typeof a !== 'number' || typeof b !== 'number'){
      reject(`${a} and ${b} must be numbers`)
    }else{
      sum=a+b
      resolve(sum)
    }
  }
  return new Promise(doAdd)
}



lazyAdd(4, 6).then(resolvedCallback, rejectedCallback)

lazyAdd("mac", 'nonso').then(resolvedCallback, rejectedCallback)