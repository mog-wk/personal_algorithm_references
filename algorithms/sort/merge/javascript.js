"use strict";
const { performance } = require('perf_hooks');

function sort(arr, l, r) {
	// arr left index, right index
	const merge = function (arr, l, m, r) {
		const nl = m - l + 1;
		const nr = r - m;

		const leftArr = []
		const rightArr = []

		for (let i = 0; i < nl; i++)
			leftArr[i] = arr[l + i];
		for (let i = 0; i < nr; i++)
			rightArr[i] = arr[m + 1 + i];
		console.log(arr, l, m, r, leftArr, rightArr)

		let [leftCounter, rightCounter, counter] = [0, 0, l]

		while (leftCounter < nl && rightCounter < nr) {
			if (leftArr[leftCounter] <= rightArr[rightCounter]) {
				arr[counter] = leftArr[leftCounter];
				leftCounter++;
			} else {
				arr[counter] = rightArr[rightCounter];
				rightCounter++;
			}
			counter++;
		}
		
		while (leftCounter < nl) {
			arr[counter] = leftArr[leftCounter];
			leftCounter++;
			counter++;
		}
		while (rightCounter < nr) {
			arr[counter] = rightArr[rightCounter];
			rightCounter++;
			counter++;
		}
	}
	if (l < r) {
		const mid = l + Math.floor((r - l) / 2);
		sort(arr, l, mid);
		sort(arr, mid+1, r);
		merge(arr, l, mid, r);
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
		[[5, 1, 4, 2, 8], [1, 2, 4, 5, 8]],
	]);
	for (let [k, v] of tests.entries()) {
		let strTime = performance.now();
		let klen = k.length - 1;
		console.log(`input: ${k}\noutput: ${sort(k, 0, klen)}\nresult: ${v}`);
		console.log(performance.now() - strTime, "\n--------------------\n");
	}
})()

