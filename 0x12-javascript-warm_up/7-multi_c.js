#!/usr/bin/node

const floor_second_arg = Math.floor(Number(process.argv[2]));
if (isNaN(floor_second_arg)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < floor_second_arg; i++) {
    console.log('C is fun');
  }
}
