using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProjectEuler
{
    // <summary>
    // @author: JWShumaker
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
            List<int[]> the_triangle;

            // Where is our triangle's data?
            string triangle_data = "C:\\Users\\spiff\\Documents\\GitHub\\ProjectEuler\\Problem_18\\Problem_18\\Problem_18_Data.txt";

            // Fill our triangle with data.
            ReadTriangle(triangle_data, out the_triangle);

            // Process the triangle and print the solution.
            System.Console.WriteLine(ProcessTriangle(ref the_triangle));

            System.Console.ReadLine();


        }

        private static int ProcessTriangle(ref List<int[]> the_triangle)
        {
            // Let's store the size of our list, we'll be using it a lot.
            int triangle_height = the_triangle.Count();

            // A one row triangle will trip our algorithm.
            if (triangle_height == 1)
            {
                return the_triangle[0].Max();
            }

            // This is the core of our algorithm for this solution.
            // Iterate through each row.  For each element, add the max of the
            // adjacent parent elements.  
            for (int row = 1; row < triangle_height; ++row)
            {
                for (int element = 0; element < the_triangle[row].Length; ++element)
                {
                    if (element == 0)
                    {
                        // There is only one adjacent parent element in this case.
                        // That element is the first element of the row above.
                        the_triangle[row][element] += the_triangle[row - 1][element];
                    }
                    else if (element == the_triangle[row].Length - 1)
                    {
                        // There is only one adjacent parent element in this case.
                        // That element is the last element of the row above.
                        // Note that this element is the last element of this row,
                        // hence the last element of the row above is element - 1.
                        the_triangle[row][element] += the_triangle[row - 1][element - 1];
                    }
                    else
                    {
                        // There are two adjacent parent elements.  Let's add the greatest.
                        the_triangle[row][element] += Math.Max(the_triangle[row - 1][element - 1], the_triangle[row - 1][element]);
                    }
                }
            }

            // Now, our solution to the problem is the largest element of the bottom row.
            return the_triangle[triangle_height - 1].Max();
        }

        // Given a file name and a reference to a jagged array, fills the array with
        // data from the file.
        private static void ReadTriangle(string file_name, out List<int[]> the_triangle)
        {
            // Initialize our list of arrays.
            the_triangle = new List<int[]>();

            // Read the file into an array called lines.
            string[] lines = System.IO.File.ReadAllLines(file_name);

            // Pass through lines parsing it into the_triangle.
            foreach (string line in lines)
            {
                // Convert the string 'line' into an array of strings split on spaces.
                // Then convert the array of strings into an array of ints.
                // Finally, add this new array to our triangle of numbers.
                the_triangle.Add(Array.ConvertAll(line.Split(' '), int.Parse));
            }     
        }
    }
}
