'''
You are investigating a cave. The cave has N rooms. There are underground passages that bidirectionally connect some pairs of rooms. Each room has at least one passage connected to it. No passage goes from a room to itself, and no two rooms are connected by more than one passage.

When in a room, you can identify what room you are in and see how many passages it connects to, but you cannot distinguish the passages. You want to estimate the number of passages that exist in the cave. You are allowed to do up to K operations. An operation is either:

be magically teleported to a room of your choice, or
walk through a random passage connected to the room you are in, taking you to the room at the other end of that passage.
When you decide to walk through a passage, you are unable to choose which one, because they are all alike. A passage is chosen for you uniformly at random.

You begin the investigation in an arbitrary room. Estimate the number of passages between rooms in the cave with at most K operations.

If E is your estimate and P is the actual number of passages, your solution is considered correct for a test case if and only if P⋅2/3≤E≤P⋅4/3.

To pass a test set, your solution must be correct for at least 90% of the test cases in that set.

Input and output
This is an interactive problem. You should make sure you have read the information in the Interactive Problems section of our FAQ.

Initially, your program should read a single line containing an integer, T, the number of test cases. Then, T test cases must be processed.

For each test case, your program must first read a line containing two integers N and K: the number of rooms in the cave, and the maximum number of room operations you are allowed. Rooms are numbered between 1 and N. The cave is determined at the beginning of the test case – it won't be changed while you explore it. Then, your program must process up to K+1 exchanges.

The i-th exchange starts with you reading a line containing two integers Ri and Pi, representing the number of the room you are currently in and the number of passages it connects to. Then, you must output a single line containing one of the following:

A single uppercase W: this means you want to walk through a random passage.
A single uppercase T and an integer S: this means you want to teleport to room S.
A single uppercase E and an integer E: this means you want to finish exploring and estimate that the cave contains E passages.
After an estimation operation, the judge will immediately start the next test case if there is one, regardless of the correctness of your estimation. If there is no next test case, the judge will wait for you to finish without any further output.

If the judge receives an invalidly formatted line from your program at any moment, or if your (K+1)-th exchange for a test case is not an estimation operation, the judge will print a single number −1 and will not print any further output. If your program continues to wait for the judge after receiving a −1, your program will time out, resulting in a Time Limit Exceeded error. Notice that it is your responsibility to have your program exit in time to receive a Wrong Answer judgment instead of a Time Limit Exceeded error. As usual, if the memory limit is exceeded, or your program gets a runtime error, you will receive the appropriate judgment.

'''
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
            getCurrentLocation
            while (i <= k) {
                val r = roomsNotVisited.toList(Random.nextInt(roomsNotVisited.size))
                addConnection(currentRoom, r)
                i += 1
            }
        }

        def walkThroughRandomPassage = {
            getCurrentLocation
            val r = roomsNotVisited.toList(Random.nextInt(roomsNotVisited.size))
            addConnection(currentRoom, r)
            i += 1
        }

        def walkThroughPassage = {
            getCurrentLocation
            val r = roomsNotVisited.toList(Random.nextInt(roomsNotVisited.size))
            addConnection(currentRoom, r)
            i += 1
        }

        def teleportToRoom(r: Int) = {
            getCurrentLocation
            addConnection(currentRoom, r)
            i += 1
        }

        def walkThroughPassageToRoom(r: Int) = {
            getCurrentLocation
            addConnection(currentRoom, r)
            i += 1
        }

        def walkThroughRandomPassageToRoom(r: Int) = {
            getCurrentLocation
            addConnection(currentRoom, r)
            i += 1
        }

        def walkThroughPassageToRoom(r: Int) = {
            getCurrentLocation
            addConnection(currentRoom, r)
            i += 1
        }

        def walkThroughRandomPassageToRoom(r: Int) = {
            getCurrentLocation
            addConnection(currentRoom, r)
            i += 1
        }

        def walkThroughPassageToRoom(r: Int) = {
            getCurrentLocation
            addConnection(currentRoom, r)
            i += 1
        }

        def walkThroughRandomPassageToRoom(r: Int) = {
            getCurrentLocation
            addConnection(currentRoom, r)
            i += 1
        }

        def walkThroughPassageToRoom(r: Int) = {
            getCurrentLocation
            addConnection(currentRoom, r)
            i += 1
        }

        def walkRandom = {
            val options = connections.filter(_._1 == currentRoom).map(_._2).toArray
            val chosen = options(Random.nextInt(options.length))
            println(s"W $chosen")
            getCurrentLocation
        }

        def estimate: Unit = {
            val Array(e) = readInputArrInt
            val p = connections.size
            val e2 = p * 2 / 3
            val e4 = p * 4 / 3
            if (e2 <= e && e <= e4) println("OK")
            else println("WRONG")
        }

        def addConnection(r1: Int, r2: Int): Unit = {
            connections += ((r1, r2))
            connections += ((r2, r1))
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
