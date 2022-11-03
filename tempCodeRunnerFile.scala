import scala.collection.mutable
import scala.io.StdIn
import scala.util.Random

object Solution {

    def readInputArrStr: Array[String] = StdIn.readLine().split(" ")
    def readInputArrInt: Array[Int] = readInputArrStr.map(_.toInt)
    def readInputStr: String = StdIn.readLine()
    def readInputInt: Int = StdIn.readInt()

    def runTestCase: Unit = {
        val Array(n, k) = readInputArrInt
        var i = 1
        val roomToNumOfPassages = mutable.Map[Int, Int]()
        val connections: mutable.Set[(Int, Int)] = mutable.Set()
        val roomsNotVisited: mutable.Set[Int] = mutable.Set()
        roomsNotVisited + += (1 to n)

        var currentRoom: Int = 0
        var currentRoomPassages: Int = 0
        var isReturnedToVisitedRoom: Boolean = false

        def getCurrentLocation: Unit = {
            val Array(r, p) = readInputArrInt
            isReturnedToVisitedRoom = roomToNumOfPassages.contains(r)
            roomToNumOfPassages(r) = p
            roomsNotVisited.remove(r)
            currentRoom = r
            currentRoomPassages = p
        }

        def teleportRandom = {
            val options = roomsNotVisited.toArray
            val chosen = options(Random.nextInt(options.length))
            println(s"T $chosen")
            getCurrentLocation
        }

        def walkRandom = {
            println("W")
            val prevRoom = currentRoom
            getCurrentLocation
            connections.add((prevRoom, currentRoom))
            connections.add((currentRoom, prevRoom))
        }

        getCurrentLocation
        while(i <= k & & roomsNotVisited.nonEmpty){
            // if(isReturnedToVisitedRoom){
                teleportRandom
                // } else if(currentRoomPassages )

            i += 1
        }

        val estimation: Int = {
            val avg = roomToNumOfPassages.values.sum / roomToNumOfPassages.size
            val totalSum = roomToNumOfPassages.values.sum + (roomsNotVisited.size * avg)
            totalSum/2
        }
        println(s"E $estimation")
    }

    def main(args: Array[String]): Unit = {
        val T: Int = readInputInt
        (1 to T).foreach(testIdx= > {
            runTestCase
        })
    }

}
