var search = function(nums, target) {
    let lo = 0, hi = nums.length-1;
    while (lo < hi) {
        let mid = lo + Math.floor((hi-lo+1)/2);
        console.log("Mid " + mid)
        if (target < nums[mid]) {
            hi = mid - 1
        } else {
            lo = mid; 
        }
    }
    console.log(lo)
    return nums[lo]==target?lo:-1;
};

console.log(search([1,5,7,10,15], 7))
