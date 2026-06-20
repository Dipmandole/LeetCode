/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {
    let resolveArray = new Array(functions.length);
    let count = 0;
    return new Promise((resolve,reject) => {
        functions.forEach((fn, index) => {
            let functionPromise = fn()
            functionPromise
            .then((response) =>{
                resolveArray[index] = response
                count++;
                if (count === functions.length){
                    resolve(resolveArray)
                }
            })
            .catch((error) =>{
                return reject(error)
            })
        })
    })
    
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */