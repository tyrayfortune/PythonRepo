/* 
  Given in an alumni interview in 2021.
  String Encode
  You are given a string that may contain sequences of consecutive characters.
  Create a function to shorten a string by including the character,
  then the number of times it appears. 
  
  
  If final result is not shorter (such as "bb" => "b2" ),
  return the original string.
  */

  const str1 = "aaaabbcddd";
  const expected1 = "a4b2c1d3";
  
  const str2 = "";
  const expected2 = "";
  
  const str3 = "a";
  const expected3 = "a";
  
  const str4 = "bbcc";
  const expected4 = "bbcc";
  
  /**
   * Encodes the given string such that duplicate characters appear once followed
   * by a number representing how many times the char occurs only if the
   * character occurs more than two time.
   * - Time: O(?).
   * - Space: O(?).
   * @param {string} str The string to encode.
   * @returns {string} The given string encoded.
   */
  
  function encodeStr(str) { 
    var count = 0
    var solution = ""
    var char = str[0]
    for (var i = 0; i< str.length; i++){
      str[i]
      if ( str[i] === char){
        count ++
        
      }
      else{
        solution += char + count
        count = 1
        char = str[i]
        }
      }
    solution += char + count
    return solution
  }
  console.log(encodeStr(str1))




    // ITERATE THROUGHT str
        // FIND LIKE CHARACTERS and KEEP COUNT ON CHARS
        // ONCE WE FIND A NEW CHARACTER, START A NEW COUNT
        // CONCAT THE CHARACTER AND FREQUENCY TO THE SOLUTION
      