/*
A password is considered strong if the below conditions are all met:

It has at least 6 characters and at most 20 characters.
It contains at least one lowercase letter, at least one uppercase letter, and at least one digit.
It does not contain three repeating characters in a row (i.e., "...aaa..." is weak, but "...aa...a..." is strong, assuming other conditions are met).
Given a string password, return the minimum number of steps required to make password strong. if password is already strong, return 0.

In one step, you can:

Insert one character to password,
Delete one character from password, or
Replace one character of password with another character.
*/

func strongPasswordChecker(s string) int {
	var res int
	var a, A, d bool
	var l, r int
	var m int
	for r < len(s) {
		if s[r] >= 'a' && s[r] <= 'z' {
			a = true
		} else if s[r] >= 'A' && s[r] <= 'Z' {
			A = true
		} else if s[r] >= '0' && s[r] <= '9' {
			d = true
		}
		r++
		if r == len(s) || s[r] != s[r-1] {
			m += r - l/3
			l = r
		}
	}
	if !a {
		res++
	}
	if !A {
		res++
	}
	if !d {
		res++
	}
	if len(s) < 6 {
		return max(res, 6-len(s))
	}
	del := max(len(s)-20, 0)
	res += del
	m -= min(del, l)
	if m > 0 {
		res += m
	}
	return res
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
