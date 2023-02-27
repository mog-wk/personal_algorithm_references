"use strict";
const { performance } = require('perf_hooks');

function selectionSort(arr) {
	for (let i = 0; i < arr.length; i++) {
		if (typeof arr[i] !== "number") return "error";
		for (let j = i + 1; j < arr.length; j++)
			if (arr[j] < arr[i]) {
				let tmp = arr[j]
				arr[j] = arr[i]
				arr[i] = tmp
			}
			console.log(arr)
		}
	return arr;
}

(function () {
	const tests = new Map([
		[[12, 41, 5, 2, 3], [2, 3, 5, 12, 41]],
		[[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]],
		[[1, 1, 0], [0, 1, 1]],
		[[-1, 1, -1], [-1, -1, 1]],
		[[123, 2414], [123, 2414]],
		[["sadasd", 123], "error"],
		[[12, 13, 52, 23, 90, 55, 23, 11, 5, 7, 89, 2], [2, 5, 7, 11, 12, 13, 23, 23, 52, 89, 90]],
	]);

	for (let [k, v] of tests.entries()) {
		let strTime = performance.now();
		console.log(`input: ${k}\noutput: ${selectionSort(k)}\nresult: ${v}`);
		console.log(performance.now() - strTime, "\n--------------------\n");
	}
})()
