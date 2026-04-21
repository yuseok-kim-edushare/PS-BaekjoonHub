namespace BOJ_C_sharp
{
    internal class Program_1002
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            int x1, y1, r1, x2, y2, r2, L2, rR, rr;

            for (int i = 0; i < n; i++)
            {
                string s = Console.ReadLine();
                string[] ss = s.Split();
                x1 = int.Parse(ss[0]);
                y1 = int.Parse(ss[1]);
                r1 = int.Parse(ss[2]);
                x2 = int.Parse(ss[3]);
                y2 = int.Parse(ss[4]);
                r2 = int.Parse(ss[5]);
                L2 = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2);
                rR = (r1 + r2) * (r1 + r2);
                rr = (r1 - r2) * (r1 - r2);
                if (L2 == 0 && r1 == r2)
                {
                    Console.WriteLine(-1);
                }
                else if (rR > L2 && L2 > rr)
                {
                    Console.WriteLine(2);
                }
                else if (rR == L2 || rr == L2)
                {
                    Console.WriteLine(1);
                }
                else
                {
                    Console.WriteLine(0);
                }
            }
        }
    }
}