/* Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.*/

class Solution {
    func generateParenthesis(_ n: Int) -> [String] {
        var result = [String]()
        generateParenthesisHelper(n, n, "", &result)
        return result
    }
    
    func generateParenthesisHelper(_ left: Int, _ right: Int, _ str: String, _ result: inout [String]) {
        if left == 0 && right == 0 {
            result.append(str)
            return
        }
        if left > 0 {
            generateParenthesisHelper(left - 1, right, str + "(", &result)
        }
        if right > left {
            generateParenthesisHelper(left, right - 1, str + ")", &result)
        }
    }
}
