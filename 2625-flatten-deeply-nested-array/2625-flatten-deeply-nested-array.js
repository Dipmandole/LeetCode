/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {
    if(n === 0){
        return arr;
    }
    
    let resultArray = [];
    const flatFunction = (array, number) => {
        for(let i = 0; i<array.length; i++){
            let item = array[i];
            if(Array.isArray(item) && number > 0){
                flatFunction(item, number - 1)
            }
            else{
                resultArray.push(item);
            }
        }
    }
    flatFunction(arr , n)
    return resultArray;
};