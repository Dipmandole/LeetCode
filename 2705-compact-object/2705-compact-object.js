/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function(obj) {
    if (obj === null){
        return null;
    }

    if(Array.isArray(obj)){
        return obj.reduce((accumulator, currentValue) =>{
            let result = compactObject(currentValue)
            if (result){
                accumulator.push(result)
            }
            return accumulator
        }, [])
    }

    if(typeof obj === 'object'){
        return Object.keys(obj).reduce((accumulator, currentKey) =>{
            let result = compactObject(obj[currentKey])
            if (result){
                accumulator[currentKey] = result
            }
            return accumulator
        }, {})
    }
    return obj;
};