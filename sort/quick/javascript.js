"use strict";
const { performance } = require('perf_hooks');

function sort(arr, l, r) {
	// error checks
	if (!arr && arr !== []) {
		console.log("error provide an array")
		return;
	}
	if (l < 0 || l >= arr.length) return;
	if (r < 0 || r >= arr.length) return;

	// default parameters
	if (!l) l = 0;
	if (!r) r = arr.length;

	const quickSort = function(arr, l, r) {
		const partition = function(arr, l, r) {
			const pivot = arr[r]
			let i = l - 1;
			for (let j = l; j <= r; j++) {
				if (arr[j] < pivot) {
					i++
					[arr[i], arr[j]] = [arr[j], arr[i]];
				}
			}
			[arr[r], arr[i+1]] = [arr[i+1], arr[r]]
			return (i+1)
		}
		if (l < r) {
			const pi = partition(arr, l, r);
			quickSort(arr, l, pi-1)
			quickSort(arr, pi+1, r)
		}
	}
	quickSort(arr,l,r)
	return arr
}

(function () {
	const tests = new Map([
		[[12, 41, 5, 2, 3], [2, 3, 5, 12, 41]],
		[[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]],
		[[1, 1, 0], [0, 1, 1]],
		[[-1, 1, -1], [-1, -1, 1]],
		[[123, 2414], [123, 2414]],
		[[12, 13, 52, 23, 90, 55, 23, 11, 5, 7, 89, 2], [2, 5, 7, 11, 12, 13, 23, 23, 52, 89, 90]],
		[[5, 1, 4, 2, 8], [1, 2, 4, 5, 8]],
	]);
	console.log(sort())
	for (let [k, v] of tests.entries()) {
		let strTime = performance.now();
		console.log(`input: ${k}\noutput: ${sort(k, 0, k.length - 1)}\nresult: ${v}`);
		console.log(performance.now() - strTime, "\n--------------------\n");
	}
})()
