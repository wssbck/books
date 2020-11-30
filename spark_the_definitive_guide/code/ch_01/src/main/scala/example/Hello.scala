package example


import scala.concurrent._
import duration._
import core.Weather


object Hello extends App {
  val w = Await.result(Weather.weather, 10.seconds)
  Weather.http.close()
  println(s"Hello! The weather in New York is $w.")
}