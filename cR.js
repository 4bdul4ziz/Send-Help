const readline = require('readline')

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})
const lines = []
rl.on('line', (input) => {
    lines.push(input);
})
rl.on('close', () => {

    let l = 0;
    let t = +lines[l++]
    for (let i = 0; i < t; i++) {
        const n = +lines[l++]
        const arr = lines[l++].trim().split(' ').map(Number)
        const ps = lines[l++].trim().split(' ').map(Number)
        console.log('Case #%d: %s', i + 1, solve(n, arr, ps));
    }
})

function dfs(adj, r, arr) {
    const stack = [[r, 0]]
    const dp = []
    let ans = 0
    while (stack.length) {
        const [u, i] = stack[stack.length - 1]

        const nb = adj[u] || []
        if (!i) {
        }
        if (i < nb.length) {
            stack[stack.length - 1][1]++
            const v = nb[i]
                stack.push([v, 0, u])
        } else {
            stack.pop()

            dp[u] = arr[u]
            if (nb.length > 1) {
                let min = Infinity
                let best
                nb.forEach((v, j) => {
                    if (dp[v] < min) {
                        min = dp[v]
                        best = j
                    }
                })
                nb.forEach((v, j) => {
                    if (j === best) {
                        dp[u] = Math.max(dp[u], dp[v])
                    } else {
                        ans += dp[v]
                    }
                })
            } else if (nb.length === 1) {
                dp[u] = Math.max(dp[u], dp[nb[0]])
            }
        }
    }
// console.log(dp)
    return ans + dp[r]
}
function solve(n, arr, ps) {
    arr.unshift(0)
    const adj = {}
    const rs = []
    ps.forEach((x, i) => {
        const a = i + 1
        const b = x
        if (x) {
            adj[b] = adj[b] || []
            // adj[a].push(b)
            adj[b].push(a)
        } else {
            rs.push(a)
        }
    })
    //
    let ans = 0
    rs.forEach(r => {
        ans += dfs(adj, r, arr)
    })
    return ans
}