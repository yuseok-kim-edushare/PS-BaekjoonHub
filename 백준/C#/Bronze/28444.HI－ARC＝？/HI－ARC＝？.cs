namespace BOJ_C_sharp
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string[] ss = Console.ReadLine().Split(' ', StringSplitOptions.RemoveEmptyEntries);
            int a = int.Parse(ss[0]) * int.Parse(ss[1]) - (int.Parse(ss[2])*int.Parse(ss[3])*int.Parse(ss[4]));
            Console.WriteLine(a.ToString());
        }
    }
}
