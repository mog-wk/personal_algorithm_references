"use strict";
const { performance } = require('perf_hooks');

function insertion_sort(arr) {
	for (let i = 1; i < arr.length-1; i++) {
		let j = i + 1;
		while (j > 0 && arr[j] > arr[j-1]) {
			swap(arr, j, j-1);
			j--;
		}
	}
	return arr
}

function swap(arr, a, b) {
	const tmp = arr[a] 
	arr[a] = arr[b]
	arr[b] = tmp
}

function main() {
	const tests = new Map([
		[[12, 41, 5, 2, 3], [2, 3, 5, 12, 41]],
		[[1, 1, 0], [0, 1, 1]],
		[[-1, 1, -1], [-1, -1, 1]],
		[[123, 2414], [123, 2414]],
		[["sadasd", 123], "error"],
		[[12, 13, 52, 23, 90, 55, 23, 11, 5, 7, 89, 2], [2, 5, 7, 11, 12, 13, 23, 23, 52, 89, 90]],
		[[5, 1, 4, 2, 8], [1, 2, 4, 5, 8]],
		[[7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7]],
		[[1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7]],
	]);
	for (let [k, v] of tests.entries()) {
		//let strTime = performance.now();
		console.time("t")
		console.log(`input: ${k}\noutput: ${insertion_sort(k)}\nresult: ${v}`);
		//console.log(performance.now() - strTime);
		console.timeEnd("t")
		console.log("\n=========================\n")
	}
}
main();
