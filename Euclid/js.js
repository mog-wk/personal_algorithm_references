"use strict"

const tests = [
	[12, 54],
	[25, 5],
	[50, 10],
	[50, 20],
	[50, 45],
	[12, 3],
	[12, 6],
	[12, 8],
	[12, 10],
	[12, 11],
	[12, 12],
	[1123, 0],
	[2048, 256],
	[6623, 662],
	[12324, 9023],
	[2048, 909],
	[37, 17],
];

const mcd = function (...[m, n]) {
	if (m < n || n === 0) return 0;
	const loop = function (...[m, n]) {
		let r = m - n * Math.floor(m / n);
		if (r === 0)
			return n;
		else
			return loop(n, r);
	}
	return loop(m, n);
}

for (let test of tests)
	console.log(`inputs: ${test[0]} ${test[1]} output: ${mcd(...test)}`);
