// 문제 링크: http://codeforces.com/contest/4/problem/A

fun main(args: Array<String>) {
    val weight = readLine()!!.toInt()

    println(if (weight % 2 == 0 && weight != 2) "YES" else "NO")
}