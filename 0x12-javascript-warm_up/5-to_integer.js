#!/usr/bin/node

const x = process.argv
typeof(+x[2]) == "integer" ? `My number: ${x[2]} ` : "Not a number";

