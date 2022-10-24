function expand(expr) {
  
  // Get exponent
  const POWER = expr.split('^')[1];
  
  // Immediately returns a "1" if power is 0
  if (POWER == '0') {
    return '1'
  }
  
  // Get the base expression without parenthesis
  const BASEEXPR = expr.split('^')[0].substring(1, expr.split('^')[0].length - 1);
  
  // Get the value of a and b and the single character variable x
  var a = '';
  var b = '';
  var x = '';
  var isFirstVar = true;   // If the for loop detects a character variable, switch to appending to second variable
  
  for (let charInd in BASEEXPR) {
    if (BASEEXPR[charInd].match(/[a-z]/i)) {
      x = BASEEXPR[charInd];
      isFirstVar = false;
      continue;
    }
    if (isFirstVar) {
      a += BASEEXPR[charInd];
    }
    else {
      b += BASEEXPR[charInd];
    }
  }

  // If a is empty, it means a is just 1
  if (a == '') {
    a = '1'
  }
  else if (a == '-') {
    a = '-1'
  }
  
  // Store the expanded expression
  var expandedExpr = '';
  
  // A function to get a value in the Pascal triangle
  var pascal = function (n, r) {
    var numerator = 1;
    for (let i = n; i > (n - r); i--) {
      numerator *= i
    }
    var denominator = 1;
    for (let i = r; i > 0; i--) {
      denominator *= i
    }
    
    return (numerator / denominator)
  }
  
  for (let i = 0; i <= parseInt(POWER); i++) {
    let value = pascal(POWER, i) * (parseInt(a) ** (POWER - i)) * (parseInt(b) ** i)

    // Check if the value is positive, if so, then manually append the plus sign the expanded expression string
    if (value > 0) {
      
      // Check if the expanded expression string variable isn't empty, since the first number doesn't need a plus sign
      if (expandedExpr != '') {
        expandedExpr += '+'
      }
      expandedExpr += value
    }
    
    // Check if the value is negative, if so, just append the whole thing since the negative sign is also part of the value already
    else if (value < 0) {
      expandedExpr += value
    }

    // Else if the value is 0, skip, don't add anything
    else {
      continue
    }
    // If the value is 0, do nothing, because it is not supposed to be part of the expression
    
    // Now appending the single character variable
    // If the current power within the loop is more than 0, check if the value is 1, if so, then remove then number '1'
    if (POWER - i > 0 && value == 1 || POWER - i > 0 && value == -1) {
      expandedExpr = expandedExpr.substring(0, expandedExpr.length - 1)
    }
    
    // If the current power is more than 0, append the character
    if (POWER - i > 0) {
      expandedExpr += x
      
      // If the current power is more than 1, then add ^n where n is the power
      if (POWER - i > 1) {
        expandedExpr += `^${POWER - i}`
      }
    }
  }

  return expandedExpr
  
}

console.log(expand('(-w+1)^3'))