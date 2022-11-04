/* Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses. */

func generateParenthesis(n int) []string {
	var res []string
	var dfs func(left, right int, s string)
	dfs = func(left, right int, s string) {
		if left == 0 && right == 0 {
			res = append(res, s)
			return
		}
		if left > 0 {
			dfs(left-1, right, s+"(")
		}
		if right > left {
			dfs(left, right-1, s+")")
		}
	}
	dfs(n, n, "")
	return res
}