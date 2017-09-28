Module Triangles

  Function ComputeColor(Byref A as Char, Byref B as Char) as Char
    If A = B
      return A
    End If
    If B < A:
      Dim C as String
      C = A
      A = B
      B = C
    End If
    If A = "B" and B = "R"
      return "G"
    Else If A = "G" and B = "R"
      return "B"
    Else If A = "B" and B = "G"
      return "R"
    End If
  End Function

  Function Main() as Integer

    Dim FirstRow as String = Console.ReadLine()
    Dim Index as Integer
    Dim OuterIndex as Integer
    Dim CurrentRow() As Char
    Dim NextRow() As Char
    Dim FirstRowSize As Integer = Len(FirstRow)

    CurrentRow = New Char(FirstRowSize) {}

    For Index = 0 To FirstRowSize - 1
      CurrentRow(Index) = FirstRow(Index)
    Next
    For OuterIndex = 0 To (FirstRowSize-2)
      NextRow = New Char(Len(CurrentRow)-1) {}
      For Index = 0 To (Len(CurrentRow)-2)
        Dim v as Char = ComputeColor(CurrentRow(Index), CurrentRow(Index + 1))
        NextRow(Index) = v
      Next
      CurrentRow = NextRow
    Next
    Console.WriteLine(NextRow(0))
    return 0
  End Function

End Module
