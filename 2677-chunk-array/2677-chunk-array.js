/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    if (arr=== null || arr.length === 0 || size <= 0){
        return []
    }

    let chunkedArray = [];
    for(let i=0; i< arr.length; i = i+size){
        let subArray = arr.slice(i, i+size);
        chunkedArray.push(subArray);
    }
    return chunkedArray
};
