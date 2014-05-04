using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProjectEuler
{
    // <summary>
    // @author: JWShumaker
    //
    // ProjectEuler.net
    // Problem ID 17
    // If the numbers 1 to 5 are written out in words: one, two, three, four, five,
    // then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
    //
    // If all the numbers from 1 to 1000 (one thousand) inclusive were written out
    // in words, how many letters would be used?
    //
    // Solution:
    // First, create a look-up table of the length of the corresponding sub-strings.
    // Next, while looping through the numbers, instead of forming the corresponding
    // words, sum up the letter counts of the substrings.
    // </summary>


    // A class that will contain string arrays storing words and methods for building
    //  words from a given integer.
    public class NumberWords
    {
        // String arrays of sub-words.
        private string[] digits_under_20 = {"and", "one", "two", "three", "four", "five",
                              "six", "seven", "eight", "nine", "ten", "eleven",
                              "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
                              "seventeen", "eighteen", "nineteen"
                              };

        private string[] digits_over_20 = {"hundred", "thousand", "twenty",
                              "thirty", "forty", "fifty", "sixty", "seventy",
                              "eighty", "ninety"
                              };

        // The main method of our class.  Returns the string of words for a given
        //   integer less than 100000.
        public string GetWord(int number)
        {
            if (number < 100)
            {
                // Our number is less than 100.
                return TwoDigit(number);
            }
            else if (number < 1000)
            {
                // Our number is greater than 99, but less than 1000.
                return ThreeDigit(number);
            }
            else if (number < 100000)
            {
                // Our number is in the thousands.
                return Thousands(number);
            }
            else
            {
                return "Number too large.";
            }
        }

        // Returns the word for a number in the thousands.
        private string Thousands(int number)
        {
            string return_string = null;

            // Determine if the last three digits are over 99.
            if (number % 1000 > 100)
            {
                return_string = " " + ThreeDigit(number % 1000);
            }
            else
            {
                // The last three digits are less than 100.  Are they greater than zero?
                if (number % 100 > 0)
                {
                    return_string = " " + digits_under_20[0] + " " + TwoDigit(number % 100);                    
                }
            }

            // What thousand do we have?
            return_string = TwoDigit(number / 1000) + " " + digits_over_20[1] + return_string;

            return return_string;
        }

        // Returns the word for a three digit number.
        private string ThreeDigit(int number)
        {
            string return_string = null;

            // Get words for the last two digits.
            if (number % 100 > 0)
            {
                return_string = " " + digits_under_20[0] + " " + TwoDigit(number % 100);
            }

            // What hundred do we need?
            return_string = digits_under_20[number / 100] + " " + digits_over_20[0] + return_string;

            return return_string;
        }

        // Returns the word for a two digit number.
        private string TwoDigit(int number)
        {
            if (number < 20)
            {
                // Returns the word for a one or two digit number under 20.
                return digits_under_20[number];
            }
            else
            {
                // Returns the word for a two digit number over 19.
                return digits_over_20[number / 10] + (number % 10 > 0 ? "-" + digits_under_20[number % 10] : "");
            }
        }
    }

    class Problem_17
    {
        static void Main(string[] args)
        {
            // Create our interactive database of number words.
            var words_list = new NumberWords();

            // Our letter count.
            int letter_count = 0;

            for (var i = 1; i < 1001; ++i)
            {
                System.Console.WriteLine(words_list.GetWord(i));
                letter_count += CountLetters(words_list.GetWord(i));
            };

            System.Console.WriteLine(letter_count);
            System.Console.ReadLine();

        }

         // A function to count the letters in a string.
        private static int CountLetters(string number)
        {
            int count = 0;
            foreach (char letter in number)
            {
                if (Char.IsLetter(letter))
                {
                    ++count;
                }
            }

            return count;
        }
    }
}
