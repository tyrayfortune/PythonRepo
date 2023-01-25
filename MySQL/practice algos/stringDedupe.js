/* 
  Given a string,
  return a new string with the duplicates excluded
  Bonus: Keep only the last instance of each character.
*/

const str1 = "abcABC";
const expected1 = "abcABC";

const str2 = "helloo";
const expected2 = "helo";

const str3 = "helloolllleeerrrrrr";
const expected3 = "helor";

/**
 * De-dupes the given string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str A string that may contain duplicates.
 * @returns {string} The given string with any duplicate characters removed.
 */
// freq counter {h:1, e: 1, l:2, o:2} 

// seen = {h: true, e:true, l: true}
seen ={} 
newstr =""
function stringDedupe(str) {
  for (var i = 0; i < str.length; i++){

    // console.log(seen, str[i])
    if (!seen[str[i]]){
      newstr += str[i]
      seen[str[i]] = true
      // console.log(seen)
    }
  }
  return newstr
  // return (stringDedupe)
    
  // for loop check for duplicates
}

// console.log(stringDedupe(str1))
// console.log(stringDedupe(str2))
console.log(stringDedupe(str3))


module.exports = { stringDedupe };