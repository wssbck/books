def forLoop {
  println("Java style loop")
  for(i <- 0 until args.length) {
    println(args(i))
  }
}

forLoop
