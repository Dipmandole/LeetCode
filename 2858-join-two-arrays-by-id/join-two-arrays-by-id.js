/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    let joinedMap = {}

    for(let i=0; i < arr1.length; i++){
        let key = arr1[i].id;
        if(joinedMap[key] === undefined){
            joinedMap[key] = arr1[i];
        }
        else{
            let value = joinedMap[key];
            joinedMap[key] = {...value, ...arr1[i]}
        }
    }

    for(let i=0; i < arr2.length; i++){
        let key = arr2[i].id;
        if(joinedMap[key] === undefined){
            joinedMap[key] = arr2[i];
        }
        else{
            let value = joinedMap[key];
            joinedMap[key] = {...value, ...arr2[i]}
        }
    }
    return Object.values(joinedMap);  
};