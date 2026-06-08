/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    let current = init

    for(let i = 0; i < nums.length; i++){
        current = fn(current,nums[i])
    }
    return current;
};