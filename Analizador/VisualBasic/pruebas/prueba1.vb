Imports System

Module Program
    Sub Main(args As String())
        Console.WriteLine("Hello World!")
        Console.WriteLine(vbCrLf + "Nombre men")
        ' name = Console.ReadLine()
        name = "Mikasa Ackerman"
        fecha = DateTime.Now
        Console.WriteLine($"{vbCrLf}Hola, {name}, en {fecha:d} at {fecha:t}")
        a As Integer = 10
        b As Integer = 5
        firstCheck, secondCheck As Boolean
        firstCheck = Not (a > b)
        secondCheck = Not (b > a)
        Console.WriteLine($"{firstCheck} | {secondCheck}")
        Console.WriteLine(vbCrLf + "Cualquier cosa para salir")
        Console.ReadKey(True)
    End Sub
End Module