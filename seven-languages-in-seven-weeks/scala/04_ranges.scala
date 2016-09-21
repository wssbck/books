println("a until range with step 1")
val range_until = 0 until 10
println(range_until)
println(range_until(5))
println(range_until.step)

println("a to range with step 3")
val range_to = (3 to 9) by 3
println(range_to)
println(range_to.step)
println(range_to(0))

println("a to range with step -1")
val range_to_minus = (20 to 9) by -1
println(range_to_minus)
println(range_to_minus.step)
println(range_to_minus(0))

println("a string range")
val range_string = ('a' to 'j') by 2
println(range_string)
println(range_string.step)
println(range_string(0))
