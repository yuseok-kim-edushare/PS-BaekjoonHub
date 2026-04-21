using System;
class PS{
    static void Main() {
        string s = Console.ReadLine();
        string[] ss = s.Split();
        int a = int.Parse(ss[0]);
        int b = int.Parse(ss[1]);
        int c = int.Parse(ss[2]);
        Console.WriteLine((b*3*c)/a);
    }
}