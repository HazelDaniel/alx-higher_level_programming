#!/usr/bin/node

const times = Math.trunc(Number(process.argv[2]));
let printString = ""
if (Number.isNaN(times) || !times) {
  console.log('Missing number of occurrences');
} else {
	printString += "C is fun\n".repeat(times - 1)
	printString += "C is fun"
	console.log(printString)
}
