sayHello :: String -> IO ()
sayHello x =
  putStrLn ("Hello, " ++ x ++ "!")

triple x = x * 3

mult (x, y) = x * y

areaOfCircleApprox x = 3.14 * x * x

areaOfCircle x = pi * x * x
