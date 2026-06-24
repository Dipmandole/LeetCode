/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    if(this === null || this.length === 0){
        return {};
    }
    let result = {};
    for(let i = 0; i < this.length; i++){
        let item = this[i];
        let key = fn(item);

        let valueArray = result[key] != undefined ? result[key] : [];
        valueArray.push(item);
        result[key] = valueArray;
    }
    return result
    
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */