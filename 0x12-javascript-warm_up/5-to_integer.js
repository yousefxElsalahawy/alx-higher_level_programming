// #!/usr/bin/node

const x = process.argv
typeof(parseInt(x[2])) == "integer" ? console.log(`My number: ${x[2]} `) : console.log("Not a number");

// console.log(parseInt(process.argv[2]) ? `My number: ${parseInt(process.argv[2])}` : 'Not a number');