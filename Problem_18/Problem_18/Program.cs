using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProjectEuler
{
    // <summary>
    // ProjectEuler.net
    // Problem ID 18
    // By starting at the top of the triangle below and moving to adjacent numbers on
    // the row below, the maximum total from top to bottom is 23.
    //
    // 3
    // 7 4
    // 2 4 6
    // 8 5 9 3
    //
    // That is, 3 + 7 + 4 + 9 = 23.
    //  
    // Find the maximum total from top to bottom of the triangle below:
    //   
    // 75
    // 95 64
    // 17 47 82
    // 18 35 87 10
    // 20 04 82 47 65
    // 19 01 23 75 03 34
    // 88 02 77 73 07 63 67
    // 99 65 04 28 06 16 70 92
    // 41 41 26 56 83 40 80 70 33
    // 41 48 72 33 47 32 37 16 94 29
    // 53 71 44 65 25 43 91 52 97 51 14
    // 70 11 33 28 77 73 17 78 39 68 17 57
    // 91 71 52 38 17 14 91 43 58 50 27 29 48
    // 63 66 04 68 89 53 67 30 73 16 69 87 40 31
    // 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
    //   
    // NOTE: As there are only 16384 routes, it is possible to solve this problem by
    // trying every route. However, Problem 67, is the same challenge with a triangle
    // containing one-hundred rows; it cannot be solved by brute force, and requires
    // a clever method! ;o)
    //   
    // Solution:
    // We will read our triangle into a multi-dimensional array.  Afterwards, we will
    // move through the array by rows starting at the top.  For each element of a row,
    // we will add the greatest adjacent number from the row above.  Our solution will
    // then be the maximum number in the bottom row of the triangle.
    // </summary>

    class Problem_18
    {
        static void Main(string[] args)
        {
            // Our triangle stored as a jagged array.
            int[][] the_triangle;

            // Where is our triangle's data?
            string triangle_data = "C:\\Users\\spiff\\Documents\\Visual Studio 2013\\Projects\\ProjectEuler\\ProjectEuler\\Problem_18_Data.txt";

            // Fill our triangle with data.
            ReadTriangle(triangle_data);//, out the_triangle);

            System.Console.ReadLine();


        }

        // Given a file name and a reference to a jagged array, fills the array with
        // data from the file.
        private static void ReadTriangle(string file_name)//, out int[][] the_triangle)
        {
            // Read the file into an array called lines.
            string[] lines = System.IO.File.ReadAllLines(file_name);

            // Pass through lines parsing it into the_triangle.
            foreach (string line in lines)
            {
                string[] row = line.Split(' ');
                int[] new_row = new int[row.Length];

                for (int i = 0; i < row.Length; ++i)
                {
                    new_row[i] = Convert.ToInt32(row[i]);
                }

                foreach (int number in new_row)
                {
                    System.Console.WriteLine(number + " ");
                }

                System.Console.WriteLine("\n");
            }

        }
    }
}
